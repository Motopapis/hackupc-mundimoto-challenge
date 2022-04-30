import psycopg2
import logging

class postgresql_utils():

    def __init__(self):
        # Constructor
        pass

    @staticmethod
    def get_full_inner_data(conn):
        try:
            cursor = conn.cursor()
            # Select the inner join data (supposedly its the whole datasets stiched together, 
            # but this way we eliminate and filter the empty ones).
            cursor.execute("SELECT * FROM brands INNER JOIN versions ON brands.id = versions.brand_id;")
            return cursor.fetchall()
        except psycopg2.Error as e:
            logging.error(e.pgerror)
            return None
