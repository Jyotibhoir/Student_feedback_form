import tkinter as tk
from tkinter import messagebox, font

def submit_feedback():
    fname = entry_fname.get()
    lname = entry_lname.get()
    gender = gender_var.get()
    course = entry_course.get()
    year = entry_year.get()
    address = text_address.get("1.0", tk.END).strip()
    comments = text_comments.get("1.0", tk.END).strip()

    if not fname or not lname or not gender or not course or not year or not address:
        messagebox.showerror("Error", "Please fill in all required fields!")
        return


    result_label.config(
        text=f"----- Feedback Submitted -----\n"
             f"First Name: {fname}\n"
             f"Last Name: {lname}\n"
             f"Gender: {gender}\n"
             f"Course: {course}\n"
             f"Year: {year}\n"
             f"Address: {address}\n"
             f"Comments: {comments}"
    )

window = tk.Tk()
window.title("Student Feedback Form")
window.geometry("500x700")
window.configure(bg="#d0e6f5")  

calibri_font = font.Font(family="Calibri", size=12)

title_label = tk.Label(window, text="Student Feedback Form", font=("Calibri", 18, "bold"), bg="#d0e6f5", fg="#003366")
title_label.pack(pady=10)

form_frame = tk.Frame(window, bg="#d0e6f5")
form_frame.pack(pady=10)


tk.Label(form_frame, text="First Name:", font=calibri_font, bg="#d0e6f5").grid(row=0, column=0, sticky="w", pady=5)
entry_fname = tk.Entry(form_frame, width=30, font=calibri_font)
entry_fname.grid(row=0, column=1, pady=5)

#
tk.Label(form_frame, text="Last Name:", font=calibri_font, bg="#d0e6f5").grid(row=1, column=0, sticky="w", pady=5)
entry_lname = tk.Entry(form_frame, width=30, font=calibri_font)
entry_lname.grid(row=1, column=1, pady=5)

# Gender
tk.Label(form_frame, text="Gender:", font=calibri_font, bg="#d0e6f5").grid(row=2, column=0, sticky="w", pady=5)
gender_var = tk.StringVar()
tk.Radiobutton(form_frame, text="Male", variable=gender_var, value="Male", font=calibri_font, bg="#d0e6f5").grid(row=2, column=1, sticky="w")
tk.Radiobutton(form_frame, text="Female", variable=gender_var, value="Female", font=calibri_font, bg="#d0e6f5").grid(row=2, column=1, sticky="e")


tk.Label(form_frame, text="Course:", font=calibri_font, bg="#d0e6f5").grid(row=3, column=0, sticky="w", pady=5)
entry_course = tk.Entry(form_frame, width=30, font=calibri_font)
entry_course.grid(row=3, column=1, pady=5)

# Year
tk.Label(form_frame, text="Year:", font=calibri_font, bg="#d0e6f5").grid(row=4, column=0, sticky="w", pady=5)
entry_year = tk.Entry(form_frame, width=30, font=calibri_font)
entry_year.grid(row=4, column=1, pady=5)

# Address
tk.Label(form_frame, text="Address:", font=calibri_font, bg="#d0e6f5").grid(row=5, column=0, sticky="nw", pady=5)
text_address = tk.Text(form_frame, width=30, height=3, font=calibri_font)
text_address.grid(row=5, column=1, pady=5)

# Comments
tk.Label(form_frame, text="Comments:", font=calibri_font, bg="#d0e6f5").grid(row=6, column=0, sticky="nw", pady=5)
text_comments = tk.Text(form_frame, width=30, height=5, font=calibri_font)
text_comments.grid(row=6, column=1, pady=5)

# Submit button
submit_btn = tk.Button(window, text="Submit Feedback", command=submit_feedback, font=("Calibri", 14, "bold"), bg="#4CAF50", fg="white", width=20)
submit_btn.pack(pady=15)

# Result display area
result_label = tk.Label(window, text="", justify="left", bg="white", anchor="w", font=calibri_font, relief="solid", padx=10, pady=10)
result_label.pack(pady=10, fill="x", padx=20)

window.mainloop()