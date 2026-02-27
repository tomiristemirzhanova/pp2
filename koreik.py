# def fun(max):
#     cnt = 1
#     while cnt <= max:
#         yield cnt
#         cnt += 1

# ctr = fun(5)
# for n in ctr:
#     print(n)


def square(N):
    a=1
    while a*a<N:
        yield a*a
        a+=1

N=int(input())
b=square(N)
for i in b:
    print(i)