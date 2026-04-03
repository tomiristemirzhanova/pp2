#1. Create a generator that generates the squares of numbers up to some number N

def square(N):
    for i in range(N+1):
        yield i*i

for a in square(5):
    print(a)

#2. Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def even(n):
    for i in range(n+1):
        if i%2==0:
            yield i

n=int(input())
print(",".join(str(a) for a in even(n)))

#3. Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def divis(n):
    for i in range(n):
        if i%3==0 and i%4==0:
            yield i

n=int(input())
for a in divis(n):
    print(a)


#4. Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

def squares (a,b):
    for i in range (a,b+1):
        yield i**2

a=int(input())
b=int(input())

for i in squares (a,b+1):
    print(i)

#5. Implement a generator that returns all numbers from (n) down to 0.

def tozero(n):
    for i in range (n, -1, -1):
        yield i
        

n=int(input())
for i in tozero(n):
    print(i) 