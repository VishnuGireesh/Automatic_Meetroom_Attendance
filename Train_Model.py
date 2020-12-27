import numpy as np
import os
import face_recognition as fr


def get_encoded_faces():

    encoded = {}

    for dirpath, dname, fname in os.walk("J:\FaceAppTests\Automatic_Meetroom_Attendance\Faces"):
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

                os.chdir("J:\FaceAppTests\Automatic_Meetroom_Attendance")
                np.save("training_data.npy", encoded)

    print("##........TRAINING COMPLETED...........##")
