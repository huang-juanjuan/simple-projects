import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

start_time = "0:0"
end_time = "23:59"
password = "123"


def set_time():
    timer = tk.Toplevel()
    timer.title("Time Setting")
    timer.geometry("400x150")

    frame = tk.Frame(timer)
    frame.pack()

    password_label = tk.Label(frame, text="Password:")
    password_label.grid(row=0, column=0)

    password_entry = tk.Entry(frame, show="*")
    password_entry.grid(row=0, column=1)

    start_label = tk.Label(frame, text="Start Time:")
    start_label.grid(row=1, column=0)

    start_hour_combobox = ttk.Combobox(frame, values=[str(i).zfill(2) for i in range(24)], width=2)
    start_hour_combobox.grid(row=1, column=1)

    start_minute_combobox = ttk.Combobox(frame, values=[str(i).zfill(2) for i in range(60)], width=2)
    start_minute_combobox.grid(row=1, column=2)

    end_label = tk.Label(frame, text="End Time:")
    end_label.grid(row=2, column=0)

    end_hour_combobox = ttk.Combobox(frame, values=[str(i).zfill(2) for i in range(24)], width=2)
    end_hour_combobox.grid(row=2, column=1)

    end_minute_combobox = ttk.Combobox(frame, values=[str(i).zfill(2) for i in range(60)], width=2)
    end_minute_combobox.grid(row=2, column=2)

    def save_time():
        global start_time, end_time
        if password_entry.get() == password:
            start_time = start_hour_combobox.get() + ":" + start_minute_combobox.get()
            end_time = end_hour_combobox.get() + ":" + end_minute_combobox.get()
            messagebox.showinfo("Time Setting", f"Start Time: {start_time}\nEnd Time: {end_time}")
            timer.destroy()
        else:
            messagebox.showerror("Invalid Password", "Incorrect password!")

    save_button = tk.Button(timer, text="Save", command=save_time)
    save_button.pack()


def get_setting():
    return {"start_time": start_time, "end_time": end_time}