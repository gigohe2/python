from tkinter import *
import os

root = Tk()

root.title("제목 없음 - Windows 메모장")
root.geometry("640x480") 

filename = "mynote.txt"

def openfile(): # mynote.txt 파일을 열어서 텍스트 상자에 보여줌
    if os.path.isfile(filename): # 파일이 있으면 True
        with open(filename, "r", encoding="utf8") as file:
            text.delete("1.0", END) # 텍스트 본문 삭제
            text.insert(END, file.read()) # 파일 내용 텍스트에 띄워줌
            
    # 내가 작성한 부분
    # text.delete("1.0", END)
    # while True:
    #     line = mynote_file.readline()
    #     if not line: # 만약 끝에 도달했다면
    #         break
    #     text.insert(END, line)
    # mynote_file.close


def savefile(): # 텍스트 상자에 있는 내용을 mynote.txt에 저장함
    with open(filename, "w", encoding="utf8") as file:
        file.write(text.get("1.0", END)) # 모든 내용을 가져와서 저장

    #내가 작성한 부분
    # content = text.get("1.0", END) #처음부터 끝까지 가져옴
    # mynote_file = open("mynote.txt", "a", encoding="utf8")
    # mynote_file.write(content)
    


#메뉴 구현하기
menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=openfile)
menu_file.add_command(label="저장", command=savefile)
menu_file.add_separator() #메뉴 구분선
menu_file.add_command(label="끝내기", command=root.quit)

menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

root.config(menu=menu)


#스크롤바 만들기
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")


text = Text(root, yscrollcommand=scrollbar.set)
text.pack(side="left", fill="both", expand=True) #전체 영역으로 채우기
scrollbar.config(command=text.yview) #텍스트박스의 y값과 스크롤바의 y값을 매칭시켜준다.


root.mainloop() #창이 닫히지 않도록 해줌