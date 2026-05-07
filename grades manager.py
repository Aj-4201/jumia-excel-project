import pandas as pd
import numpy as np
import os
import csv

import csv

class grade_manager:
    def __init__(self, first_name, last_name, subject, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.subject = subject
        self.grade = grade

    def read_studentinfo(self):
        rows = []
        with open('student_info.csv', 'r', newline='') as soma:
            reader = csv.reader(soma)
            for row in reader:
                rows.append(row)
        return rows                          # ← moved outside the with block

    def save_studentinfo(self):
        with open('student_info.csv', 'a', newline='') as soma:
            writer = csv.writer(soma)
            writer.writerow([self.first_name, self.last_name, self.points, self.grade])

    def students_subjects(self):             # ← 4 spaces indent
        Math      = int(input('Enter Math grade: '))
        science   = int(input('Enter Science grade: '))
        english   = int(input('Enter English grade: '))
        history   = int(input('Enter History grade: '))
        kiswahili = int(input('Enter Kiswahili grade: '))
        average   = (Math + science + english + history + kiswahili) / 5
        marks     = ((Math + science + english + history + kiswahili) * 100) / 500
        self.points = self.students_grades(marks)
        self.grade  = marks
        print(f"{self.first_name} {self.last_name}'s marks: {marks}%  average: {average}  points: {self.points}")

    def students_grades(self, marks):        # ← also 4 spaces indent, NOT inside students_subjects
        if marks >= 82:
            return "A"
        elif marks >= 65:
            return "B"
        elif marks >= 50:
            return "C"
        elif marks >= 35:
            return "D"
        else:
            return "F"

    def add_studentinfo(self):
        self.first_name = input("Enter student's first name: ")
        self.last_name  = input("Enter student's last name: ")
        self.subject    = input("Enter subject: ")
        self.students_subjects()
        self.save_studentinfo()

    def retrieve_studentinfo(self):
        first_name = input("Enter student's first name: ")
        last_name  = input("Enter student's last name: ")
        rows  = self.read_studentinfo()
        match = [r for r in rows if r[0] == first_name and r[1] == last_name]
        if match:
            for row in match:
                print(f"Name: {row[0]} {row[1]} | Points: {row[2]} | Grade: {row[3]}")
        else:
            print("Student not found.")

    def update_studentinfo(self):
        first_name = input("Enter student's first name: ")
        last_name  = input("Enter student's last name: ")
        rows       = self.read_studentinfo()
        found      = any(r[0] == first_name and r[1] == last_name for r in rows)
        if not found:
            print("Student not found.")
            return
        new_rows = [r for r in rows if not (r[0] == first_name and r[1] == last_name)]
        self.first_name = first_name
        self.last_name  = last_name
        self.subject    = input("Enter subject: ")
        self.students_subjects()
        new_rows.append([self.first_name, self.last_name, self.points, self.grade])
        with open('student_info.csv', 'w', newline='') as soma:
            csv.writer(soma).writerows(new_rows)
        print(f"{first_name} {last_name}'s information updated.")

    def delete_studentinfo(self):
        first_name = input("Enter student's first name: ")
        last_name  = input("Enter student's last name: ")
        rows     = self.read_studentinfo()
        new_rows = [r for r in rows if not (r[0] == first_name and r[1] == last_name)]
        if len(new_rows) == len(rows):
            print("Student not found.")
        else:
            with open('student_info.csv', 'w', newline='') as soma:
                csv.writer(soma).writerows(new_rows)
            print(f"{first_name} {last_name}'s information has been deleted.")

    def display_allstudentinfo(self):
        rows = self.read_studentinfo()
        if not rows:
            print("No students to display.")
            return
        for i, row in enumerate(rows, 1):
            print(f"{i}. Name: {row[0]} {row[1]} | Points: {row[2]} | Grade: {row[3]}")

    def main_menu(self):
        while True:
            print("\nEnter your choice:")
            print("1. Add student information")
            print("2. Retrieve student information")
            print("3. Update student information")
            print("4. Delete student information")
            print("5. Display all student information")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_studentinfo()
            elif choice == '2':
                self.retrieve_studentinfo()
            elif choice == '3':
                self.update_studentinfo()
            elif choice == '4':
                self.delete_studentinfo()
            elif choice == '5':
                self.display_allstudentinfo()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    student = grade_manager("", "", "", 0)
    student.main_menu()
    



 








                




                


        
        

           


            

