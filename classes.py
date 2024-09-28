from database_class import StudentsDatabase

class Student:

    def __init__(self, name, email, course, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.course = course

    def asdict(self):
        return {
            "id": self.id,
            "nome": self.name,
            "email": self.email,
            "curso": self.course
        }


class StudentControl():

    def __init__(self):
        self._student_db = StudentsDatabase()

    def create_student(self, name, email, course):
        self._student_db.insert(
            name=name,
            email=email,
            course=course
        )

    def get_students(self, id=None):
        return [
            Student(
                id=value[0],
                name=value[1],
                email=value[2],
                course=value[3],
            )
            for value in self._student_db.select(id=id)
        ]

    def delete_student(self, id):
        self._student_db.delete(id)
        
    def update_student(self, id):
        self._student_db.update(id)





