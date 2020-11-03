import os
import sqlite3


class SqliteDB(object):
    def __init__(self, dbname=None, create=False):
        self.conn = None
        self.create = create
        if(dbname is not None):
            self.dbname = dbname

    @property
    def connection(self):
        return self.open()

    def open(self):
        if(self.conn is None):
            if(os.path.isfile(self.dbname) or self.create):
                self.conn = sqlite3.connect(self.dbname)
        return self.conn

    def close(self):
        if(self.conn is not None):
            self.conn.close()

    def execute(self, sql):
        conn = self.open()
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
