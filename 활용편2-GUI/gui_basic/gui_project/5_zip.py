kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

zip(kor, eng) # list 두개를 합쳐준다. [(사과, apple), (바나나, banana) ~~~~]

print(list(zip(kor,eng)))

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*mixed))) # unzip : zip 된 리스트를 다시 분리해준다.

kor2, eng2 = zip(*mixed) # 분리된 리스트를 각 변수에 저장한다.
print(kor2)
print(eng2)
