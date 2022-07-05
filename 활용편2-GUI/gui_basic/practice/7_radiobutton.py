from tkinter import * # tkinter에 있는 모든 것을 가져와 쓰겠다.

root = Tk()

root.title("Jun GUI")
# root.geometry("640x480") # 가로*세로의 창 크기를 지정해줌
root.geometry("640x480+300+100") # 가로*세로+ x좌표 + y좌표를 지정해주어 x,y에 화면이 뜨게 된다.


Label(root, text="메뉴를 선택하세요").pack()


# 라디오버튼 : 여러개중에서 하나를 선택하는 버튼이다.
burger_var = IntVar() # 여기에 int형으로 값을 저장한다.
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)
btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()


drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink3 = Radiobutton(root, text="환타", value="환타", variable=drink_var)
btn_drink1.select()
btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()


def btncmd():
    print(burger_var.get()) # 햄버거 중 선택된 라디오 항목의 값 (value)를 반환해준다.
    print(drink_var.get()) # 음료 중 선택된 값(value)를 출력


btn = Button(root, text="주문", command=btncmd)
btn.pack()


root.mainloop() #창이 닫히지 않도록 해줌