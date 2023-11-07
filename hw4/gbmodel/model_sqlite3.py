"""
SQL model for a quote_library webapp.

Schema for the SQLite database:

+---------------------+--------+--------+-------------------------+
| Person              | Source | Rating | Quote                   |
+=====================+========+========+=========================+
| William Shakespeare | Hamlet | 9      | "To be or not to be..." |
+---------------------+--------+--------+-------------------------+

Created with SQL: 
    CREATE TABLE quote_library (person TEXT, source TEXT, rating INTEGER, quote TEXT);

"""

from .Model import Model
import sqlite3
DB_FILE = 'quote_library.sqlite'


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
            cursor.execute("CREATE TABLE quote_library (person TEXT, source TEXT, rating INTEGER, quote TEXT)")
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
    
    def insert_quote(self, person, source, rating, quote):
        """
        Inserts quote into database, using Model's parameters. 
        :param person: String
        :param source: String 
        :param rating: int
        :param quote: String
        :return: True
        """
        parameters = {'person':person, 'source':source, 'rating':rating, 'quote':quote, }
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
             cursor.execute("INSERT INTO quote_library (person, source, rating, quote) VALUES (:person, :source, :rating, :quote, )", parameters)
        except sqlite3.OperationalError as error:
            print(error)

        # Commit makes the database change visible to other open connections.
        connection.commit()
        cursor.close()
        return True



        

