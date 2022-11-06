import FRM
import cv2

import os
from glob import glob


def recognizer(test_image):

    directory = os.getcwd()
    persons = glob(directory+'/data/*')
    known_face_encodings = []
    known_face_names = []

    for person_name in persons:
        Known_names = os.path.basename(person_name)
        path = os.path.join(person_name, '*.jpeg')
        for img in glob(path):
            print(img)
            face_image = FRM.load_image_file(img)
            face_encoding = FRM.face_encodings(face_image)[0]
            known_face_encodings.append(face_encoding)
            known_face_names.append(Known_names)

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    frame = cv2.imread(test_image)

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
   

    face_locations = FRM.face_locations(rgb_small_frame)
    face_encodings = FRM.face_encodings(rgb_small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        
        matches = FRM.CNN_Mask_Face(known_face_encodings, face_encoding)
        name = "Unknown"
      
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        face_names.append(name)
       

    for (top, right, bottom, left), name in zip(face_locations, face_names):
      
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

       
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    frame = cv2.resize(frame,(900,600)) 
    cv2.imwrite(test_image,frame)


