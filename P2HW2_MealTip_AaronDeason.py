Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # a program that calculates the total amount of a meal purchased at a restaurant.The program will ask the user to enter the charge for food and calculate the amount of the following tip percentages: 15% 18% 20%
>>> # 6/23/2019
>>> #CTI-110 P2HW2- Meal Tip Calculator
>>> # Aaron Deason
>>> #
>>> meal = 44.50
>>> tax = 0.0675
>>> tip = .15
>>> 
>>> meal = meal + meal * tax
>>> total = meal + meal * tip
>>> 
>>> print("%.2f" % total)
54.63
>>> tip2 = .18
>>> 
>>> meal = meal + meal * tax
>>> total = meal + meal * tip2
>>> 
>>> print("%.2f" % total)
59.84
>>> tip3 = .20
>>> 
>>> meal = meal + meal * tax
>>> total = meal + meal * tip3
>>> 
>>> print("%.2f" % total)
64.96
>>> 
