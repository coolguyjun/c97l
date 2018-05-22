score= 0
while(score >= 0 and score <=100):
    score =int(input("점수: "))
    if(score>=90 and score <=100):
        print(score,"=a")
        continue
    elif(score>=80 and score<=90):
        print(score,"=b")
        continue
    elif(score>=70 and score<=80):
        print(score,"=c")
        continue
    elif(score>=60 and score <=69):
        print(score,"=d")
        continue
    elif(score >=0 and score <=59):
        print(score,"=f")
        continue
    else:
        print("입력가능한 점수 범위는 0~100 입니다. ")
        break
    
