python = "Python is Amazing"

# lower() : 소문자로
print(python.lower())

# upper() : 대문자로
print(python.upper())

# isupper() : 대문자이면 True
print(python[0].isupper())

# len() :  문자열 길이 반환
print(len(python))

# .repace("A", "B") : 문자열 A를 B로 바꿔줌
print(python.replace("Python", "Java"))


# index() : 몇번째 인덱스에 위치하는지 반환
index = python.index("n")
print(index)

index=python.index("n", index+1) #두번째 n을 찾음
print(index)

# find() : 문자가 있는가?
print(python.find("n"))
print(python.find("Java")) #문자가 없으면 -1 반환

# count() : 문자가 몇번 등장하는가?
print(python.count("n"))