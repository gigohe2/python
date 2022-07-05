
for waiting_no in range(1,101):
    print("대기번호:{0}".format(waiting_no))

for i in [1,3,4]:
    print("대기번호:{0}".format(i))
    

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks: # starbucks 내에서 customer 하나씩 뽑아서 반복함
    print("{0}, 커피가 준비되었습니다.".format(customer))