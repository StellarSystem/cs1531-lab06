class ConferenceCenter:

    def__init__(self, name):
        self._name = name
        self._courses = []
    
    def print(self):
        print(self._name)
        
    def add_course(self, course):
        self._courses.append(course)
    
    def __str__(self):
        return "PRONTE"

class Course:
    
    def __init__(Self, name):
        self._name = name
        
unsw = ConferenceCenter("UNSW")

comp1531 = Course("COMP1531")
unsw.add_course()
comp1531.change_name("COMP2911")
print(unsw)

