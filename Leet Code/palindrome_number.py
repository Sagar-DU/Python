x = input ("Enter a number: ")

reverse = x[::-1]

if (int(x) == int(reverse)):
    print ("Palindrome!")
else:
    print ("The input number is not a Palindrome.")
print ("Direct number:", x)
print ("Reversed number:", reverse)