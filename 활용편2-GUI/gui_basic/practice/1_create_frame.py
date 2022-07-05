from tkinter import * # tkinter에 있는 모든 것을 가져와 쓰겠다.

root = Tk()

root.title("Jun GUI")
# root.geometry("640x480") # 가로*세로의 창 크기를 지정해줌
root.geometry("640x480+300+100") # 가로*세로+ x좌표 + y좌표를 지정해주어 x,y에 화면이 뜨게 된다.
#창 크기 고정시키기
root.resizable(False, False) # x축, y축에 대해 크기 조정을 False로 수정해줌




root.mainloop() #창이 닫히지 않도록 해줌