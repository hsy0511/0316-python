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
```python
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
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/225513926-e2f10a66-e3e4-42ba-933c-4e04c7e07231.png)
## 매개변수 초깃값 미리설정
```python
def say_myself(a, b, c=True): 
    print("수면시간 %d"%a) 
    print("자유시간 %d"%b) 
    if c: 
        print("점심시간")
    else: 
        
        print("학습시간")
        
print(say_myself(7,12,True))
```
c 매개변수의 값을 미리 지정해주며 초깃값을 세팅했다. 초깃값을 True로 지정했기 때문에 if문은 점심시간이 출력된다.

false이라면 학습시간이 나온다. 초깃값 설정은 중간에 오지 못하고 마지막 인수에 설정해야한다.
###### ※ say_myself 함수는 3개의 매개변수 값에서 마지막 인수가 True면 if문에서 Ture값을 출력하는 함수이다.
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/225513237-f5462172-7e42-417a-b49a-91087c506873.png)
## 함수 안에서 선언한 변수의 효력 범위
```python
a = 1

def vartest(a):
    a = a + 1

vartest(3)
print(a)
```
함수 안에있는 매개변수 a는 vartest(3)을 통해서 4가 되지만 함수 밖에있는 print(a)는 1이된다. 즉 함수 안에서 선언한 변수는 함수 안에서만 사용되는것을 볼 수 있다. 
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/225516399-d208b250-2309-4ee9-ba65-a806fab5d3e7.png)
## 함수 안에서 함수 밖의 변수를 변경하는 방법
#### return을 사용하는 방법
```python
a = 1 
def vartest(a): 
    a = a +1 
    return a

a = vartest(a)
print(a)
```
vartest(a) 함수의 입력된 값을 1을 더하도록 리턴하도록 변경했다.
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/225517545-67cab045-62f3-4541-ae7e-85383bdefde6.png)
#### global 명령어 사용하는 방법
```python
a = 1 
def vartest(): 
    global a 
    a = a+1

vartest() 
print(a)
```
global 명령어로 밖의 있는 변수를 직접적으로 사용하겠다고 선언하는 것이다. 하지만 함수는 독립적으로 존재하는 것이 좋기 때문에 global 명령어 사용을 권장하지 않는다.

###### ※독립적으로 존재하는게 좋은 이유: 외부 변수에 종속적인 함수는 그다지 좋은 함수가 아니다
## lambda
```python
def add(a,b):
    return a+b
c = add(1,2)
print(c)
```
#### lambda로 변환
```python
add = lambda a, b: a+b
c = add(1,2)
print(c)
```
lambda는 def와 같이 함수를 생성할 때 사용하는 예약어로 보통 함수를 한줄로 간결하게 만들때나 def를 사용해야 할 정도로 복잡하지않고, def를 사용하지 못하는 곳에서 사용된다.

lambda로 만든 함수는 return명령어를 쓰지 않아도 리턴 값을 반환한다.
###### ※ 함수명 = lambda 매개변수로 표현한다. 
### 결과값
![image](https://user-images.githubusercontent.com/104752580/225520944-3af79e06-c8a9-4a22-a208-5c445be3061a.png)
# Quiz
```python
from random import *
a = range(1,46)
b = list(a)
c = sample(b,5)
c.sort()
def lotto(a):
    a = a
    return a
a = lotto(c)
print(a)
```
return으로 함수 안에 변수를 함수 밖에 있는 변수와 변경했다.
### 결과 값
![image](https://user-images.githubusercontent.com/104752580/225536170-ed491fd6-90f2-4be0-a49f-7e7385020a80.png)

