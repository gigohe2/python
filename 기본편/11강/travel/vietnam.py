class VietnamPackage:
    def detail(self):
        print("[베트남 패키지 3박 5일] 다낭 효도 여행 60만원")

if __name__ == "__main__": #name이 main이면
    print("vietnam 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행된다.")
    trip_to = VietnamPackage()
    trip_to.detail()
else:
    print("vietnam 외부에서 모듈 호출")