# Automatic_Meetroom_Attendanceimport os
import cv2


def add_student():

    path = "D:\FaceAppTests\Automatic_Meetroom_Attendance\Faces"
    os.chdir(path)
    name = input("Enter name of student : ")

    if not os.path.exists(name):

        os.makedirs(name)
        os.chdir(os.path.join(path, name))
        cpt = 0
        vidStream = cv2.VideoCapture(0)

        while True:
            path_new = os.path.join(path, name, "image%04i.jpg" % cpt)
            print(path_new)
            ret, frame = vidStream.read()
            cv2.imshow("test window", frame)
            cv2.imwrite(path_new, frame)
            cpt += 1

            if cpt > 20:
                break

    else:
        print("Enter Correct Roll Number ")

import os
import cv2


def add_student():

    path = "D:\FaceAppTests\Automatic_Meetroom_Attendance\Faces"
    os.chdir(path)
    name = input("Enter name of student : ")

    if not os.path.exists(name):

        os.makedirs(name)
        os.chdir(os.path.join(path, name))
        cpt = 0
        vidStream = cv2.VideoCapture(0)

        while True:
            path_new = os.path.join(path, name, "image%04i.jpg" % cpt)
            print(path_new)
            ret, frame = vidStream.read()
            cv2.imshow("test window", frame)
            cv2.imwrite(path_new, frame)
            cpt += 1

            if cpt > 20:
                break

    else:
        print("Enter Correct Roll Number ")
