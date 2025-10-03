import os
import cv2
import uuid
import time
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from utils.tracker import CentroidTracker
import imutils

UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'video' not in request.files:
        return redirect(url_for('index'))
    file = request.files['video']
    if file.filename == '':
        return redirect(url_for('index'))
    
    uid = str(uuid.uuid4())[:8]
    filename = f"{uid}_{file.filename}"
    in_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(in_path)

    out_name = f"out_{filename.rsplit('.',1)[0]}.mp4"
    out_path = os.path.join(app.config['RESULT_FOLDER'], out_name)
    min_area = int(request.form.get('min_area', 500))  
    counting_line_position = float(request.form.get('line_pos', 0.5)) 
    show_debug = request.form.get('debug', 'on') == 'on'

    vs = cv2.VideoCapture(in_path)
    if not vs.isOpened():
        return "Could not open video", 500

    W = int(vs.get(cv2.CAP_PROP_FRAME_WIDTH))
    H = int(vs.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = vs.get(cv2.CAP_PROP_FPS) if vs.get(cv2.CAP_PROP_FPS)>0 else 25

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(out_path, fourcc, fps, (W, H))

    backSub = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)

    ct = CentroidTracker(maxDisappeared=40, maxDistance=90)

    line_y = int(H * counting_line_position)
    total_up = 0
    total_down = 0
    track_history = {}

    frame_idx = 0
    while True:
        grabbed, frame = vs.read()
        if not grabbed:
            break
        frame_idx += 1
        fgMask = backSub.apply(frame)
        _, fg = cv2.threshold(fgMask, 200, 255, cv2.THRESH_BINARY)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        fg = cv2.morphologyEx(fg, cv2.MORPH_OPEN, kernel, iterations=2)
        fg = cv2.morphologyEx(fg, cv2.MORPH_DILATE, kernel, iterations=2)
        contours, _ = cv2.findContours(fg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        rects = []
        for c in contours:
            if cv2.contourArea(c) < min_area:
                continue
            (x, y, w, h) = cv2.boundingRect(c)
            rects.append((x, y, x+w, y+h))
            if show_debug:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 1)

        objects = ct.update(rects)
        for (objectID, (centroid, bbox)) in objects.items():
            cX, cY = centroid
            pts = track_history.get(objectID, [])
            pts.append((cX, cY))
            track_history[objectID] = pts[-30:] 
            if len(pts) >= 2:
                prev_y = pts[-2][1]
                cur_y = pts[-1][1]
        
                if prev_y < line_y and cur_y >= line_y:
                    total_down += 1
                elif prev_y > line_y and cur_y <= line_y:
                    total_up += 1

            if bbox is not None:
                (startX, startY, endX, endY) = bbox
                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)
            text = f"ID {objectID}"
            cv2.putText(frame, text, (cX - 10, cY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
            cv2.circle(frame, (cX, cY), 4, (255,0,0), -1)

        cv2.line(frame, (0, line_y), (W, line_y), (0,255,255), 2)
        cv2.putText(frame, f"Up: {total_up}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
        cv2.putText(frame, f"Down: {total_down}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
        cv2.putText(frame, f"Objects tracked: {len(objects)}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,0), 1)

        writer.write(frame)

    vs.release()
    writer.release()

    return render_template('result.html', output_video=out_name)

@app.route('/results/<path:filename>')
def get_result(filename):
    return send_from_directory(app.config['RESULT_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
