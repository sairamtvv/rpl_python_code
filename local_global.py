# mutable objects can be chaged
#immutable objects canot be changed
#if we rebind the reference in the method,




def num_func():
    #
    global num
    num = 9
    print(f"from inside function {num}")
num = 5
num_func()
print(f"from outside function {num}")

# def demo(a_lst):
#     #number = 3
#     #a_lst = [1,2,3]
#     a_lst[0] = 8
#     a_lst.append(7)
#     print(f"from inside function {a_lst}")
#
#
#
#
# mylist  = [1,2,3]
# demo(mylist)
# print(f"from outside function {mylist}")