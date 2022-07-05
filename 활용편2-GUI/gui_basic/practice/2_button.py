from tkinter import * # tkinter에 있는 모든 것을 가져와 쓰겠다.

root = Tk()

root.title("Jun GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()

# padx, pady는 버튼의 내용에 따라 크기를 가변적으로 변경하나, 상대적인 크기를 지정해줌
btn2 = Button(root, padx=5, pady=10, text="버튼222222222")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

#width, height 는 버튼의 상하 좌우 크기를 지정해줌
btn4 = Button(root, width=10, height=3, text="버튼4")
btn4.pack()

# fg는 글자색상, bg는 배경색상
btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

# 이미지를 통해서 버튼을 만든다.
photo = PhotoImage(file="gui_basic/img.png") #이미지의 경로를 지정해줌
btn6 = Button(root, image=photo)
btn6.pack()

# 버튼의 동작
def btncmd():
    print("버튼이 클릭되었어요")
btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop() #창이 닫히지 않도록 해줌