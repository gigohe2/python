# 구글에 : list of python modules 검색

# glob : 경로 내의 폴더 / 파일 목록 조회
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일에 대해 실행

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리를 표시한다.

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 디렉토리에 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir()) # 현재 디렉토리에 존재하는 폴더 표시

# time : 시간 관련 함수
# import time
# print(time.localtime()) # 현재 시간 표시
# print(time.strftime("%Y-%m-%d %H:%M:%S")) # 시간 표현 형식

# date time 
import datetime
print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격을 알려주는 외장 함수
today = datetime.date.today() #오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today+td) #오늘부터 100일 후를 나타낼 수 있다.
