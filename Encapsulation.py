#Encapsulation yani kapsülleme sınıfın verilerini dış erişime kapatıp sadece
#belirlenen metotlar aracılığıyla erişim sağlamaktır.

#öğrencilerin bilgilerini tutan ve not ortalamalarını hesaplayabildiğmiz
#bir sistem oluşturalım. ancak öğrenci bilgileri gizli tutulmalı.

class Student:
    def __init__(self,name,surname,student_id,):
        self.__name = name
        self.__surname = surname
        self.__student_id = student_id
        self.__grades = {}

    def add_new_grade(self,subject,grade):
        if 0 <= grade <= 100:
            if subject not in self.__grades:
                self.__grades[subject] = []
            self.__grades[subject].append(grade)
            print(f'{subject} grade ({grade}) added..!')
        else:
            print("Invalid grade, please enter a value between 0 and 100..!")

    def student_average(self):
         total_grades=[grade for grades in self.__grades.values() for grade in grades]
         return sum(total_grades)/len(total_grades)

    def subject_avergence(self,subject):
        if subject in self.__grades:
            return sum(self.__grades[subject])/len(self.__grades[subject])
        else:
            return "This subject has no grades"

    def student_info(self):
        print(f'Student Name: {self.__name} {self.__surname}\nStudent ID: {self.__student_id}')
        print(f"Student's Grades: {self.__grades}")
        print(f"Student Average: {self.student_average()}")
        for subject,grades in self.__grades.items():
            print(f"Subject: {subject} Average: {self.subject_avergence(subject)}")

student1 = Student("Ahmet", 20, "S12345")
student1.add_new_grade("Matematik", 85)
student1.add_new_grade("Fizik", 90)
student1.add_new_grade("Matematik", 78)
student1.add_new_grade("Türkçe",87)
student1.student_info()




