import os
import pyautogui
import datetime
import time
import xlsxwriter
import Recognize_Faces as re

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


def mark_attendance():
    print("#### THE ATTENDANCE RECORDING STARTED YOU CAN RESUME TO MEETING ####")
    path = "J:\FaceAppTests\Automatic_Meetroom_Attendance"
    meeting_name = input("Enter Meeting name : ")

    if not os.path.exists('Screenshots'):

        workbook_name = meeting_name + ".xlsx"
        os.makedirs(meeting_name)
        path = os.path.join(path, meeting_name)
        path_attendance = path
        os.chdir(path)
        meeting_time = int(input("Enter the meeting time in minutes : "))

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
                worksheet.write(row, column, "Present")
            else:
                worksheet.write(row, column, "Absent", absent_format)
            row = row + 1

        workbook.close()

    else:
        printf("MEETING NAME ALREADY EXSISTS!!!!")
