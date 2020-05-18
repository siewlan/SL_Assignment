Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Assignment - Session22 (Create function to pass multiple strings and join them together and return a sentence)
>>> 
>>> def sentence(*text):
	newsentence=""
	for each in text:
		newsentence=newsentence+" "+each
	return "The sentence is: "+newsentence

>>> 
>>> sentence("Today is","a wonderful day for","an outing")
'The sentence is:  Today is a wonderful day for an outing'
>>> 