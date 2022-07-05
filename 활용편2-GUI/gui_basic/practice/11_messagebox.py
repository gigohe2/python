from tkinter import * # tkinter에 있는 모든 것을 가져와 쓰겠다.
import tkinter.messagebox as msgbox

root = Tk()

root.title("Jun GUI")
# root.geometry("640x480") # 가로*세로의 창 크기를 지정해줌
root.geometry("640x480+300+100") # 가로*세로+ x좌표 + y좌표를 지정해주어 x,y에 화면이 뜨게 된다.

# 기차 예매 시스템
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.") # 메세지 박스 띄우기

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

def err():
    msgbox.showerror("에러", "결제 오류가 발생했습니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

def retrycancel():
    response = msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다.")
    if response == 1:
        print("재시도")
    elif response == 0:
        print("취소")

def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다. \n 저장 후 프로그램을 종료하시겠습니까?")
    # 네 : 저장 후 종료 TRUE 1, 아니오 : 저장하지 않고 종료 FALSE 0  , 취소 : 프로그램 종료 취소 NONE 그 외 ( 계속 작업 )
    if response == 1:
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=err, text="에러").pack()

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop() #창이 닫히지 않도록 해줌