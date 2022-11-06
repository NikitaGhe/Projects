from datetime import date
from datetime import datetime
import csv
import os
import mtcnn
import pandas as pd

import FRM
import cv2

import os
from glob import glob


def recognizer(test_image,subject_name):
    f = open("divisions.txt", "r")
    div = f.read()
    if div=="div1":
        directory = os.getcwd()
        persons = glob(directory+'/ATTENDANCE_SHEET/DIV1/*') # /ATTENDANCE_SHEET/+
        get_file_name = 0
        for person_name in persons:
            if person_name.split('\\')[-1] == subject_name+".csv":
                get_file_name = 1

        if get_file_name == 0:
            directory = os.getcwd()
            persons = glob(directory+'/data/*')
            fieldnames = ['Date', 'Time']
            names = []
            for person_name in persons:
                Known_names = os.path.basename(person_name)
                path = os.path.join(person_name, '*.jpeg')
                for img in glob(path):
                    print(img)
                    fieldnames.append(Known_names)
                    names.append(person_name)
            print(fieldnames)


            with open("ATTENDANCE_SHEET/DIV1/" + subject_name + '.csv', 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
            


        attendance = []
        directory = os.getcwd()
        persons = glob(directory+'/data/*')
        known_face_encodings = []
        known_face_names = []
        fieldnames = []
        fieldnames.append('Date')
        fieldnames.append('Time')

        f = open("date_time.txt", "r")
        date_time = f.read()
        present_date=date_time.split('T')[-2]
        current_time=date_time.split('T')[-1]
        print('Given Time')
        print(present_date)
        print(current_time)
        attendance.append(present_date)
        attendance.append(current_time)

        for person_name in persons:
            Known_names = os.path.basename(person_name)
            path = os.path.join(person_name, '*.jpeg')
            for img in glob(path):
                print(img)
                face_image = FRM.load_image_file(img)
                face_encoding = FRM.face_encodings(face_image)[0]
                known_face_encodings.append(face_encoding)
                known_face_names.append(Known_names)
                fieldnames.append(Known_names)
                attendance.append('A')


        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        frame = cv2.imread(test_image)

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        #detecttor=mtcnn()


        face_locations = FRM.face_locations(rgb_small_frame)
        face_encodings = FRM.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            
            matches = FRM.CNN_Mask_Face(known_face_encodings, face_encoding)
            name = "Unknown"
          
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                attendance[first_match_index+2] = 'P'
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

        print('Lecture Over')
        data2write1=zip(fieldnames,attendance)
        data2write = dict(data2write1)
        with open("ATTENDANCE_SHEET/DIV1/" + subject_name + '.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(data2write)

        os.system("start EXCEL.EXE " + "ATTENDANCE_SHEET/DIV1/" + subject_name + '.csv')
    else:
        directory = os.getcwd()
        persons = glob(directory+'/ATTENDANCE_SHEET/DIV2/*')
        get_file_name = 0
        for person_name in persons:
            if person_name.split('\\')[-1] == subject_name+".csv":
                get_file_name = 1

        if get_file_name == 0:
            directory = os.getcwd()
            persons = glob(directory+'/data/*')
            fieldnames = ['Date', 'Time']
            names = []
            for person_name in persons:
                Known_names = os.path.basename(person_name)
                path = os.path.join(person_name, '*.jpeg')
                for img in glob(path):
                    print(img)
                    fieldnames.append(Known_names)
                    names.append(Known_names)
            print(fieldnames)


            with open("ATTENDANCE_SHEET/DIV2/" + subject_name + '.csv', 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
            


        attendance = []
        directory = os.getcwd()
        persons = glob(directory+'/data/*')
        known_face_encodings = []
        known_face_names = []
        fieldnames = []
        fieldnames.append('Date')
        fieldnames.append('Time')

        f = open("date_time.txt", "r")
        date_time = f.read()
        present_date=date_time.split('T')[-2]
        current_time=date_time.split('T')[-1]
        print('Given Time')
        print(present_date)
        print(current_time)
        attendance.append(present_date)
        attendance.append(current_time)

        for person_name in persons:
            Known_names = os.path.basename(person_name)
            path = os.path.join(person_name, '*.jpeg')
            for img in glob(path):
                print(img)
                face_image = FRM.load_image_file(img)
                face_encoding = FRM.face_encodings(face_image)[0]
                known_face_encodings.append(face_encoding)
                known_face_names.append(Known_names)
                fieldnames.append(Known_names)
                attendance.append('A')

        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        frame = cv2.imread(test_image)

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        #detecttor=mtcnn()


        face_locations = FRM.face_locations(rgb_small_frame)
        face_encodings = FRM.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            
            matches = FRM.CNN_Mask_Face(known_face_encodings, face_encoding)
            name = "Unknown"
          
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                attendance[first_match_index+2] = 'P'
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

        print('Lecture Over')
        data2write1=zip(fieldnames,attendance)
        data2write = dict(data2write1)
        with open("ATTENDANCE_SHEET/DIV2/" + subject_name + '.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(data2write)

        os.system("start EXCEL.EXE " + "ATTENDANCE_SHEET/DIV2/" + subject_name + '.csv')


