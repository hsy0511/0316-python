def add_mul(a,*b):
    if a == "add":
        c = 0
        for d in b:
            c = c+d
    elif a == "mul":
        c = 1
        for d in b:
            c = c*d
    return c
a = add_mul("add",1,2,3,4,5)
print(a)

b = add_mul("mul",1,2,3,4,5) # add_mul 함수를 이용해 2개에 매개변수에 각각 다른 연산을 하게 했다.
print(b)