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
LONG_BREAK_MIN = 30
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer_label
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label = Label(text="Long Break", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 50))
        timer_label.grid(column=1, row=0)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label = Label(text="Short Break", fg=PINK, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 50))
        timer_label.grid(column=1, row=0)

    else:
        count_down(work_sec)
        timer_label = Label(text="Work", fg=RED, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 50))
        timer_label.grid(column=1, row=0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_btn = Button(text="START", command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="RESET", command=reset_timer)
reset_btn.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_mark.grid(column=1, row=3)


window.mainloop()

