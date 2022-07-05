#score_file = open("score.txt", "w", encoding="utf8")
#print("수학 : 0", file=score_file)
#print("영어 : 50", file=score_file)
#score_file.close()

#score_file = open("score.txt", "a", encoding="utf8") # a는 내용 추가
#score_file.write("과학 : 80")
#score_file.write("\n코딩 : 100")
#score_file.close()

#score_file=open("score.txt", "r", encoding="utf8")
#print(score_file.read()) #모든 정보 읽어옴
#score_file.close()

# 한줄씩 읽어오기
#score_file = open("score.txt", "r", encoding="utf8")
#print(score_file.readline(), end="") # 줄별로 읽기 수행, 한 줄 읽고 커서는 다음 줄로 이동한다.
#print(score_file.readline())
#print(score_file.readline())
#print(score_file.readline())
#score_file.close()

# 임의의 파일에 대한 읽기 처리
#score_file = open("score.txt", "r", encoding="utf8")
#while True:
#    line = score_file.readline()
#    if not line:
#        break
#    print(line, end="")
#score_file.close()

# 다른 방법
score_file=open("score.txt", "r", encoding="utf8")
lines=score_file.readlines() # list 형태로 한 줄 씩 읽어서 저장한다.
for line in lines:
    print(line, end="")
score_file.close()