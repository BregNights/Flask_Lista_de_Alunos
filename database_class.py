import mysql.connector

class MyDatabase:

    def __init__(self):
        try:
            self._db = mysql.connector.connect(
                host='localhost',
                database='apexalunos',
                user='root',
                password='apex2223'
            )
            self._cursor = self._db.cursor()
        except Exception as e:
            print(f"Erro ao conectar no bando de dados. error {e}")


class StudentsDatabase(MyDatabase):

    def __init__(self):
        super().__init__()

        self._create_table()

    def _create_table(self):

        query = (
            "CREATE TABLE IF NOT EXISTS students ("
            "id INT AUTO_INCREMENT PRIMARY KEY,"
            "name VARCHAR(255) NOT NULL,"
            "email VARCHAR(255) NOT NULL,"
            "course VARCHAR(255) NOT NULL,"
            "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
            ")  ENGINE=INNODB;"
        )
        self._cursor.execute(query)

    def insert(self, name, email, course):

        self._cursor.execute(
            "INSERT INTO students (name, email, course) VALUES (%s,%s,%s)",
            (f"{name}",f"{email}",f"{course}" )
        )

        self._db.commit()

    def select(self, id=None):

        if id:
            self._cursor.execute(f"SELECT * FROM students WHERE id = {id}")
        else:
            self._cursor.execute("SELECT * FROM students")

        return self._cursor.fetchall()

    def delete(self, id):
        self._cursor.execute(
            f"DELETE FROM students WHERE id = {id}"
        )

        self._db.commit()

    def update(self, id):
        self._cursor.execute(
            f"UPDATE students SET name=name, email=email, course=course WHERE id = {id}"
        )

        self._db.commit()