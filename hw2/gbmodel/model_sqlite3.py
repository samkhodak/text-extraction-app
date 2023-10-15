"""
SQL model for a quote_library webapp.

Schema for the SQLite database:

+-------------------------+---------------------+--------+--------+
| Quote                   | Person              | Source | Rating |
+=========================+=====================+========+========+
| "To be or not to be..." | William Shakespeare | Hamlet | 9      |
+-------------------------+---------------------+--------+--------+

Created with SQL: 
    CREATE TABLE quote_library (quote TEXT, person TEXT, source TEXT, rating INTEGER);

"""

from .Model import Model
import sqlite3
DB_FILE = 'quote_library.db'


class model(Model):
    def __init__(self):
        """
        Initializes model class by creating backend database if one does not already exist in DB_FILE.
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT COUNT(rowid) FROM quote_library")
        except sqlite3.OperationalError:
            cursor.execute("CREATE TABLE quote_library (quote TEXT, person TEXT, source TEXT, rating INTEGER)")
        cursor.close()

    def select_quotes(self):
        """
        Selects all rows from database and returns an iterable list of lists.
        Each row contains data in the format of the schema above.
        :return: List of lists, with each list being a row from the database.
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM quote_library")
        except sqlite3.OperationalError as error:
            print (error)
        return cursor.fetchall()
    
    def insert_quote(self, quote, person, source, rating):
        """
        Inserts quote into database, using Model's parameters. 
        :param quote: String
        :param person: String
        :param source: String 
        :param rating: int
        :return: True
        """
        parameters = {'quote':quote, 'person':person, 'source':source, 'rating':rating}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
             cursor.execute("INSERT INTO quotes (quote, person, source, rating) VALUES (:name, :email, :date, :message)", parameters)
        except sqlite3.OperationalError as error:
            print(error)

        # Commit makes the database change visible to other open connections.
        connection.commit()
        cursor.close()
        return True



        

