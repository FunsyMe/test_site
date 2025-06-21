import sqlite3

class Database:
    def __init__(self, db_file = 'databaser.db'):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Errors (
                id CHAR(16) PRIMARY KEY
            )''')

        self.connection.commit()

    def add_id(self, id):
        self.cursor.execute('''
            INSERT INTO Errors VALUES (?)''', (id,))
        
        print(f"Добавил в БД ошибку: {id}")
        self.connection.commit()

    def get_id(self, id):
        self.cursor.execute('''
            SELECT * FROM Errors WHERE id = (?)''', (id,))
            
        return self.cursor.fetchone()
