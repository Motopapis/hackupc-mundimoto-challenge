import psycopg2
from utils.postgresql_utils import postgresql_utils

def main():
    con = psycopg2.connect(
        dbname      = "mundimoto",
        host        = "localhost",
        port        = "5432",
        user        = "hackupc",
        password    = "not_secure_pass"
    )
    cursor = con.cursor()

    cursor.execute("SELECT * FROM brands INNER JOIN versions ON brands.id = versions.brand_id;")
    results = cursor.fetchall() 

    models = []
    for result in results:
        model = result[3]
        if model not in models:
            models.append(model)
    
    print(len(models), len(results))

if __name__ == "__main__":
    main()