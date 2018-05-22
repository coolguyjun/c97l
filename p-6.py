engkor_dict={}
eng=""
kor=""
while True:
    eng=str(input("영어 단어: "))
    kor =str(input("한글 단어 :"))
    engkor_dict[eng]=kor
    if eng=="" and kor =="":
        del engkor_dict[kor]
        prin(engkor_dict)
        break
    
