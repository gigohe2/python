from tkinter import * # tkinter에 있는 모든 것을 가져와 쓰겠다.

root = Tk()

root.title("Jun GUI")
# root.geometry("640x480") # 가로*세로의 창 크기를 지정해줌
root.geometry("640x480+300+100") # 가로*세로+ x좌표 + y좌표를 지정해주어 x,y에 화면이 뜨게 된다.

# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")
# # btn1.pack(side="left")
# # btn2.pack(side="right")

# # 그리드 : 좌표를 지정해주어 그곳에 나타냄
# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)


# 숫자패드 만들기

#맨 윗줄
btn_f16 = Button(root, text="F16", width=5, height=2) # padx, pady -> 늘리기
btn_f17 = Button(root, text="F17",width=5, height=2)  # width, height -> 지정된 크기로 버튼 만들기
btn_f18 = Button(root, text="F18",width=5, height=2)
btn_f19 = Button(root, text="F19",width=5, height=2)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3) # sticky : 지정한 방향으로 버튼을 늘려라.
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3) # grid 기준의 padx, pady -> 
btn_f18.grid(row=0, column=2,sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

#두번째 줄
btn_clear = Button(root, text="clear",width=5, height=2)
btn_equal = Button(root, text="=",width=5, height=2)
btn_div = Button(root, text="/",width=5, height=2)
btn_mul = Button(root, text="*",width=5, height=2)

btn_clear.grid(row=1, column=0,sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1, column=1,sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2,sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1, column=3,sticky=N+E+W+S, padx=3, pady=3)

# 세번재 줄
btn_7 = Button(root, text="7",width=5, height=2)
btn_8 = Button(root, text="8",width=5, height=2)
btn_9 = Button(root, text="9",width=5, height=2)
btn_sub = Button(root, text="-",width=5, height=2)

btn_7.grid(row=2, column=0,sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1,sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2, column=2,sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2, column=3,sticky=N+E+W+S, padx=3, pady=3)

# 네번째 줄
btn_4 = Button(root, text="4",width=5, height=2)
btn_5 = Button(root, text="5",width=5, height=2)
btn_6 = Button(root, text="6",width=5, height=2)
btn_add = Button(root, text="+",width=5, height=2)

btn_4.grid(row=3, column=0,sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3, column=1,sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3, column=2,sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=3, column=3,sticky=N+E+W+S, padx=3, pady=3)

# 다섯번재 줄
btn_1 = Button(root, text="1",width=5, height=2)
btn_2 = Button(root, text="2",width=5, height=2)
btn_3 = Button(root, text="3",width=5, height=2)
btn_enter = Button(root, text="enter",width=5, height=2)

btn_1.grid(row=4, column=0,sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1,sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2,sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2,sticky=N+E+W+S, padx=3, pady=3) # rowspan : 현재 위치로부터 아래쪽으로 2칸을 합침

# 마지막 출
btn_0 = Button(root, text="0",width=5, height=2) # 가로로 2칸 합쳐짐
btn_point = Button(root, text=".",width=5, height=2)

btn_0.grid(row=5, column=0, columnspan=2,sticky=N+E+W+S, padx=3, pady=3) # 현재 위치로부터 오른쪽으로 2칸을 합침
btn_point.grid(row=5, column=2,sticky=N+E+W+S, padx=3, pady=3)
# sticky : N E W S (동서남북)으로 버튼의 그래픽을 늘려준다.

root.mainloop() #창이 닫히지 않도록 해줌