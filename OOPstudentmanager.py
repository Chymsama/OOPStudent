#!/usr/bin/env python
# coding: utf-8

# Xây dựng ứng dụng quản lý sinh viên với các chức năng cơ bản sau:
# Xem danh mục sinh viên
# Thêm sinh viên mới vào danh mục
# Cập nhật thông tin của sinh viên trong danh mục
# Xóa thông tin sinh viên khỏi danh mục
# Tìm kiếm thông tin sinh viên trong danh mục theo từ khóa
# Sắp xếp thông tin sinh viên trong danh mục
# Hướng dẫn
# Xây dựng lớp Student với các thuộc tính như mã sinh viên, họ tên, ngày tháng năm sinh, quê quán, chuyên ngành, lớp…Chức năng chính của lớp này là lưu giữ thông tin của 1 sinh viên
# 
# Xây dựng lớp danh mục sinh viên (Student_List) với thuộc tính là một List các đối tượng của lớp Student vừa xây dựng ở trên. Lớp này có các hàm thành viên tương ứng với các chức năng như đề bài yêu cầu. Mỗi hàm chức năng đều thao tác trên thuộc tính List sinh viên của lớp này. 

# In[5]:


class Student:
    def __init__(self,studentID,studentName,DOB,home,major,classname):
        self.studentID=studentID
        self.studentName= studentName
        self.DOB= DOB
        self.home= home
        self.major= major
        self.classname = classname
        
class StudentList:
    def __init__(self):
        self.Student = []
        
    def getstudent(self):
        if not self.Student:
            print('Danh sách sinh viên rỗng: ')
            return
        print('Danh sach sinh viên: ')
        for Student in self.Student:
            print(f"Mã Sinh Viên: {Student.studentID} -- Họ và tên: {Student.studentName} -- Ngày sinh: {Student.DOB} -- Quê quán: {Student.home} -- Lớp: {Student.classname}")
     
    
    def addstudent(self):
        StudentID = input("Nhập mã sinh viên: ")
        StudentName = input("Nhập tên sinh viên: ")
        DOB = input("Nhập ngày tháng năm sinh(MM/dd/YYYY): ")
        home = input("Nhập quê quán: ")
        major = input("Nhập chuyên ngành: ")
        classname = input("Nhập tên lớp: ")

        NewStudent = Student(StudentID, StudentName, DOB, home, major, classname)
        self.Student.append(NewStudent)
    
    
    
    def updatestudent(self):
        studentID = input("Nhập mã sinh viên cần cập nhật: ")
        update_student = self.searchstudent(studentID)
        if update_student:
            StudentName = input("Nhập tên sinh viên: ")
            DOB = input("Nhập ngày tháng năm sinh(MM/dd/YYYY): ")
            home = input("Nhập quê quán: ")
            major = input("Nhập chuyên ngành: ")
            classname = input("Nhập tên lớp: ")

            new_student = Student(studentID, StudentName, DOB, home, major, classname)
            success = self.updatestudent(new_student)
            if success:
                print("Đã cập nhật thông tin sinh viên:")
            else:
                print("Cập nhật không thành công.")
        else:
            print("Không tìm thấy sinh viên có mã này")

    
    def deleteStudent(self):
        studentID = input("Nhập mã sinh viên cần xóa: ")
        for i, student in enumerate(self.Student):
            del self.Student[i]
            print("Đã xóa thông tin sinh viên.")
            return
        print("Không tìm thấy sinh viên có mã này.")

    
    def searchstudent(self,keyword):
        result = []
        for student in self.Student:
            if (keyword.lower() in student.studentID.lower()) or \
               (keyword.lower() in student.studentName.lower()) or \
               (keyword.lower() in student.home.lower()):
                result.append(student)
        return result
    
    
    def searchby(self):
        keyword = input("Nhập từ khóa tìm kiếm: ")
        result = []
        for student in self.Student:
            if (keyword.lower() in student.studentID.lower()) or \
               (keyword.lower() in student.studentName.lower()) or \
               (keyword.lower() in student.home.lower()):
                result.append(student)
        if result:
            print("Kết quả tìm kiếm:")
            for student in result:
                print(f"Mã Sinh Viên: {student.studentID} -- Họ và tên: {student.studentName} -- Ngày sinh: {student.DOB} -- Quê quán: {student.home} -- Lớp: {student.classname}")
        else:
            print("Không tìm thấy sinh viên phù hợp.")
    
    
    def sortbyname(self):
        self.student.sort(key=lambda student: student.studentName.lower())
    
class Menu:
    def __init__(self):
        self.StudentList = StudentList()
    
    def display_menu(self):
        print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
        print("1. Xem danh sách sinh viên")
        print("2. Thêm sinh viên mới")
        print("3. Cập nhật thông tin sinh viên")
        print("4. Xóa thông tin sinh viên")
        print("5. Tìm kiếm sinh viên theo từ khóa")
        print("6. Sắp xếp sinh viên theo tên")
        print("0. Thoát chương trình")
        
    def run(self):
        while True:
            self.display_menu()
            choice = input("Nhập lựa chọn của bạn: ")

            if choice == "1":
                self.StudentList.getstudent()
            elif choice == "2":
                self.StudentList.addstudent()
            elif choice == "3":
                self.StudentList.updatestudent()
            elif choice == "4":
                self.StudentList.deleteStudent()
            elif choice == "5":
                self.StudentList.searchby()
            elif choice =="0":
                break
if __name__ == "__main__":
    menu = Menu()
    menu.run()

