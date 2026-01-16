'''
13-01-2026 Task: sum of array elements

a = [1,2,3,4,5]
sum = 0
for i in a:
    sum += i
    print(f"At iteration {i} point sum is ", sum)
print(f"Total sum:", sum)

b = 123
result = sum(int(d) for d in str(b))
print("Sum:",result)

'''
# 14-01-26 Task: factorial of a number and prime number 

# def is_prime(n):
    
#     if n<2:
#         return False
    
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#     return True

# n = int(input())
# if is_prime(n):
#     print("it is a prime number")
# else:
#     print("not a prime number")
    
def fact(num):
    result = 1

    for i in range(1, num+1):
        result *= i
    return result

num = int(input())
print("Factorial of the number: ", fact(num))