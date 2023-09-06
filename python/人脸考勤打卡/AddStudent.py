import cv2
import os
import csv
import tkinter as tk
from tkinter import messagebox

password = "123"


def capture_photo_and_save():
    # 创建新的顶层窗口
    mission = tk.Toplevel()
    mission.title("Input Passwords")
    mission.geometry("400x100")

    # 创建一个新的框架放在窗口中
    frame = tk.Frame(mission)
    frame.pack()

    password_label = tk.Label(frame, text="Password:")
    password_label.grid(row=0, column=0)

    password_entry = tk.Entry(frame, show="*")
    password_entry.grid(row=0, column=1)

    def add_student():
        # 创建data文件夹（如果不存在）
        if not os.path.exists("data"):
            os.makedirs("data")

        # 打开摄像头
        cap = cv2.VideoCapture(0)

        # 读取摄像头画面
        ret, frame = cap.read()

        # 创建人脸识别器
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        # 检测人脸
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # 显示摄像头画面
        cv2.imshow("Capture Photo", frame)

        # 等待按下键盘上的任意键
        cv2.waitKey(0)

        # 如果未识别到人脸
        if len(faces) == 0:
            print("未识别到人脸")
            cap.release()
            cv2.destroyAllWindows()
            return

        # 获取存入文件夹的相关信息
        data_folder = "C:\\Users\\Hty\\Desktop\\test_python\\data"
        data_files = os.listdir(data_folder)
        file_count = len(data_files)

        name = input("请输入姓名：")
        photo_path = os.path.join(data_folder, f"{file_count}.jpg")
        cv2.imwrite(photo_path, frame)

        attendance_path = os.path.join("attendance.csv")
        with open(attendance_path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([name, file_count, "未打卡"])

        print(f"已保存{name}.jpg到data文件夹中")

        # 关闭摄像头和窗口
        cap.release()
        cv2.destroyAllWindows()

    def check_password():
        if password_entry.get() == password:
            mission.destroy()
            add_student()
        else:
            messagebox.showerror("Invalid Password", "Incorrect password!")

    ensure_button = tk.Button(mission, text="确定", command=check_password)
    ensure_button.pack()