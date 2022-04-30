from src.models.PostgresqlManager import postgresql_manager
from src.models.Brand import Brand
from src.models.Bike import Bike

class postgresql_controller():
    manager = postgresql_manager.get_instance()

    @staticmethod
    def get_all_catalogue():
        manager = postgresql_manager.get_instance()
        obj, condition = manager.get_query(
            fields=['*'], 
            tables=['brands'],
            options='INNER JOIN versions ON brands.id = versions.brand_id'
        )

        if obj == None or condition == False:
            return None, condition
        
        posts = []
        for entry in obj:
            # (id, name, id, model, brand_id, year, fuel, price)
            posts.append(Bike(
                    brand=entry[1],
                    model=entry[3],
                    year=entry[5],
                    fuel=entry[6],
                    price=entry[7]
                )
            )
        posts_json = [post.to_safe_json() for post in posts]
        return posts_json, condition

        

    @staticmethod
    def get_brands():
        manager = postgresql_manager.get_instance()
        obj, condition = manager.get_query(
            fields=['*'], 
            tables=['brands']
        )

        if obj != None:
            # (id, name)
            brands = []
            for entry in obj:
                id, name = entry
                models, valid = manager.get_query(
                    fields=['name'],
                    tables=['versions'],
                    options=f'WHERE brand_id = {id}'
                )

                models_name = []

                if valid == False:
                    return models, valid

                for model in models:
                    # (name)
                    version = model[0]
                    if version not in models_name:
                        models_name.append(version)
                    
                brands.append(Brand(name, models_name))
        brands_json = [brand.to_safe_json() for brand in brands]
        return brands_json, condition

    @staticmethod
    def get_raw_query(query):
        manager = postgresql_manager.get_instance()
        obj = manager.raw_query(query)

        return obj