from  timeit import default_timer

b = ["a"] * 100000
start = default_timer()
rslt = ""
for i in b:
    rslt = rslt + i
stop = default_timer()
#print(f"result is {rslt}")
loop_time = stop - start
print(f"time taken for loop is {loop_time}")

start = default_timer()
rslt_join = "".join(b)
stop = default_timer()
join_time = stop - start
# print(f"result is {rslt_join}")
print(f"time taken for join is {join_time}")

print(f"faster by {loop_time/join_time}")