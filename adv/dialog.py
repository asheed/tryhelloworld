# 대화상자 모듈
import tkinter.messagebox as mb

ans = mb.askyesno("질문", "라면을 좋아합니까?")
if ans == True:
    # OK 버튼만 있는 대화상자 표시
    mb.showinfo("동의", "저도 좋아합니다.")
else:
    mb.showinfo("정말로요?", "설마 라면을 싫어하는 사람이 있을줄이야!")