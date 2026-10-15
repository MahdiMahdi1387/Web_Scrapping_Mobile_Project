import sqlite3 as sq


class Database_control:
    def __init__(self, DB_NAME='Mobile.db'):
        self.DB_NAME = DB_NAME


    def init(self) -> bool:
        '''Inits the database.'''

        try:
            conn = sq.connect(self.DB_NAME)
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS mobile(
                id INTEGER primary key AUTOINCREMENT,
                description TEXT,
                brand TEXT,
                memory TEXT,
                ram TEXT,
                rating REAL
            )''')
            return True
        except Exception as e:
            print(f'An error occurred:\n{e}')
            return False
        finally:
            conn.close()


    def add(self, mobile_id: int, description: str, brand: str,
            memory: str, ram: str, rating: float) -> bool:
        '''Adds a record to database.'''

        try:
            conn = sq.connect(self.DB_NAME)
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO mobile(id, description, brand, 
            memory, ram, rating) VALUES(?, ?, ?, ?, ?, ?)''',
            (mobile_id, description, brand, memory, ram, rating))
            conn.commit()
            return True
        except Exception as e:
            print(f'An error occurred:\n{e}')
            return False
        finally:
            conn.close()


    def show_record(self, mobile_id: int) -> bool:
        try:
            conn = sq.connect(self.DB_NAME)
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM mobile WHERE id = ?''',
                          (mobile_id,))
            return True
        except Exception as e:
            print(f'An error occurred:\n{e}')
            return False
        finally:
            conn.close()
