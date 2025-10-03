# utils/tracker.py
# Simple centroid-based tracker for short-term tracking

import numpy as np
from scipy.spatial import distance as dist
from collections import OrderedDict

class CentroidTracker:
    def __init__(self, maxDisappeared=50, maxDistance=60):
        # next unique object ID
        self.nextObjectID = 0
        # maps objectID -> centroid (x,y)
        self.objects = OrderedDict()
        # tracks frames missed for each objectID
        self.disappeared = OrderedDict()
        self.maxDisappeared = maxDisappeared
        self.maxDistance = maxDistance

    def register(self, centroid, bbox=None):
        self.objects[self.nextObjectID] = (centroid, bbox)
        self.disappeared[self.nextObjectID] = 0
        self.nextObjectID += 1

    def deregister(self, objectID):
        if objectID in self.objects:
            del self.objects[objectID]
        if objectID in self.disappeared:
            del self.disappeared[objectID]

    def update(self, rects):
        """
        rects: list of bounding boxes [(startX, startY, endX, endY), ...]
        Returns dict: objectID -> (centroid, bbox)
        """
        # no detections
        if len(rects) == 0:
            # mark all existing as disappeared
            for oid in list(self.disappeared.keys()):
                self.disappeared[oid] += 1
                if self.disappeared[oid] > self.maxDisappeared:
                    self.deregister(oid)
            return self.objects

        # compute input centroids
        inputCentroids = []
        for (startX, startY, endX, endY) in rects:
            cX = int((startX + endX) / 2.0)
            cY = int((startY + endY) / 2.0)
            inputCentroids.append((cX, cY))

        # if no existing objects, register all
        if len(self.objects) == 0:
            for i, centroid in enumerate(inputCentroids):
                self.register(centroid, rects[i])
        else:
            # existing object IDs and centroids
            objectIDs = list(self.objects.keys())
            objectCentroids = [self.objects[oid][0] for oid in objectIDs]

            # compute distance matrix between object centroids and input centroids
            D = dist.cdist(np.array(objectCentroids), np.array(inputCentroids))

            # find the smallest value in each row then sort row indexes based on min values
            rows = D.min(axis=1).argsort()
            cols = D.argmin(axis=1)[rows]

            usedRows = set()
            usedCols = set()

            for (row, col) in zip(rows, cols):
                if row in usedRows or col in usedCols:
                    continue
                if D[row, col] > self.maxDistance:
                    continue

                objectID = objectIDs[row]
                self.objects[objectID] = (inputCentroids[col], rects[col])
                self.disappeared[objectID] = 0

                usedRows.add(row)
                usedCols.add(col)

            # compute unused rows and cols
            unusedRows = set(range(0, D.shape[0])).difference(usedRows)
            unusedCols = set(range(0, D.shape[1])).difference(usedCols)

            # if the number of object centroids >= input centroids -> increase disappeared
            if D.shape[0] >= D.shape[1]:
                for row in unusedRows:
                    objectID = objectIDs[row]
                    self.disappeared[objectID] += 1
                    if self.disappeared[objectID] > self.maxDisappeared:
                        self.deregister(objectID)
            else:
                # register new objects
                for col in unusedCols:
                    self.register(inputCentroids[col], rects[col])

        return self.objects
