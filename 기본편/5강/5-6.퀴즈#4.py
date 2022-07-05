# shuffle() : 값의 순서를 무작위로 바꿔줌
# sample(variable, number) : variable에서 number개의 샘플을 무작위로 뽑음

# 댓글 작성자 중 추첨을 통해 1명 치킨, 3명 커피 쿠폰 받음
# 조건 1: 댓글은 20명 작성, 아이디는 1~20
# 조건 2: 댓글 내용과 상관없이 무작위로 추첨, 중복 불가
# 조건 3: random 모듈의 shuffle과 sample을 활용

from random import *
user=range(1,21) # 1~21미만의 숫자 생성
user=list(user) # list로 형변환

shuffle(user)
print(user)

win=sample(user, 4)


print("--당첨자 발표--")
print("치킨 당첨자: ", win[0])
print("커피 당첨자: ", win[1:])


