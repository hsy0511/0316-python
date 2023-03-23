a = 1 
def vartest(): 
    global a 
    a = a+1

vartest() # global 명령어는 직접적으로 밖의 있는 변수를 사용하겠다는 것이다.
print(a)