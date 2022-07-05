from tkinter import * # tkinter에 있는 모든 것을 가져와 쓰겠다.


root = Tk()

root.title("Jun GUI")
# root.geometry("640x480") # 가로*세로의 창 크기를 지정해줌
root.geometry("640x480+300+100") # 가로*세로+ x좌표 + y좌표를 지정해주어 x,y에 화면이 뜨게 된다.


def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New window")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit) # root.quit 은 끝내기 명령


menu.add_cascade(label="File", menu=menu_file)

#Edit 메뉴 (빈 값)
menu.add_cascade(label="Edit")

# 언어 메뉴 추가 (radio 버튼을 통해서 택 1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C")
menu.add_cascade(label="Language", menu=menu_lang)


# View 메뉴 추가
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)




root.mainloop() #창이 닫히지 않도록 해줌