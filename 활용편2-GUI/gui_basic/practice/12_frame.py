from tkinter import * # tkinter에 있는 모든 것을 가져와 쓰겠다.

root = Tk()

root.title("Jun GUI")
# root.geometry("640x480") # 가로*세로의 창 크기를 지정해줌
root.geometry("640x480+300+100") # 가로*세로+ x좌표 + y좌표를 지정해주어 x,y에 화면이 뜨게 된다.

Label(root, text="메뉴를 선택해 주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1) 
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right",fill="both", expand=True)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()

root.mainloop() #창이 닫히지 않도록 해줌