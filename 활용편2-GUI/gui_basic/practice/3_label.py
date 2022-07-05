from tkinter import * # tkinter에 있는 모든 것을 가져와 쓰겠다.

root = Tk()
root.title("Jun GUI")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="또 만나요") #레이블의 변경
    global photo2 # 전역변수로 지정해주어야 함수가 끝나고 메모리 할당이 해제되지 않는다.
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)


btn = Button(root, text="클릭", command=change)
btn.pack()



root.mainloop() #창이 닫히지 않도록 해줌