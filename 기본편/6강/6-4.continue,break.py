absent = [2, 5] # 결석
no_book = [8]
for student in range(1,11): #1~10번의 출석번호 존재
    if student in absent:
        continue #다음 분기로 이어가는 continue 문
    elif student in no_book:
        print("오늘수업 여기까지다. {0}는 교무실로 와라".format(student))
        break # 반복문 탈출
    print("{0}야 책을 읽어줘.".format(student))

