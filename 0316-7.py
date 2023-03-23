def say_myself(a, b, c=True): 
    print("수면시간 %d"%a) 
    print("자유시간 %d"%b) 
    if c: 
        print("점심시간")
    else: 
        
        print("학습시간")
print(say_myself(7,12,True)) # 3번째 매개변수 값을 true로 미리 설정한 후 if문에서 True 값을 출력함.
