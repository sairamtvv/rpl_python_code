

#lst
#[-1,-2,0,-1,-2]
#0 will be output

#[1,4,2,3,5,6,7,7,1,2,4,6,3]---> output 5
# lst = [-1,-2,0,-1,-2]
lst = [1,4,2,3,5,6,7,7,1,2,4,6,3]
num_dict = {}

for num in lst:
    if num in num_dict.keys():
        num_dict[num] = num_dict[num] + 1
    else:
        num_dict[num] = 1
print(num_dict)

for key,value in num_dict.items():
    if value == 1:
        print(key)