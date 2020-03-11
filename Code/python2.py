# INSTRUCTIONS

# In case it is not clear, the Question appears first, then examples, then any hints and finally the function that you need to complete appears underneath:

# <QUESTION>

# <EXAMPLES>

# <HINT>

# You are NOT allowed access to the internet for this assessment, instead you should use the DOCUMENTATION that comes bundled with your Python installation.  You should already be comfortable accessing this documentation, but to summarise:

# Access Python from you CLI

# Type help() or for example help(str)


# <QUESTION 1>

# Given a string, return a string where for every char in the original string, there are three chars.

# <EXAMPLES>

# one("The") → "TTThhheee"
# one("AAbb") → "AAAAAAbbbbbb"
# one("Hi-There") → "HHHiii---TTThhheeerrreee"

# <HINT>
# How does a for loop iterate through a string?

def one(string):
	return ''.join(c*3 for c in string)
	# Long version
	# outword = ''  # empty output var to be added to
	# for c in string:  # iterate through characters in the string
	# outword = outword + (c*3)  # concatenation of output and multiplied chars
	# return outword



# <QUESTION 2>

#  Write a function which returns the boolean True if the input is only divisible by one and itself.

# The function should return the boolean False if not.

# <EXAMPLES>

# two(3) → True
# two(8) → False

# <HINT>
# What operator will give you the remainder?
# Use your CLI to access the Python documentation and get help manipulating strings - help(range).

