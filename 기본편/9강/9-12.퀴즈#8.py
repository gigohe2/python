#부동산 프로그램 작성
# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location=location
        self.house_type=house_type
        self.deal_type=deal_type
        self.price=price
        self.completion_year=completion_year
    
    def show_detail(self):
        print("{0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))


houses = [] #list 형식으로 만들기
h1=House("강남", "아파트", "매매", "10억", "2010년")
h2=House("마포", "오피스텔", "전세", "5억", "2007년")
h3=House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(h1)
houses.append(h2)
houses.append(h3) #리스트 형식에 h1~h3 를 넣어 반복문을 통해 관리한다.



print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for h in houses:
    h.show_detail() #총 3대의 매물의 정보 출력
