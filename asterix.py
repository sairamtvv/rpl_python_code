#asterix (*)

a = 5 * 7
lst = [1,2,3] * 5
power = 2 ** 3



def check(var):  #parameters
    print(var)

check(3) #argument


def demo(a, b ,c,*args, **kwargs) :
    print(a,b,c)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])
demo(1 ,2 ,3, 4, 7, 8,e=9, k=90, j=89) #positional
#demo (a=1, b=3, c=3) #keywords arguments


def verify(a, b, c):
    print(a, b,c)
lst = [2,5,6]
verify(*lst)

lst1 = [1, 2, 4]
lst2 = [5, 6, 7, 8]

lst3 = [*lst1, *lst2]
print(lst3)
#
#
# dict1 = {"a":1, "b":2}
# dict2 = {"c":3, "d":5}
# dict3 = {**dict1, **dict2}
# print(dict3)


#Tuple unpacking
# a, b, c = (1,2, 3 )
# a, *b , c = [1,2,3 ,4, 5 ,6, 7 ,8, 9, 10]
