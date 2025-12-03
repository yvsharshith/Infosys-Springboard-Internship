# Day-1 02/12/2025

# 1. Print prime numbers from 1 to n natural numbers
# approach-1
n = int(input())
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# approach-2
m = int(input())
for num in range(2, m + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)

# 2. Find the frequency of each character in a string
# approach-1
str = input()
freq = {}

for char in str:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

for char, count in freq.items():
    print(char, ":", count)
    
# approach-2
s = input()
cct = ""
for char in s:
    if char not in cct:
        print(char, ":", s.count(char))
        cct += char
