'''def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")  # end=" " : 프린트 끝나고 줄바꿈하지않고 스페이스 하나로 종료
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "python", "java", "c", "c++", "c#")
profile("김태호", 25, "kotlin", "swifft", "","","")'''

def profile(name, age, *language): # *로 시작하는 가변인자 사용가능
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석" , 20, "python", "java", "c", "c++", "c#", "script")