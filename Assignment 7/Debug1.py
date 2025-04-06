'''
note: welcome f:
"when using an "f" in front of a string, all the variables inside curly brackets are read and replaced by their value"
thank you stackoverflow!
keep in mind adding parentheses to the return if you use f disables it!

All of these classes are built for you! you just need to work inside of main!... but you do need to understand the classes!
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years young"

    def work(self):
        return "I am working!"

class Janitor(Person):
    def __init__(self, name, age, building):
        super().__init__(name, age)
        self.building = building

    def work(self):
        """Override"""
        return f"I maintain {self.building}."

    def clean(self, room):
        """Not inherited """
        return f"I'm cleaning {room} in {self.building}."

class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def work(self):
        """Override"""
        return f"I am a {self.specialization} doctor."

    def diagnose(self, patient, illness):
        """Not inherited"""
        return f"I have diagnosed {patient} with {illness}"

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def work(self):
        """Override"""
        return f"I teach {self.subject}."

    def teach(self, topic, students):
        """Not inherited """
        return f"I am teaching {topic} to {students}."


def main():
    #make a janitor, a doctor, and a teacher for me!

    #have them introduce themselves and what they do! (call all of their functions!)
    
    #In a comment (or in brightspace), explain to me exactly where each line printed in terminal came from (which class, what function, etc)


main()
