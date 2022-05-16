from itertools import count


class Person:
    def __init__(self,name,age,gender,interests):
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests

    def hello(self):
        print("Hello, my name is {}".format(self.name), end=" ")
        print(", my gender is {}".format(self.gender), end=" ")
        print("and i am {} years old.".format(self.age), end=" ")
        #print("My interests are {[0]}".format(self.interests), end="")
        #print(", {[1]}".format(self.interests), end=" ")
        #print("and {[2]}.".format(self.interests))
        interest_count = len(self.interests)
        ic=interest_count
        if interest_count == 0:
            print("My interests are, I have no interests.")
        elif interest_count == 1:
            print("My interest is {[0]}".format(self.interests), end="")
        else:
            print("My interests are {[0]}".format(self.interests), end="")
            print(", {[1]}".format(self.interests), end=" ")
            print("and {[2]}.".format(self.interests))
                 


person = Person("Mike", 25, "male",['Chess', 'Movies', 'Music'])
greeting = person.hello()
print(greeting)