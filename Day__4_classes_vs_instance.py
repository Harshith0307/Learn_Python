class Person:
    def __init__(self, initialAge):
        if initialAge > 0:
            self.age = initialAge
        else: 
            self.age = 0
            print("Age is not valid, setting age to 0.")
    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif ((self.age >= 13) and (self.age < 18)):
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self, num_of_years=1):
        self.age = self.age + num_of_years
    def get_age(self):
        return self.age

test_cases = int(input())
for i in range(0, test_cases):
    per = Person(int(input()))
    per.amIOld()
    per.yearPasses(3)
    per.amIOld()



