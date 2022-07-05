from tkinter import * # tkinter에 있는 모든 것을 가져와 쓰겠다.

root = Tk()

root.title("Jun GUI")
# root.geometry("640x480") # 가로*세로의 창 크기를 지정해줌
root.geometry("640x480+300+100") # 가로*세로+ x좌표 + y좌표를 지정해주어 x,y에 화면이 뜨게 된다.

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set) # set이 없으면 스크롤을 내려도 다시 올라온다.
for i in range(1,32):
    listbox.insert(END, str(i)+"일") # 1일, 2일 ...


listbox.pack(side="left")

scrollbar.config(command=listbox.yview) # 리스트박스의 y값과 스크롤 바의 y값이 서로 매칭이 된다.
root.mainloop() #창이 닫히지 않도록 해줌