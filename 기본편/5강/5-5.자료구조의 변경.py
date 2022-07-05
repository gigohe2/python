# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "쥬스"}
print(menu, type(menu)) #menu의 type은 set이다

menu=list(menu)
print(menu, type(menu)) #menu의 type은 lsit이다

menu = tuple(menu)
print(menu,type(menu))

menu=set(menu)
print(menu,type(menu))



