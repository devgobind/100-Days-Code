# Python Syntax
#variables 
# We can declare variables in python just by declaring it , noneed to define the data types eg.
width = 20 #integer
height = 5.9 #float
msg = 'HI' #String

print msg , width * height
#output : HI 118.0
# There is full support for floating point; operators with mixed type operands convert the integer operand to floating point
print 3 * 3.75 / 1.5
#output : 7.5
#In addition to int and float, Python supports other types of numbers, such as Decimal and Fraction. Python also has built-in support for complex numbers, and uses the j or J suffix to indicate the imaginary part (e.g. 3+5j).
#String 
# String literals can span multiple lines. One way is using triple-quotes:
print ("""\
Usage : things
	name""")
# we can concat two strings with '+' sign.
#Fun Fact:Python indices may have negative number also. eg:
word = 'Python'
word[5]
word[-1]
#Output : 'n'
#Python also supports slicing i.e.,
word[0:2]
#Output : 'Py'
#Note: An omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.Python strings cannot be changed — they are immutable , it will cause an error.
#Lists: list of comma-separated values (items) between square brackets.
root = [1 , 8 , 27 , 64 , 125]
#Note : Difference between string and lists is that list is mutable where string isn't.
#Few built in functions
root.append(216)
len(root)
#Lists can be nested
a = ['a' , 'b' , 'c']
n = [1, 2, 3]
x = [a , n]
#output:[['a', 'b', 'c'], [1, 2, 3]]


 
