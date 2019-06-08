#Lesson 6: Object Oriented Programing

#Time class
class Time:
    """Blueprint for Time object"""
    def __init__(self): #I spelled "init" wrong but
        #the program still worked except for... (a few liens down)
        self.hour = 0
        self.minute = 0
        self.second = 0
    def set_time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def print_time(self):
        print(self.hour, ":", self.minute, ":", self.second)
#myTime1 = Time()
#myTime1.print_time() #This function here. So a class in Python does not need
#myTime1.set_time(1,1,1) #a default constructor in order to work.
#myTime1.print_time() #Try to comment out the default constructor and the line 2 above
                    #The program will run just fine.

#Second object can be created
#myTime2 = Time()
#myTime2.print_time()
#myTime2.set_time(1,2,3)
#myTime2.print_time()

#Time2 class that restricts client program from accessing data fields
class Time2:
    """Blueprint for Time2 object that fixes the client access"""
    def __init__(self):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0
    def set_time(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    def print_time(self):
        print(self.__hour, ":", self.__minute, ":", self.__second)
    #Getter (Or Accessor) Function - a function in which the client can obtain the value of a variable in an object
    def get_hour (self):
        print(self.__hour)
    def get_minute (self):
        return self.__minute
    def get_second (self):
        return self.__second
    #Setter (Or Mutator) Function - a function in which the client can change variables in an object through the class
    def set_hour(self, hour):
        self.__hour = hour
    def set_minute(self, minute):
        self.__minute = minute
    def set_second(self, second):
        self.__second = second
