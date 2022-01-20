def fib(n):
    curr, prev = 1, 1
    for i in range(n - 2):
        curr, prev = curr + prev, curr
    return curr
    
    
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n > 1:
#         return fib(n - 1) + fib(n - 2)

n = 2
n = 3
n = 4
print(fib(n))
