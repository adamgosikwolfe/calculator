#calculator 

from math import *

def add(x,y):
	return x+y

def subtract(x,y):
	return x-y

def multiply(x,y):
	return x*y

def divide(x,y):
	return x/y

def power(x,y):
	return pow(x,y)

functions = "+", "-", "*", "/", "^"
operator = {"+":add, "-":subtract, "*":multiply, "/":divide, "^":power}

on = True
while on == True:
	operation = input("Type the operation.\n + : Addition\n - : Subtraction\n * : Multiplication\n / : Division\n ^ : Exponential\n")
	x = float(input("First number:"))
	y = float(input("Second number:"))
	result = operator[operation](x,y)
	print(result)
	loop = input("q to quit")
	if loop == "q":
		on = False


