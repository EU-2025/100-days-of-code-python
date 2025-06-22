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

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    label_1.config(text="Timer")
    canvas.itemconfig(timer_text, text="0:00")
    label_2.config(text="")
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    count_work_sec = WORK_MIN*60
    count_short_break_sec = SHORT_BREAK_MIN*60
    count_long_break_sec = LONG_BREAK_MIN*60
    
    if reps %2==0 and reps<8:
        label_1.config(text="Break", fg=GREEN)
        count_down(count_short_break_sec)
    elif reps %2!=0 and reps<8:
        label_1.config(text="Work", fg=PINK)
        count_down(count_work_sec)
    elif reps == 8:
        label_1.config(text="Break", fg=RED)        
        count_down(count_long_break_sec)
    else:
        pass

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0"+str(count_sec)
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        if reps %2 == 0:
            multiplier= reps//2
            check_marks="✔ "*multiplier
            label_2.config(text=check_marks)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=(224), bg=YELLOW, highlightthickness=0)
pomodoro_img = PhotoImage(file= "tomato.png")
canvas.create_image(100, 112, image=pomodoro_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Label
label_1 = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
label_2 = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "normal"))
label_1.grid(column=1, row=0)
label_2.grid(column=1, row=3)

# Buttons
button_1 = Button(text="Start", highlightthickness=0, command=start_timer)
button_2 = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_1.grid(column=0, row=2)
button_2.grid(column=2, row=2)
button_1



window.mainloop()