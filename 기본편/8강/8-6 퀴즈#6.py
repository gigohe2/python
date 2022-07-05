# 매주 1회 작성해야 하는 보고서가 있다.
# 아래는 형식이다.

# - X 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1~50주차까지의 보고서 파일을 만들어라.
# 조건 : 파일명은 '1주차.txt', '2주차.txt' 와 같이 만든다.

for i in range(1,51):
    num = str(i)
    files = open("{0}주차.txt".format(num), "w", encoding="utf8")
    print("- "+num+" 주차 주간보고 -", file=files)
    print("부서 : ", file=files)
    print("이름 : ", file=files)
    print("업무 요약 : ", file=files)
    files.close()

# for i in range(1,51):
#     with open(str(i)+"주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약 :")


