import unittest
import logging
import psycopg2
from utils.postgresql_utils import postgresql_utils

class test_postgresql_utils(unittest.TestCase):
    def test_retrieve_inner_join(self):
        try:

            con = psycopg2.connect(
                dbname      = "mundimoto",
                host        = "localhost",
                port        = "5432",
                user        = "hackupc",
                password    = "not_secure_pass"
            )

            data = postgresql_utils.get_full_inner_data(con)

        except psycopg2.Error as e:
            logging.error(e.pgerror)
            data = None
        
        self.assertNotEqual(None, data)