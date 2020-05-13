Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Assignment - Session16
>>> #To create a function that takes 3 numbers and returns the greatest of the 3
>>> 
>>> def greatest(a,b,c):
	if a>b and a>c:
		return str(a)+"-->a is the greatest"
	elif b>a and b>c:
		return str(b)+"-->b is the greatest"
	else:
		return str(c)+"-->c is the greatest"

	
>>> 
>>> greatest(1,2,3)
'3-->c is the greatest'
>>> greatest(1,3,2)
'3-->b is the greatest'
>>> greatest(3,1,2)
'3-->a is the greatest'
>>> 