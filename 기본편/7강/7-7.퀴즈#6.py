# 표준 체중을 구하는 프로그램
# 남자 : 키 x 키 x 22
# 여자 : 키 x 키 x 21 [m^2]

# 조건 1 : 표준 체중을 별도의 함수 내에서 계산
# 함수 명 : std_weight, 전달값 : 키(height), 성별(gender)

# 조건 2: 표준 체중은 소수점 둘쨰자리까지 표시

# 출력 예제: 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender =="남자":
        return height*height*22
    else:
        return height*height*21

gender = "남자"
height=1.75
standard=round(std_weight(height, gender), 2) # round( a, b) : a 를 소숫점 b째 자리까지 표시

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(int(100*height), gender, standard))