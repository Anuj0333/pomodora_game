from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
time=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(time)
    canvas.itemconfig(timer_text,text="00:00")
    timer.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps=0 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
        
    if reps%8==0:
        count_down(long_break_sec)
        timer.config(tect="Break",fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        timer.config(text="Break",fg=PINK)
    else :
        count_down(work_sec)
        timer.config(text="Work",fg=GREEN )



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec==0:
        count_sec="00"
    elif count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0: 
        global time
        time=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✓"
        check_marks.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Podomoro Counter")
window.config(padx=100,pady=50,bg=YELLOW)


timer=Label(text="TIMER",fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,"bold"))
timer.grid(column=1,row=0)

start_button=Button(text="Start",command=start_timer)
start_button.grid(row=3,column=0)

reset_button=Button(text="Reset",command=reset_timer)
reset_button.grid(row=3,column=3)

canvas=Canvas(width=200,height=224,bg=YELLOW)
tamato_img=PhotoImage(file="C:/Users/ASUS/OneDrive/Documents/anuj_work/python_mini_projects/pomodora_game/pomodoro-start/tomato.png")

canvas.create_image(102,112,image=tamato_img)
timer_text=canvas.create_text(102,130 ,text="00:00 ",fill="white",font=(FONT_NAME,25,"bold"))
canvas.grid(row=1,column=1)


check_marks=Label(fg=GREEN,bg=YELLOW)
check_marks.grid(row=3,column=1)
 










window.mainloop()