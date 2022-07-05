# {key: value}

cabinet = {3:"유재석", 100:"김태호"}

print(cabinet[3]) # key:3인 value를 출력
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5])
print(cabinet.get(5)) #key에 value없으면 None 출력
#또는
print(cabinet.get(5,"사용가능한 key"))

# key in variable : 사용가능한 key 확인
print(3 in cabinet)
print(5 in cabinet)

cabinet={"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])

# 새 키와 밸류 받기
cabinet["A-3"] = "김종국"
cabinet["C-20"]="조세호"
print(cabinet)

# del variable[key] : 키 지우기
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 초기화
cabinet.clear()
print(cabinet)