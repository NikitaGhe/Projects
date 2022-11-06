import os
from glob import glob
import csv

def generate():
    directory = os.getcwd()
    persons = glob(directory+'/data/*')

    file_name = input("Enter Subject name : ")

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


    with open("ATTENDANCE_SHEET/" + file_name + '.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

    os.system("start EXCEL.EXE " + "ATTENDANCE_SHEET/" + file_name + ".csv")


generate()



