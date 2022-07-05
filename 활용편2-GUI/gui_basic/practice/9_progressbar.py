from tkinter import * # tkinter에 있는 모든 것을 가져와 쓰겠다.
import tkinter.ttk as ttk
import time

root = Tk()

root.title("Jun GUI")
# root.geometry("640x480") # 가로*세로의 창 크기를 지정해줌
root.geometry("640x480+300+100") # 가로*세로+ x좌표 + y좌표를 지정해주어 x,y에 화면이 뜨게 된다.

#progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # indeterminate : 언제끝날지 모르는 작업에 대한 프로그레스 바
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # determinate : 처음부터 꾸준히 채워지는 모드
# progressbar.start(10) # 10ms 마다 움직임
# progressbar.pack()



# def btncmd():
#     progressbar.stop()


# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar() # 실수값으로 변하는 %값에 대한 처리
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): #1~100 까지
        time.sleep(0.01) #0.01초 대기
        p_var2.set(i) # progress bar 의 값 설정
        progressbar2.update() # 매번 실행마다 GUI에 반영시켜준다.
        print(p_var2.get())


btn = Button(root, text="시작", command=btncmd2)
btn.pack()


root.mainloop() #창이 닫히지 않도록 해줌