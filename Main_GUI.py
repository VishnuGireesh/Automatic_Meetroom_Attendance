from tkinter import *
import time
import pyautogui
import datetime
import xlsxwriter
import Recognize_faces as re
import os
import face_recognition as fr
import numpy as np

root = Tk()
root.title("Automatic MeetRoom Attendance")
root.geometry("800x800")


def get_encoded_faces():
    encoded = {}

    for dirpath, dname, fname in os.walk("J:\FaceAppTests\GUI Meetroom_Attendance\Faces"):
        for f in fname:
            i = 1
            if f.endswith(".jpg") or f.endswith(".png"):
                loc = os.path.join(dirpath, f)
                face = fr.load_image_file(loc)
                array = loc.split("\\")

                if array[-2] in encoded.keys():
                    array[-2] = array[-2] + str(i)
                    i = i + 1

                encoding = fr.face_encodings(face)[0]
                encoded[array[-2]] = encoding

                os.chdir("J:\FaceAppTests\GUI Meetroom_Attendance")
                np.save("training_data.npy", encoded)

    print("##........TRAINING COMPLETED...........##")
    training_completed_model = Label(train_frame, text="Training Completed", font="arial 25", anchor="center")
    training_completed_model.grid(row=2, column=0, columnspan=2, pady=10)


def train_model():
    hide_menu_frames()
    train_frame.grid()
    main_label = Label(train_frame, text="TRAINING MODEL", font=("helvectica", 32))
    main_label.grid(row=0, column=0, columnspan=2, pady=20, padx=20)
    training_button = Button(train_frame, text="START TRAINING", command=get_encoded_faces)
    training_button.grid(row=1, column=0, columnspan=2, pady=15)


def recording_attendance(name, times):
    stud_list = {1: "Abhijith",
                 2: " ",
                 3: "Ajmi",
                 4: "Anagha",
                 5: "Anuja",
                 6: "anusree",
                 7: "ashly",
                 8: "Dayal Dev",
                 9: "Fathima",
                 10: " ",
                 11: "Haritha",
                 12: "Harsha",
                 13: "joseph",
                 14: "Lekshmi",
                 15: "Mubeena A",
                 16: "Nandu",
                 17: "Preethi P S",
                 18: "Rahul Ramakrishnan",
                 19: "Rajeesh Raj",
                 20: "Revathy U",
                 21: "riya",
                 22: "Sana Earnest",
                 23: "saniya Thahseen M",
                 24: "Sariga",
                 25: "Saritha H",
                 26: "Shefna",
                 27: "Shifin",
                 28: "Soumya",
                 29: "Sreelakshmi",
                 30: "sulthan",
                 31: "Vishnu",
                 32: "Vivek",
                 33: " ",
                 34: "Anjali R",
                 35: "manijima mohan",
                 36: " ",
                 37: " ",
                 38: "Harilekshmi",
                 39: "Aswathy",
                 40: "Anandu",
                 41: "Amal",
                 42: "Gouri",
                 43: "Anjali Venugopal",
                 44: "Rehna",
                 45: "Jincy",
                 46: "Gopika",
                 47: "Shahitha"}
    path = "J:\FaceAppTests\GUI Meetroom_Attendance"
    meeting_name = name

    if not os.path.exists('Screenshots'):

        workbook_name = meeting_name + ".xlsx"
        os.makedirs(meeting_name)
        path = os.path.join(path, meeting_name)
        path_attendance = path
        os.chdir(path)
        meeting_time = times

        os.makedirs('Screenshots')
        new = path + "\Screenshots"
        os.chdir(new)
        i = 0
        found = []
        endTime = datetime.datetime.now() + datetime.timedelta(minutes=meeting_time)
        while True:
            if datetime.datetime.now() >= endTime:
                break
            # print("da mwome")
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save("screen{}.jpg".format(i))
            path = new + "\screen{}.jpg".format(i)
            # print(path)
            founded = re.classify_face(path)
            # print(founded)

            for names in founded:
                if names not in found:
                    found.append(names)

            i += 1
            time.sleep(30)

        os.chdir(path_attendance)
        workbook = xlsxwriter.Workbook(workbook_name)
        worksheet = workbook.add_worksheet()

        absent_format = workbook.add_format({'bold': True, 'font_color': 'red'})
        present_format = workbook.add_format({'bold': True, 'font_color': 'blue'})

        worksheet.write('A1', 'Roll No')
        worksheet.write('B1', 'Student Name')
        worksheet.write('C1', 'Attendance Status')

        row = 1

        for key, value in stud_list.items():
            column = 0
            worksheet.write(row, column, key)
            column = column + 1
            worksheet.write(row, column, value)
            column = column + 1
            if value in found:
                worksheet.write(row, column, "Present", present_format)
            else:
                worksheet.write(row, column, "Absent", absent_format)
            row = row + 1

        workbook.close()

    else:
        print("MEETING NAME ALREADY EXSISTS!!!!")


def mark_attendance(name, times):
    hide_menu_frames()
    countdown_frame.grid()
    # print(name, times)
    main_label = Label(countdown_frame, text="Recording " + name + " Meeting", font=("helvectica", 40), anchor="center")
    main_label.grid(row=0, column=0, columnspan=3, padx=15)
    times = int(times)
    recording_attendance(name, times)


def home():
    hide_menu_frames()
    home_frame.grid()
    main_label = Label(home_frame, text="MEETROOM ATTENDANCE", font=("helvectica", 32))
    main_label.grid(row=0, column=0, columnspan=2, pady=20, padx=15)
    meet_name_label = Label(home_frame, text="Meeting Name :")
    meet_name_label.grid(row=1, column=0, pady=50)
    meet_name = Entry(home_frame)
    meet_name.grid(row=1, column=1, pady=50)
    meet_time_label = Label(home_frame, text="Meeting Duration(in Minutes) :")
    meet_time_label.grid(row=2, column=0, pady=15)
    meet_time = Entry(home_frame)
    meet_time.grid(row=2, column=1)

    start_button = Button(home_frame, text="START RECORDING",
                          command=lambda: mark_attendance(meet_name.get(), meet_time.get()))
    start_button.grid(row=3, column=0, columnspan=2, pady=20)


def hide_menu_frames():
    home_frame.grid_forget()
    countdown_frame.grid_forget()
    train_frame.grid_forget()


# defining Main Menu

my_menu = Menu(root)
root.config(menu=my_menu)

# Adding Menu Items

home_menu = Menu(my_menu)
my_menu.add_cascade(label="Home", menu=home_menu)
home_menu.add_command(label="Home", command=home)
home_menu.add_command(label="Train", command=train_model)

# Creating Frames

home_frame = Frame(root, width=800, height=800)
countdown_frame = Frame(root, width=800, height=800)
train_frame = Frame(root, width=800, height=800)

root.mainloop()
