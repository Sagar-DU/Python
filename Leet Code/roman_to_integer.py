roman_values = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}
roman = "XIV"
decimal = 0
previous_value = 0
for i in reversed(roman):
    current_value = roman_values[i]
    if (current_value < previous_value):
        decimal -= current_value
    else:
        decimal += current_value
    previous_value = current_value
    

print ("The decimal of the roman number is:", decimal)