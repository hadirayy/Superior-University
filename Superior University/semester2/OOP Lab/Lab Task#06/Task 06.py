class Course:
    def __init__(self,course_code,course_name):
        self.course_code=course_code
        self.course_name=course_name
    def display_info(self):
        print(f"course_code:{self.course_code}")
        print(f"course_name:{self.course_name}")
class UndergraduateCourse(Course):
    def __init__(self,course_code,course_name,year_level):
        super().__init__(course_code,course_name)
        self.year_level=year_level
    def additional_info(self):
        print(f"Year_level:{self.year_level}")
class GraduationCourse(Course):
    def __init__(self,course_code,course_name,research_area):
        super().__init__(course_code,course_name)
        self.research_area=research_area
    def additional_info(self):
        print(f"Reseach_area{self.research_area}")
def Register_course():
    course_type = input("Enter the course Type(Undergraduation\Graduation):")
    course_code = input("Enter the Course Code:")
    course_name = input("Enter the Course_Name:")
    if course_type =="Undergraduation":
        year_level =input("Enter year level:"  )
        course=UndergraduateCourse(course_code,course_name, year_level)
    elif course_type == "Graduation":
        research_area=input("Enter research area:")
        course =GraduationCourse(course_code,course_name,research_area)
    else:
        print("Invalid course_type")
        return
    course.display_info()
    course.additional_info()
Register_course()    