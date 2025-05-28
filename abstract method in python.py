from abc import ABC,abstractmethod

class vehicle(ABC):

    @abstractmethod
    def motion(self):
        pass

    @abstractmethod
    def nonmotion(self):
        return "horn"
    
class car(vehicle):

    def motion(self):
        print("car is moving") 

    def nonmotion(self):
        print('car is not moving')

v1 = car()

v1.motion()
v1.nonmotion()

class motorbike(vehicle):

    def motion(self):
        print('bike is moving')

    def nonmotion(self):
        print('bike is not moving')

v2 = motorbike()
v2.motion()
v2.nonmotion()

