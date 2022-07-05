from tkinter import * # tkinter에 있는 모든 것을 가져와 쓰겠다.

root = Tk()

root.title("Jun GUI")
# root.geometry("640x480") # 가로*세로의 창 크기를 지정해줌
root.geometry("640x480+300+100") # 가로*세로+ x좌표 + y좌표를 지정해주어 x,y에 화면이 뜨게 된다.


# 텍스트 상자(글자 상자) 만들기
txt = Text(root, width=30, height=5)
txt.pack()

#미리 글자를 써놓기
txt.insert(END, "글자를 입력하세요:")


# 엔트리 상자 만들기 -> 엔터 입력 불가능, 한줄 입력 받을 때 사용
e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요:")


# 버튼을 클릭했을 때 텍스트의 수정
def btncmd():
    #내용 출력
    print(txt.get("1.0", END)) # txt에 있는 1.0(1행 0열)부터 END(끝)까지 내용을 가져와라
    print(e.get())

    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop() #창이 닫히지 않도록 해줌