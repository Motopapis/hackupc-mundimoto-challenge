import psycopg2
from models.Post import Post
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

    # Model explanation
    # (brand_id, brand_name, version_id, model, brand_id, year, fuel, price)

    models = []
    for result in results:
        model = result[3]
        if model not in models:
            models.append(model)
    
    models_map = {}
    index = 0
    for model in models:
        models_map[model] = index
        index += 1
    
    posts = []
    for result in results:
        brand_id = result[0]
        price = result[7]
        year = result[5]
        fuel = result[6]
        model_string = result[3]

        model = models_map[model_string]

        posts.append(Post(brand = brand_id, model = model, year=year, fuel = fuel, price = price))


    id = 0
    with open("data/results.csv", "w") as f:
        f.write("ID,BRAND,MODEL,YEAR,FUEL,PRICE\n")
        for post in posts:
            f.write(f"{id},{post.get_brand()},{post.get_model()},{post.get_year()},{post.get_fuel()},{post.get_price()}\n")
            id += 1

if __name__ == "__main__":
    main()