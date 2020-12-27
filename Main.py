import Create_Database as db
import Record_Attendance as re
import Train_Model as tr

print("#########    AUTOMATIC ATTENDANCE RECORD   #######")

while (1):
    n = int(input(
        "Select \n\n1. Train Model\n\n2. Add Student\n\n3. Record Attendance\n\n0. Exit\n\nPlease Select : "))

    if (n == 1):
        tr.get_encoded_faces()

    elif (n == 2):
        db.add_student()

    elif (n == 3):
        re.mark_attendance()

    elif (n == 0):
        break;


    else:
        print("INVALID OPTION")
