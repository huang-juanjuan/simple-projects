import os
import cv2
import csv
import dlib
import datetime
import numpy as np
import tkinter as tk
from PIL import ImageTk, Image
from imageio import imread
from tkinter import messagebox


detector = dlib.get_frontal_face_detector()
predictor_path = 'shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(predictor_path)
face_rec_model_path = 'dlib_face_recognition_resnet_model_v1.dat'
facerec = dlib.face_recognition_model_v1(face_rec_model_path)


def get_feature(path):
    img = imread(path)
    dets = detector(img)
    # 假设每张图只有一个人脸
    shape = predictor(img, dets[0])
    face_vector = facerec.compute_face_descriptor(img, shape)
    return face_vector


# 计算欧式距离
def distance(a, b):
    a, b = np.array(a), np.array(b)
    sub = np.sum((a - b) ** 2)
    add = (np.sum(a ** 2) + np.sum(b ** 2)) / 2.
    return sub / add


def student_clock_in(root, time_setting):
    # 获取当前系统时间
    current_time = datetime.datetime.now().time()

    start_time = datetime.datetime.strptime(time_setting["start_time"], "%H:%M").time()
    end_time = datetime.datetime.strptime(time_setting["end_time"], "%H:%M").time()

    if current_time < start_time or current_time > end_time:
        messagebox.showinfo("超出时间范围", "当前时间超出打卡时间范围！")
        return

    re_name = "photo.jpg"  # 要删除的文件名

    if os.path.exists(re_name):  # 检查文件是否存在
        os.remove(re_name)  # 删除文件
    else:
        pass

    cap = cv2.VideoCapture(0)

    # 读取摄像头画面
    ret, frame = cap.read()

    # 创建人脸识别器
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # 检测人脸
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 如果未识别到人脸
    if len(faces) == 0:
        print("未识别到人脸")
        cap.release()
        cv2.destroyAllWindows()
        return

    # 关闭摄像头和窗口
    cap.release()
    cv2.destroyAllWindows()

    # 保存图像为"photo.jpg"
    cv2.imwrite("photo.jpg", frame)

    data_folder = "C:\\Users\\Hty\\Desktop\\test_python\\data"  # data文件夹路径
    data_files = os.listdir(data_folder)  # 获取data文件夹中的所有文件名
    data_paths = [os.path.join(data_folder, file) for file in data_files]  # 获取data文件夹中所有文件的完整路径

    # 计算图像文件和data文件夹中的文件的特征距离
    detected = False
    path = "photo.jpg"
    img = cv2.imread(path)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    for data_path in data_paths:
        # 加载data文件夹中的图像文件并提取特征
        data_image = Image.open(data_path)

        # 计算图像文件和data文件夹中的文件的特征距离
        feature_distance = distance(get_feature(data_path), get_feature(path))
        if feature_distance <= 0.09:
            filename_with_extension = os.path.basename(data_path)
            filename, extension = os.path.splitext(filename_with_extension)
            # 输出文件名
            detected = True
            break

    if detected:
        attendance_path = "attendance.csv"
        temp_path = "temp.csv"

        with open(attendance_path, "r") as f, open(temp_path, "w", newline='') as temp:
            reader = csv.reader(f)
            writer = csv.writer(temp)
            for row in reader:
                if row[1] == filename:
                    row[2] = "已打卡"
                    filename = row[0]
                writer.writerow(row)

        # 重命名临时文件为原文件
        os.remove(attendance_path)
        os.rename(temp_path, attendance_path)

        print(f"{filename}已打卡")
    else:
        print("未检测到对应人脸")