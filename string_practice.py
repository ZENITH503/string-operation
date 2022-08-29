b = 'harrymetsejalfuckinglovelybitch'
c= "harry's"
d= '''harry "s'''
print(b)
print(d)
print(c)
#uses of single double and triple quotes to print string literal
#concatenating two strings 
a = b+c
print(a)
#slicing strings or getting the leetter for usage
print(b[0])
print(b[1])
# we can access a string character but cannot change it
#in order to get a set of character from the string literal we use
print(a[0:3])
#here 3 is not included in the list and 0 is inlcuded in the list
e= b[-3:-1]
print(e)
#here -1 index no. is given to the last character of the string and the seqence of -1, -2 ,-3,so on starts from backwards
# [:3]is same as[0:3]
# [0:]is same as[0:4] in case of b= 'harry'
#in case of negative indices [-3:-1] -1 indice character wud be left out and -3 ,-2, wud be printed. 
print(b[0:20:2])
# here skipping values is done where 2 indicates tht 2 letters wud be missed while printing charaters from 0 to 20 index no.
