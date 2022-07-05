import sys
print("Python", "Java", file=sys.stdout) 

print("Python", "Java", "Javascript", sep=" vs ")
print("Python", "Java", sep=" vs ", end="?")
print(

)

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")


# 은행 대기순번표
# 001, 002, 003, ....

for num in range(1, 21):
    print("대기번호 :" + str(num).rjust(2))
    print("대기번호 :"+ str(num).zfill(3)) #값이 없는 빈 공간에는 0으로 채워준다.


# 표준입력
answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) #사용자를 통해 입력받은 값은 str(문자열)형식으로 저장된다.
print("입력하신 값은 "+answer+"입니다.")
