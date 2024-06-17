#user can give multiple operations

["add", "sub", "mul", "div", ""]

oper_lst = ["add", "mul"]
a = 2
b = 3

for oper in oper_lst:
    if oper=="add":
        print(f"add value is {a + b}")
    elif oper=="sub":
        print(f"sub value is {a - b}")
    else:
        print(f"invalid operation")