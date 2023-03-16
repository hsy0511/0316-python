# 0316-python
# 함수
## 함수 구조
```python
def add(a, b): 
    return a + b 
a = 1 
b = 2 
c = add(a,b) 
print(c)
```
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/225482261-21e0cf21-1218-4e5c-8cdc-1ab86efe9b9b.png)
def는 함수를 사용할 때 쓰는 예약어, add는 함수명, (a, b)는 매개변수이고, return은 함수에서 실행되는 결과 값을 돌려주는 명령어.
## 매개변수와 인수
```python
def add(a, b):  # a, b는 매개변수
    return a+b

print(add(3, 4))  # 3, 4는 인수
```
###### ※매개변수 : 함수에 전달된 값을 저장하는 변수(받는값)
###### ※인수 : 함수에 전달하는 값(호출값)
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/225482288-1599c515-6edf-4077-908d-aa85a5433188.png)
## 입력값이 없는 함수
```python
def say():
    return 'Hi'

a = say()
print(a)
```
입력값이 없는 함수에서는 say()에서 ()안에 아무것도 넣지 않았을 때 리턴 값을 출력한다.(입력값이 없다면 리턴값을 출력하게됨.)
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/225484912-5d75b459-9c61-4c0d-8276-528924ab73d1.png)
## 리턴값이 없는 함수
```python
print(add(1,2))
# 리턴값 확인
def add(a, b):
    print(a+b)
a = add(1, 2)
print(a)
```
리턴값이 없는 함수는 함수이름(인수,인수)로 입력값을 출력한다.(리턴값이 없는걸 확인하면 none이 출력됨)
### 결과값
![image](https://user-images.githubusercontent.com/104752580/225487024-29a27373-9e80-4f19-b0c8-df5ef34acd2e.png)
## 입력값과 리턴값이 둘 다 없는 함수
```python
def say():
    print("hi")
print(say())
```
입력값과 리턴값이 둘 다 없는 함수는 함수 이름만 출력한다.
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/225487807-7ba7f529-eea4-4dc8-84de-e356785a7b94.png)
## 매개변수 지정하여 호출하기
```pyhton
def sub(a,b):
    return a-b
a= sub(a=1,b=1)
print(a)
```
매개변수를 1,1로 지정하여 출력했다.(매개변수를 지정하면 순서에 상관없이 사용할 수 있다.)
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/225488960-803c1dd0-7181-4096-9412-7dc66a7446c0.png)
## 여러 개의 입력값을 받는 함수
```python
def add_many(*a):
    b = 0
    for c in a :
        b = b+c
    return b
a = add_many(1,2,3,4,5)
print(a)
```
매개변수 앞에 * 를 붙여서 입력값을 다 모아서 튜플로 만들어준다. add_many 함수로 입력값이 많아도 다 더할 수 있게 해준다.
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/225490707-e1022b82-0f5b-4a8e-9a6d-6aa3c0c5e2d0.png)
## 키워드 매개변수 kwargs(keyword arguments 약자)
###### ※kwargs는 함수를 호출할 때 함수의 인자에 이름을 붙여 전달할 수 있다는 뜻을 가지고있다
```python
def print_kwargs(**a):
    print(a)
print_kwargs(a=1)
print_kwargs(a="hello",b="world!")
```
매개변수 앞에 ** 를 붙여서 입력값을 딕셔너리({key:value})로 변환 시켜준다. print_kwargs 함수로 입력받은 매개변수를 출력한다.
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/225496002-205789fd-40de-407f-890a-b47c5aded3c8.png)
## 함수의 리턴 값
```python
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
print(a)
```
add_and_mul 함수로 2개의 인수를 각각 더한값과 곱한값으로 리턴하는 함수이다. 이때 출력은 튜플로된다.


여기서 변수 두개를 선언하여 함수로 튜플을 분리할 수 있다. 하지만 리턴문을 2개를 사용한다고 2개에 리턴값을 주는 것은 아니다.

즉 함수 두개의 인수는 리턴이 가능하지만 2개의 리턴값을 가질 수 없다. 
