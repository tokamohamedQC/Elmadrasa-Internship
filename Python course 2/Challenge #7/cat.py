class cat:
    def __init__(self, name, color, stepsOfwalk, stepsOfrun, age, type):
        self.name = name
        self.color = color
        self.age = age
        self.type = type
        self.stepsOfwalk = stepsOfwalk
        self.stepsOfrun = stepsOfrun
    
    def walks(self):
        result = self.common()
        result += f" and my steps of walk {self.stepsOfwalk} per second"
        print(result)
    
    def runs(self):
        result = self.common()
        result += f" and my steps of run {self.stepsOfrun} per second"
        print(result)
    
    def common(self):
        result = f"My name is {self.name}"
        result += f" and my color is {self.color}"
        result += f" and my age is {self.age}"
        result += f" and my type is {self.type}"
        return result