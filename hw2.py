#for number in range(101):
# print(number)
# for number in range(101):
#   print(f"order is {number}")
# for number in range(101):
#   if number % 5 == 0:
#     print(number)
#from datetime import datetime, timedelta
#date_string = "2024-12-15"
#date_object = datetime.strptime(date_string, "%Y-%m-%d")
#print(date_object)
#new_date = date_object + timedelta(days=7)
#print(new_date)
#print(new_date.strftime("%B-%d-%Y"))
#import numpy as np
#def f (A,K,L):
#  return (A*(K**0.3)*(L**0.7))
#A=np.array([1,2,3])
#K=np.array([4,5,6])
#L=np.array([7,8,9])
#result = f(A,K,L)
#print(result)
person1 = {"name": "Bat", "age": 25, "salary": 2000, "birth": "2001-11-08"}
person2 = {"name": "Bold", "age": 30, "salary": 2500, "birth": "2002-06-24"}
person3 = {"name": "Saruul", "age": 22, "salary": 1800, "birth": "2003-03-15"}
person4 = {"name": "Tsetseg", "age": 28, "salary": 2200, "birth": "1997-08-20"}
person5 = {"name":"Temuulen", "age": 35, "salary": 3000, "birth": "1985-12-01"}
import pandas as pd
data = [person1, person2, person3, person4, person5]
hun = pd.DataFrame(data)
print(hun)