from tkinter import *
from tkinter import messagebox
import random

# ----------------------------
#       QUIZ VARIABLES
# ----------------------------
# These variables are used to keep track of the progress, score, attempts, and selected difficulty level of the quiz.
score = 0
question_count = 0
correct_answer = 0
attempt = 1
difficulty = "easy"

# ----------------------------
#          FUNCTIONS
# ----------------------------
# These functions are used to control the flow of the quiz, generate questions, check answers, and display results.
def switch_to_frame(frame):
    frame.tkraise()

# This switches between the menu frame, quiz frame, and results frame based on the user's progress.
def display_menu():
    switch_to_frame(menu_frame)

# This randomly generates a pair of numbers based on the selected difficulty level of the quiz.
def random_int():
    if difficulty == "easy":
        return random.randint(0, 9)

    elif difficulty == "moderate":
        return random.randint(10, 99)

    else:
        return random.randint(1000, 9999)

# This randomly selects an operation between addition or subtraction.
def decide_operation():
    return random.choice(["+", "-"])

# This randomly generates the next problem, with new number pairs and operations.
def next_problem():
    global correct_answer, attempt

    attempt = 1

    num1 = random_int()
    num2 = random_int()

    operation = decide_operation()

    if operation == "+":
        correct_answer = num1 + num2
    else:
        correct_answer = num1 - num2

    question_label.config(
        text=f"{num1} {operation} {num2} = ?"
    )

    answer_entry.delete(0, END)

# This checks the correctness of the answer and the number of attempts, updating the score accordingly.
def check_answer():
    global score, question_count, attempt

    try:
        answer = float(answer_entry.get())

    except ValueError:
        messagebox.showerror(
            "Error",
            "Enter a Valid Number."
        )
        return

    if answer == correct_answer:

        if attempt == 1:
            score += 10
        else:
            score += 5

        question_count += 1

        if question_count == 10:
            display_results()
        else:
            next_problem()

    else:

        if attempt == 1:
            attempt = 2

            messagebox.showinfo(
                "Wrong Answer",
                "Try One More Time."
            )

            answer_entry.delete(0, END)

        else:

            messagebox.showinfo(
                "Wrong Answer",
                f"The Correct Answer was {correct_answer}."
            )

            question_count += 1

            if question_count == 10:
                display_results()
            else:
                next_problem()

# This calculates the score and grade of the user.
def display_results():
    global score

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "Fail.\nYou Need More Practice!"

    result_label.config(
        text=f"Score: {score}\nGrade: {grade}"
    )

    switch_to_frame(result_frame)

# This starts a new quiz following the selected difficulty level.
def start_game(level):
    global difficulty, score, question_count

    difficulty = level
    score = 0
    question_count = 0

    switch_to_frame(quiz_frame)
    next_problem()

# This returns the user to the difficulty selection menu.
def play_again():
    display_menu()

# ----------------------------
#         MAIN WINDOW
# ----------------------------
# The main window contains the title, menu frame, quiz frame, and results frame.
root = Tk()
root.title("Exercise 1: Math Quiz")
root.geometry("500x700")
root.resizable(False, False)

# ----------------------------
#         MENU FRAME
# ----------------------------
# The menu frame allows the user to choose a difficulty level before starting the quiz.
menu_frame = Frame(root, bg="white")
menu_frame.place(x=0, y=0, width=500, height=700)

menu_heading = Label(
    menu_frame,
    text="Math Quiz",
    font=("Roboto", 40),
    bg="white"
)
menu_heading.pack(pady=(120, 10))

instruction = Label(
    menu_frame,
    text="Want to Test Your Math Skills?\nPick Your Difficulty Level!",
    font=("Roboto", 16),
    bg="white"
)
instruction.pack(pady=20)

# This starts a new quiz in the easy difficulty.
easy_button = Button(
    menu_frame,
    text="Easy",
    font=('Arial', 12),
    width=22,
    command=lambda: start_game("easy")
)
easy_button.pack(ipady=8, pady=20)

# This starts a new quiz in the moderate difficulty.
moderate_button = Button(
    menu_frame,
    text="Moderate",
    font=('Arial', 12),
    width=22,
    command=lambda: start_game("moderate")
)
moderate_button.pack(ipady=8, pady=20)

# This starts a new quiz in the advanced difficulty.
advanced_button = Button(
    menu_frame,
    text="Advanced",
    font=('Arial', 12),
    width=22,
    command=lambda: start_game("advanced")
)
advanced_button.pack(ipady=8, pady=20)

# ----------------------------
#         QUIZ FRAME
# ----------------------------
# The quiz frame shows the math questions and allows the user to submit their answers.
quiz_frame = Frame(root, bg="lightblue")
quiz_frame.place(x=0, y=0, width=500, height=700)

quiz_heading = Label(
    quiz_frame,
    text="Math Quiz",
    font=("Roboto", 40),
    bg="lightblue"
)
quiz_heading.pack(pady=(140, 10))

# This shows the current math question.
question_label = Label(
    quiz_frame,
    text="Question",
    font=("Roboto", 20),
    bg="lightblue"
)
question_label.pack(pady=30)

# This allows the user to enter their answer.
answer_entry = Entry(
    quiz_frame,
    font=("Roboto", 20)
)
answer_entry.pack(pady=10)

# This submits the answer for checking.
submit_button = Button(
    quiz_frame,
    text="Submit Answer",
    font=('Arial', 12),
    width=18,
    command=check_answer
)
submit_button.pack(pady=(30, 10))

# This brings the user back to the menu.
back_button = Button(
    quiz_frame,
    text="Back to Menu",
    font=('Arial', 12),
    width=18,
    command=display_menu
)
back_button.pack(pady=10)

# ----------------------------
#        RESULTS FRAME
# ----------------------------
# The results frame shows the score and grade, before giving the user the choice to play again or exit.
result_frame = Frame(root, bg="lightgreen")
result_frame.place(x=0, y=0, width=500, height=700)

results_heading = Label(
    result_frame,
    text="Math Quiz",
    font=("Roboto", 40),
    bg="lightgreen"
)
results_heading.pack(pady=(140, 10))

# This shows the user's score and grade.
result_label = Label(
    result_frame,
    text="",
    font=("Roboto", 20),
    bg="lightgreen"
)
result_label.pack(pady=50)

# This returns the user to the menu frame upon clicking.
replay_button = Button(
    result_frame,
    text="Play Again",
    font=('Arial', 12),
    width=22,
    command=play_again
)
replay_button.pack(ipady=8, pady=10)

# This closes the application upon clicking.
quit_button = Button(
    result_frame,
    text="Quit",
    font=('Arial', 12),
    width=22,
    command=root.destroy
)
quit_button.pack(ipady=8, pady=10)

# This shows the menu frame when the application starts.
display_menu()
root.mainloop()