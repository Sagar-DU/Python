x = input ("Enter a number: ")

reverse = x[::-1]

if (int(x) < 0):
    print ("The number is not a Palindrome.")
elif (int(x) == int(reverse)):
    print ("Palindrome!")
else:
    print ("The input number is not a Palindrome.")