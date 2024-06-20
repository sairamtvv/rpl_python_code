#ncr
#user input
n = 5
r = 3

#n! /(n-r)! (r!)


def factorial(n):
    prod = 1
    for i in range(1, n + 1):
        prod = prod * i
    factorial = prod
    #print(factorial)
    return factorial

# print(f"factorial of 10 is {factorial(10)}")
ncr = factorial(n)/(factorial(n-r)*factorial(r))
print(f"ncr = {ncr}")




# prod=1
# for i in range(1, n-r+1):
#     prod = prod * i
#
# nminusrfactorial = prod
# print(nminusrfactorial)
#
#
# prod=1
# for i in range(1, r+1):
#     prod = prod * i
#
# rfactorial = prod
# print(rfactorial)
#
# ncr = nfactorial/(nminusrfactorial*rfactorial)
# print(f"ncr = {ncr}")