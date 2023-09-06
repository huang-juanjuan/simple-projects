import tkinter as tk

import AddStudent
import TimeSetting
import ClockIn

nums = 0
time_setting = {"start_time": "0:0", "end_time": "23:59"}


def get_time_setting():
    global time_setting
    time_setting = TimeSetting.get_setting()
    return time_setting


root = tk.Tk()
root.title("武工大智慧学工人脸考勤系统")
root.geometry("400x400")

image_label = tk.Label(root)

get_feature_button = tk.Button(root, text="Add person", command=AddStudent.capture_photo_and_save)
get_feature_button.pack()

mark_attendance_button = tk.Button(root, text="Clock in", command=lambda: ClockIn.student_clock_in(root, get_time_setting()))
mark_attendance_button.pack()

mark_attendance_button = tk.Button(root, text="Setting time", command=TimeSetting.set_time)
mark_attendance_button.pack()

result_label = tk.Label(root)
result_label.pack()

root.mainloop()
