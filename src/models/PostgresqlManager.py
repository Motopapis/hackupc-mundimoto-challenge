import psycopg2
import logging

class postgresql_manager():
    logger = logging.getLogger()
    __instance = None
    conn = None

    def get_instance():
        if postgresql_manager.__instance == None:
            postgresql_manager()
        return postgresql_manager.__instance
    
    def __init__(self):
        if postgresql_manager.__instance != None:
            raise Exception('singletone already initialised')
        else:
            postgresql_manager.__instance = self
            self.conn = psycopg2.connect(
                dbname      = "mundimoto",
                host        = "localhost",
                port        = "5432",
                user        = "hackupc",
                password    = "not_secure_pass"
            )
            self.logger.info(f"Started connection on {self.conn}")

    def raw_query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)

        return cursor.fetchall()
        
    def get_query(self, fields = None, tables=None, options=None):
        if fields == None:
            return None, False

        if tables == None:
            return None, False
        
        query = "SELECT"
        for field in fields:
            query += f" {field}"
        
        query += " FROM"
        for table in tables:
            query += f" {table}"
        
        if options != None:
            if type(options) == type("") and len(options) > 0:
                query += f" {options}"

        query += ";"
        cursor = self.conn.cursor()
        cursor.execute(query)

        return cursor.fetchall(), True