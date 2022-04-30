import unittest

class TestPostgres(unittest.TestCase):
    def test_import_psycopg2(self):
        is_ok = False
        try:
            import psycopg2
            is_ok = True
        except:
            print("ERROR: You do not have psycopg2, we highly suggest that you look at the README.md for more information and detailed solutions")

        self.assertTrue(is_ok)
    
    def test_connect_to_postgres(self):
            is_ok = False
            try:
                from psycopg2 import connect

                con = connect(
                    dbname      = "mundimoto",
                    host        = "localhost",
                    port        = "5432",
                    user        = "hackupc",
                    password    = "not_secure_pass"
                )

                is_ok = True
            except:
                print("ERROR: error while connecting to the postgresql. Check postgresql is up and running, check URL and port parameters.")
            
            self.assertTrue(is_ok)


if __name__ == "__main__":
    unittest.main()
