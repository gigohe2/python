try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러 발생!")
except ZeroDivisionError as err:
    print(err)
except Exception as err: #위에서 적힌 오류가 아닌 나머지 모든 에러에 대한 처리해줌.
    print("알 수 없는 에러")
    print(err) #나머지 에러에 대한 에러 메세지를 출력해줌
