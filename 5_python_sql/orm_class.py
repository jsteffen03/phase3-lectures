# Now how can we implement this into a class
# With this we need to start by asking how we map from Sql to Python
# 
# We can fetch using .fetchone() or .fetchall()
import sqlite3
connection = sqlite3.connect("school.db")

cursor = connection.cursor()

class Student:
    def __init__(self,name,grade,id=None):
        self.id = id
        self.name = name
        self.grade = grade

    def add_to_database(self):
        insert = f'''
        INSERT INTO student(name,grade)
        VALUES ("{self.name}","{self.grade}")
        '''
        cursor.execute(insert)
        connection.commit()
    
    def change_attr(self,attr,new_value):
        change = f'''
        UPDATE student
        SET {attr}= "{new_value}"
        WHERE id = {self.id}
        '''
        cursor.execute(change)
        connection.commit()

    def delete_self(self):
        delete = f'''
        DELETE FROM student
        WHERE id = {self.id}
        '''
        cursor.execute(delete)
        connection.commit()

    def get_schedule(self):
        get = f'''
        SELECT student.name, schedule.classname
        FROM schedule
        JOIN student,teacher
        ON schedule.student_id = student.id
        WHERE student.id = {self.id};
        '''
        return cursor.execute(get).fetchall()

    @classmethod
    def get_all_students(cls):
        find = f'''
        SELECT * FROM student;
        '''
        return cursor.execute(find).fetchall()
    

    # def add

    

# ben = Student("Ben",10)
all_stud = Student.get_all_students()
all_stud_obj = []
for student in all_stud:
    new_stud = Student(student[1],student[2],student[0])
    all_stud_obj.append(new_stud)

jacob = all_stud_obj[0]
print(jacob.get_schedule())