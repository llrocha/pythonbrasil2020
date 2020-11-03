from sqlite_db import SqliteDB


class ZipCodeDB(SqliteDB):

    def __init__(self, db_name, create = False):
        self.auto_commit = False
        # Database definitions
        self.DATABASE_NAME = db_name
        self.TABLE_NAME = 'CEP'
        self.CREATE_TABLE = """
          CREATE TABLE {0} (
            ID INTEGER PRIMARY KEY,
            CEP TEXT,
            CIDADE INT,
            ESTADO INT,
            BAIRRO INT,
            LOGRADOURO NUMERIC,
            DESCRICAO TEXT
          );
          """.format(self.TABLE_NAME)
        self.TABLE_FIELDS = ['ID', 'CEP', 'CIDADE', 'ESTADO', 'BAIRRO', 'LOGRADOURO', 'DESCRICAO']
        self.INSERT = 'INSERT INTO {0} ({1}) VALUES (?, ?, ?, ?, ?, ?, ?);'.format(self.TABLE_NAME, ', '.join(self.TABLE_FIELDS))
        self.UPDATE = 'UPDATE {0} SET {{0}} = ? WHERE ID = ?;'.format(self.TABLE_NAME)
        self.SELECT_ALL = 'SELECT {{0}} FROM {0} ORDER BY ID'.format(self.TABLE_NAME)
        self.SELECT_FILTER = 'SELECT {{0}} FROM {0} WHERE {{1}}'.format(self.TABLE_NAME)

        SqliteDB.__init__(self, self.DATABASE_NAME, create)

        conn = self.open()
        if(conn is not None):
            sql = "SELECT count(1) FROM sqlite_master WHERE type='table' AND name='{0}';".format(self.TABLE_NAME)
            cursor = conn.cursor()
            cursor.execute(sql)
            table_exists = int(cursor.fetchone()[0])
            if(not bool(table_exists)):
                print('Tabela não existe! {0}'.format(self.TABLE_NAME))
                self.connection.execute(self.CREATE_TABLE)
                self.connection.commit()
        else:
            raise Exception('Não foi possível abrir [{0}]'.format(self.DATABASE_NAME))

    def insert(self, CEP, CIDADE, ESTADO, BAIRRO=None, LOGRADOURO=None, DESCRICAO=None):
        conn = self.open()
        sql = self.INSERT
        ID = int(CEP)
        conn.execute(sql, (ID, CEP, CIDADE, ESTADO, BAIRRO, LOGRADOURO, DESCRICAO))
        if(self.auto_commit):
            conn.commit()

    def select_all(self, fields=None):
        sql = self.SELECT_ALL.format(', '.join(self.TABLE_FIELDS))
        return self.execute(sql)

    def select_where(self, filter):
        sql = self.SELECT_FILTER.format(', '.join(self.TABLE_FIELDS), filter)
        return self.execute(sql)

    def commit(self):
        self.connection.commit()
