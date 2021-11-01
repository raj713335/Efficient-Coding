#for input use:
input_list = "-2,1,3,-4,5"
input_list = input_list.split(",")
input_list = [int(i) for i in input_list]

a = 0
b = 0
for i in input_list:
    new_b = b if b > a else a
    a = b + i
    b = new_b
print(b if b > a else a)
