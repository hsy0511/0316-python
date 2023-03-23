def print_kwargs(**a):
    print(a)
print_kwargs(a=1)
print_kwargs(a="hello",b="world!") # 키워드 함수로 **라는 딕셔너리 값으로 변환해준다.