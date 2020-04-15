#to extract 3,5,7,9,10,11,14,15

#Input
s=[1,2,3,[4,5,[6,7,[8,[9,[10],11],12],13],14],15]
len(s)

#Output

#to extract 3
print(s[2])

#to extract 4th list [4,5,[6....
s[3]

#to extract 5
print(s[3][1])

#to extract 7
print(s[3][2][1])

#to extract 9
print(s[3][2][2][1][0])

#to extract [10] as list
s[3][2][2][1][1]

#to extract 10
print(s[3][2][2][1][1][0])

#to extract 11
print(s[3][2][2][1][2])

#to extract 14
print(s[3][3])

#to extract 15
print(s[4])
