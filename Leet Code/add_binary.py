a = "1010"
b = "1011"

decimal = int (a, 2)
decimal2 = int (b, 2)
# count = 0

# for i in reversed(a):
#     decimal += (int(i) * pow(2, count))
#     count += 1

# count = 0
# for i in reversed(b):
#     decimal2 += (int(i) * pow(2, count))
#     count += 1

sum = decimal + decimal2
binary_sum = format(sum, "b")

print(binary_sum)
