# Objective: Get started with Python syntax.
# Audience: Programmers with basic knowledge of OOP.
 
# import modules
from math import pi, sqrt # import multiple 
from re import match as re_match # set alias
 
# class definition and inheritance
class Animal:
 __character = "Positive" # won't be imported via "from module_name import *"
 _gender = "Unknown" # not suggested to access
 """
 Document comments, will be retained in runtime
 """
 def __init__(self, name, age):
  self.name = name
  self.age = age
 
 def shout(self): # define a method
  print("Sound")
 
 def live(self):
  print("Alive!")
 
 def train(behavior): # decorator
  def wrap():
   behavior()
  return wrap
 
 @property # a read-only property
 def gender(self):
  return self._gender
 
 @gender.setter # setter for gender property
 def gender(self, value):
  if value:
   self._gender = value
  else:
   print("Gender not set")
 
class Wolf(Animal): # inherited from Animal class
 def shout(self, default = "Woof!", *sounds, **tones):
  print(default)
  if len(sounds) &gt; 0:
   print(sounds[0])
  print(tones) # {'key':value,}
 
 def bite(self):
  print("Bite!")
 
class Dog(Wolf):
 def shout(self):
  print("Woo")
 
 def bite(self):
  print("Bite?")
  super().shout()
 
 def __add__(self, other): # change the behavior of + operator
  return Dog(self.name + " and " + other.name, self.age + other.age)
 
 def __special_behavior(self): # won't be imported via "from module_name import *"
  print("Read books!")
 
 @classmethod # define class method
 def find_a_puppy(cls, name):
  return cls(name, 0)
 
 @staticmethod # define static method
 def find(times)
  print((self.name + "!") * 3)
 
 @train
 def run():
  print("train running")
 
# define an object of the class
puppy = Dog("Puppy", 5)
print(puppy.age) # 5
puppy.live() # Alive!
puppy.shout() # Woo
puppy.bite() # Bite? Woof!
print(_Animal__character) # Positive
 
# array
def add_one(x):
 return x + 1
 
nums = [1,2,3]
result_map = list(map(add_one,nums)) # [2,3,4]
result_filter = list(filter(lambda x:x%2==0,nums)) # [1,3]
nums[0:2:1] # [1,2,3]
nums[1:-1] # [2,3]
first = nums[0]
print(list(range(3))) # [0,1,2]
 
# Generator 与循环
def infinitive_loop():
 i = 1
 while True:
  yield i
  if True:
   i += 1
  elif False:
   i = 0
  else
   i = 1
 
for i in infinitive_loop():
 print(i) # 1 2 3...
 if False:
  break
else:
 print("finished without break")
 
# set
num_set = {1,2,3}
print(3 in num_set) # True
 
# dictionary
age_dictionary = {"Alice":17, "Bob":18}
print(age_dictionary["Alice"]
 
# tuple
immutable_tuple = ("A","B") # tuple is immutable
simple_tuple = 1,2,3
a,b = immutable_tuple
a, *b, c = [1,2,3,4] # a 为 1, b 为 [2,3]，c 为 4
b = 5 if a == 2 else 3 # b 为 3 
 
# format a string
string_format_sample = "String: {0} {1} {x}".format("A","B",x="C")
 
# exception handling
try:
 print(1/0)
 assert (2 + 2 == 6), "wrong answer" # AssertionError:wrong answer
 with open("file.txt") as f:
  print(f.read())
 file = open(file.txt)
 print("A" * 3) # AAA
 n = int("9")
except ZeroDivisionError:
 print("Devided by zero"
except (ValueError, TypeError):
 print("Error")
finally:
 file.close()
 print("Finally")
 raise
 
input("Enter a number: ")
 
if __name__=="__main__":
 print("Won't be printed if it is imported")
