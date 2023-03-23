def add_many(*a):
    b = 0
    for c in a :
        b = b+c
    return b
a = add_many(1,2,3,4,5) # 여러개의 입력값을 받으려면 매개변수 앞에
print(a)
