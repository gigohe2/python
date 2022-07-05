from tkinter import * # tkinter에 있는 모든 것을 가져와 쓰겠다.

root = Tk()

root.title("Jun GUI")
# root.geometry("640x480") # 가로*세로의 창 크기를 지정해줌
root.geometry("640x480+300+100") # 가로*세로+ x좌표 + y좌표를 지정해주어 x,y에 화면이 뜨게 된다.


listbox = Listbox(root, selectmode="extended", height=0) #height 0은 모든 리스트를 보여주고, 상수 n을 넣으면 n개 만큼의 리스트만 보여준다.
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박") #END로 하면 맨뒤에 넣어준다.
listbox.insert(END, "포도")
listbox.pack()


def btncmd():
    #삭제
    #listbox.delete(END) #맨 뒤에 항목이 삭제된다.
    #listbox.delete(0) #맨 앞의 항목이 삭제된다.

    #갯수 확인
    #print("리스트에는", listbox.size(), "개가 있다.")
    
    #항목 확인 (시작 idx, 끝 idx)
    #print("1번째부터 3번째까지의 항목: ", listbox.get(0,2))

    #선택된 항목의 확인(idx값 반환)
    print("선택된 항목: ", listbox.curselection()) # curselection : 현재 선택된 항목의 idx 값을 반환해준다.



btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop() #창이 닫히지 않도록 해줌