def two(number):
	Prime = True  # assume prime by default, easier to check for divisibility.
	for d in range(2,number//2):  # loop over all possible divisors.
		if number % d == 0:  # is the number divisible by the test divisor?
			Prime = False  # if so, it isn't prime.
			break  # don't want to check any further, we know it isn't prime.
	return Prime


# <QUESTION 3>

# Write a function which takes an integer input, a, and returns the sum a+aa+aaa+aaaa.

# So if 2 was the input, the function should return 2+22+222+2222 which is 2468.

# <EXAMPLES>

# three(9) → 11106
# three(5) → 6170

# <HINT>
# What happens if you multiply a string by a number?

def three(a):
	return sum(map(int,(str(a),str(a)*2,str(a)*3,str(a)*4)))
# 	Long version:
# 	sa = str(a)  # converting to string makes it easier to produce aaaa etc
# 	(sat,sah,saf) = (sa*2,sa*3,sa*4) # produce extended strings
# 	return sum(map(int,(sa,sat,sah,saf)))  # sum the values together after mapping them to integers


# <QUESTION 4>

# Given two Strings of equal length, 'merge' them into one String.

# Do this by 'zipping' the Strings together.

# Start with the first char of the first String.
# Then add the first char from the second String.
# Then add the second char from the first String.
# And so on.

# Maintain case.

# You will not encounter whitespace.

# <EXAMPLES>

# four("String","Fridge") → "SFtrriidngge"
# four("Dog","Cat") → "DCoagt"
# four("True","Tree") → "TTrrueee"
# four("return","letter") → "rleettutrenr"

# <HINT>
# Use your CLI to access the Python documentation and get help manipulating strings - help(list.insert).
# Who would you seperate a string into characters?

def four(input1, input2):
	return ''.join(input1[i] + input2[i] for i in range(0, len(input1)))
# 	Long version:
# 	o = ''
# 	for i in range(0, len(input1)):  # loop over all possible string indexes
# 		o = o + input1[i]  # add char i of string 1
# 		o = o + input2[i]  # then add char i of string 2
# 	return o


# <QUESTION 5>

# Write a function to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

# <EXAMPLES>

# five() → [100,102,122,198,200]
# five() → [108,104,106,188,200]
# five() → [154,102,132,178,164]

# <HINT>
# There is a module which can be used to generate random numbers, this module is called random.
# The random module contains a function called randint.

def five():
	from random import randint
	return [(randint(100, 201)//2)*2,(randint(100, 201)//2)*2,(randint(100, 201)//2)*2,(randint(100, 201)//2)*2,(randint(100, 201)//2)*2]
# 	Long version:
# 	outlist = []
# 	while len(outlist) < 5:  #
# 		number = randint(100, 201)  # get a random integer in desired range (including 200)
# 		if number % 2 == 0:  # if the random number is even
# 			outlist.append(number)
# 	return outlist


# <QUESTION 6>

# Given a string, return the boolean True if it ends in "py", and False if not.

# Ignore Case.

# For Example:

# six("ilovepy") → True
# six("welovepy") → True
# six("welovepyforreal") → False
# six("pyiscool") → False

# <HINT>
# There are no hints for this question.

def six(string):
	return True if string.lower()[-2:] == 'py' else False
	# Long version
	# l = string.lower()
	# if l[-2:] == 'py':
	# 	return True
	# else:
	# 	return False


# <QUESTION 7>

# Given three ints, a b c, one of them is small, one is medium and one is large.

# Return the boolean True if the three values are evenly spaced, so the
# difference between small and medium is the same as the difference between
# medium and large.

# Do not assume the ints will come to you in a reasonable order.

# <EXAMPLES>

# seven(2, 4, 6) → True
# seven(4, 6, 2) → True
# seven(4, 6, 3) → False
# seven(4, 60, 9) → False

# <HINT>
# There is a function for lists called sort.
# Use the cli to access the documentation help(list.sort)

def seven(a, b, c):
	return True if sorted([a,b,c])[1] - sorted([a,b,c])[0] == sorted([a,b,c])[2] - sorted([a,b,c])[1] else False
	# Long version
# 	l = sorted([a, b, c])  # put inputs into a list sorted in ascending order
# 	if l[1] - l[0] == l[2] - l[1]:  # if differences are equal:
# 		return True
# 	else:
# 		return False


# <QUESTION 8>

# Given a string and an integer, n, return a string that removes n letters from the 'middle' of the string.

# The string length will be at least n, and be odd when the length of the input is odd, so there will always be a 'middle'.

# <EXAMPLES>

# eight("Hello", 3) → "Ho"
# eight("Chocolate", 3) → "Choate"
# eight("Chocolate", 1) → "Choclate"

# <HINT>
# Use the cli to access the documentation help(str.replace)

def eight(s, a):
	return '' if a >= len(s) else s[0:((len(s) - a) // 2)] + s[-((len(s) - a) // 2):]
# 	Long version:
# 	if a >= len(s):
# 		return ''
# 	else:
# 		l = (len(s) - a) // 2
# 		start = s[0:l]
# 		end = s[-l:]
# 		return start + end

# <QUESTION 9>

# Given two string inputs, if one can be made from the other return the boolean True, if not return the boolean False.

# <EXAMPLES>

# nine("god", "dog") → True
# nine("tree", "tiredest") → True
# nine("cat", "dog") → False
# nine("tripping", "gin") → True

# <HINT>
# There are no hints for this question.

def nine(string1, string2):
	A = False
	B = False
	for c in string1:
		if c in string2:
			A = True
		else:
			A = False
			break
	for d in string2:
		if d in string1:
			B = True
		else:
			B = False
			break
	return True if A == True or B == True else False


# <QUESTION 10>

# Write a function which takes 2 integers greater than 0, X,Y as input and generates a 2-dimensional array.

# The element value in the i-th row and j-th column of the array should be i*j.

# <EXAMPLES>

# ten(3,2) → [[0,0,0],[0,1,2]]
# ten(1,1) → [[0]]
# ten(3,4) → [[0,0,0],[0,1,2],[0,2,4],[0,3,6]]

# <HINT>
# Think about nesting for loops.

def ten(X, Y):
	outlist = []
	for j in range(Y):  # Columns
		ylist = []
		for i in range(X):  # Rows nested within columns
			ylist.append(i * j)
		outlist.append(ylist)
	return outlist

