def add_and_mul(a,b):
    return a+b, a*b
a = add_and_mul(1,2)
print(a)

a,b=add_and_mul(1,2)
print(a,b)

def add_and_mul(a,b):
    return a+b
    return a*b
a = add_and_mul(1,2)
print(a) # 인수를 2개를 만들어 튜플로 나눌 수 있지만 리턴 값은 2개로 받지 못함