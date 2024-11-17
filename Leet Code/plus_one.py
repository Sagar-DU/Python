array = [1, 2, 3]
string = ""
for i in array:
    string += str(i)
add = int (string) + 1

new_array = list(str(add))

plus_one = []
for i in new_array:
    plus_one.append(int(i))

print (plus_one)