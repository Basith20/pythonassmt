import math

def factorial(n):
	return 1 if (n==1 or n==0) else n * factorial(n - 1);


def findlog10(n):
	return math.log10(14)


def converttoradian(degree):
    pi = 3.14159265359;
    return (degree * (pi / 180));


def trignomrtricfun(n):
    return "sin value of " + str(n) +" is " + str(math.sin(n)) +" "+"cos value of "+ str(n) +" is "+ str( math.cos(n))+" "+"tan value of "+ str(n) +" is "+ str(math.tan(n))
 
print(trignomrtricfun(math.pi/6))