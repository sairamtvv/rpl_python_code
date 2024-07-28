my_str = "my number is 9022257710"
#9022257710

lst = my_str.split()
print(lst)

# map(lamda x)


for i in lst:
    try:
        k = int(i)
        print(k)
    except:
        pass