# 출석번호가 1 2 3 4에서 101 102 103 104로 변경
students = [1,2,3,4,5]
print(students)

students = [i+100 for i in students]  #students의 하나의 원소를 뽑아 100을 더해 다시 저장하여라
print(students)


# 이름을 길이로 변환
students.clear()
students = ["아이언맨", "토르", "그루트"]
students=[len(j) for j in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)