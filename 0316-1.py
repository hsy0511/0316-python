# 함수
def add(a, b): # def는 함수를 사용할 때 쓰는 예약어, add는 함수명, (a, b)는 매개변수 
    return a + b # 함수에서 실행되는 결과 값을 돌려주는 명령어

# 예시 
a = 1 # 변수지정
b = 2 # 변수지정
c = add(a,b) # 만든 변수 매개변수로 지정하여 add(+)함수를 사용
print(c)

def add(a, b):  # a, b는 매개변수
    return a+b

print(add(3, 4))  # 3, 4는 인수  

def add(a, b): 
    result = a + b 
    return result # 리턴 값으로 받는 코드
a = add(3,4)
print(a) # 인수값으로 호출하는 코드

def say():
    return 'Hi'

a = say()
print(a) # 입력값을 넣지 않아 리턴 값으로 출력한다.

    
print(add(1,2))

def add(a, b):
    print(a+b)
a = add(1, 2)
print(a)

def say():
    print("hi")
print(say())
