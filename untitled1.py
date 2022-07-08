from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Heart Diagnose Report")
root.geometry("540x540")
root.configure(background = "salmon")

q1_rBtn = StringVar(value = "0")
q1 = Label(root, text = "Do you experience shortness of breath during routine activities ?", fg = "white", bg = "salmon")
q1.pack()
q1_r1 = Radiobutton(root, text = "Yes", variable = q1_rBtn, value = "Yes", bg = "salmon")
q1_r1.pack()
q1_r2 = Radiobutton(root, text = "No", variable = q1_rBtn, value = "No", bg = "salmon")
q1_r2.pack()

q2_rBtn = StringVar(value = "0")
q2 = Label(root, text = "Do you have swelling in the feet / ankles / legs (shoes feel tighter) or abdomen ?", fg = "white", bg = "salmon")
q2.pack()
q2_r1 = Radiobutton(root, text = "Yes", variable = q2_rBtn, value = "Yes", bg = "salmon")
q2_r1.pack()
q2_r2 = Radiobutton(root, text = "No", variable = q2_rBtn, value = "No", bg = "salmon")
q2_r2.pack()

q3_rBtn = StringVar(value = "0")
q3 = Label(root, text = "Do you feel any symptoms - confusion, disorientation or loss of memory ?", fg = "white", bg = "salmon")
q3.pack()
q3_r1 = Radiobutton(root, text = "Yes", variable = q3_rBtn, value = "Yes", bg = "salmon")
q3_r1.pack()
q3_r2 = Radiobutton(root, text = "No", variable = q3_rBtn, value = "No", bg = "salmon")
q3_r2.pack()

q4_rBtn = StringVar(value = "0")
q4 = Label(root, text = "Do you experience shortness of breath while at rest / lying down ?", fg = "white", bg = "salmon")
q4.pack()
q4_r1 = Radiobutton(root, text = "Yes", variable = q4_rBtn, value = "Yes", bg = "salmon")
q4_r1.pack()
q4_r2 = Radiobutton(root, text = "No", variable = q4_rBtn, value = "No", bg = "salmon")
q4_r2.pack()

q5_rBtn = StringVar(value = "0")
q5 = Label(root, text = "Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus ?", fg = "white", bg = "salmon")
q5.pack()
q5_r1 = Radiobutton(root, text = "Yes", variable = q5_rBtn, value = "Yes", bg = "salmon")
q5_r1.pack()
q5_r2 = Radiobutton(root, text = "No", variable = q5_rBtn, value = "No", bg = "salmon")
q5_r2.pack()

def hd_score():
    score = 0
    if q1_rBtn.get() == "Yes":
        score = score + 10
        print(score)
        
    if q2_rBtn.get() == "Yes":
        score = score + 10
        print(score)
        
    if q3_rBtn.get() == "Yes":
        score = score + 10
        print(score)
        
    if q4_rBtn.get() == "Yes":
        score = score + 10
        print(score)
        
    if q5_rBtn.get() == "Yes":
        score = score + 10
        print(score)
        
    if score <=10:
        messagebox.showinfo("Report", "You don't need to visit a doctor.")
        
    elif score >=10 and score  <=30:
        messagebox.showinfo("Report", "You might perhaps have to visit a doctor.")
    
    else:
        messagebox.showinfo("Report", "I strongly advise you to visit a doctor.")

btn = Button(root, text = "Show Report", command = hd_score)
btn.pack()

root.mainloop()