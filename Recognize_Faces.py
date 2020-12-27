import face_recognition as fr
import cv2
import numpy as np



def classify_face(im):

    faces = np.load('J:\FaceAppTests\Automatic_Meetroom_Attendance\\training_data.npy', allow_pickle='TRUE').item()
    # print("this is detection file", faces)
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    img = cv2.imread(im)
    face_locations = fr.face_locations(img)
    unknown_face_encodings = fr.face_encodings(img, face_locations)

    face_names = []

    for face_encoding in unknown_face_encodings:
        name = "UnKnown"
        matches = fr.compare_faces(faces_encoded, face_encoding)
        face_distances = fr.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            name = ''.join([j for j in name if not j.isdigit()])

        face_names.append(name)

    # print(face_names)

    return face_names


