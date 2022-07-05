from tkinter import * # tkinter에 있는 모든 것을 가져와 쓰겠다.
import tkinter.ttk as ttk

root = Tk()

root.title("Jun GUI")
# root.geometry("640x480") # 가로*세로의 창 크기를 지정해줌
root.geometry("640x480+300+100") # 가로*세로+ x좌표 + y좌표를 지정해주어 x,y에 화면이 뜨게 된다.

values=[str(i) + "일" for i in range(1,32)] # 1~31까지의 숫자 + 일
combobox= ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") #최초 목록 제목 설정


readonly_combobox= ttk.Combobox(root, height=10, values=values, state="readonly") #읽기 전용 콤보박스, 에러 발생 막기 위함
readonly_combobox.pack()
readonly_combobox.current(1) # 1번째 인덱스 값 선택
readonly_combobox.set("카드 결제일") #최초 목록 제목 설정




def btncmd():
    print(combobox.get()) # 선택된 값 표시


btn = Button(root, text="선택", command=btncmd)
btn.pack()


root.mainloop() #창이 닫히지 않도록 해줌