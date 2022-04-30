import pandas as pd
import numpy as np
from User import User
from Point5d import Point5d
from Vector5d import vector_5d
from utils.vector_utils import VectorUtils
import random
if __name__ == '__main__':
    data = pd.read_csv("./data/results.csv")
    priceArray= data.drop(columns=['ID','BRAND','MODEL','YEAR','FUEL'])
    minPrice = priceArray['PRICE'].min()
    maxPrice = priceArray['PRICE'].max()
    print("Rango prices:")
    print(minPrice)
    print(maxPrice)
    brandArray = data.drop(columns=['ID','PRICE','MODEL','YEAR','FUEL'])
    minBrand = brandArray['BRAND'].min()
    maxBrand = brandArray['BRAND'].max()
    print ("Rango brand:")
    print(minBrand)
    print(maxBrand)
    modelArray = data.drop(columns=['ID','PRICE','BRAND','YEAR','FUEL'])
    minModel = modelArray['MODEL'].min()
    maxModel= modelArray['MODEL'].max()
    print ("Rango model:")
    print(minModel)
    print(maxModel)
    yearArray = data.drop(columns=['ID','PRICE','BRAND','MODEL','FUEL'])
    minYear = yearArray['YEAR'].min()
    maxYear= yearArray['YEAR'].max()
    print ("Rango years:")
    print(minYear)
    print(maxYear)
    fuelArray = data.drop(columns=['ID','PRICE','BRAND','YEAR','MODEL'])
    minFuel = fuelArray['FUEL'].min()
    maxFuel= fuelArray['FUEL'].max()
    print ("Rango FUEL:")
    print(minFuel)
    print(maxFuel)
    userList = []
    for i in range(1000):
        randomPrice = random.randint(minPrice, maxPrice)
        randomBrand = random.randint(minBrand, maxBrand)
        randomModel = random.randint(minModel, maxModel)
        randomYear = random.randint(minYear, maxYear)
        randomFuel = random.randint(minFuel, maxFuel)
        userPoint = Point5d(randomPrice, randomBrand, randomModel, randomYear, randomFuel)
        tolerance = random.randint(5000, 8000)
        print(f"Generating User({randomPrice}, {randomBrand}, {randomModel}, {randomYear}, {randomFuel}, {tolerance})")
        user = User(id=i, point5d = userPoint, tolerance = tolerance)
        userList.append(user)

    for row in data.itertuples():

        pointMoto = Point5d(row[5], row[1], row[2], row[3], row[4])
        for user in userList:
            vector = vector_5d(user.point5d, pointMoto)
            module = VectorUtils.compute_module(vector)
            like = 0
            if (module <= user.tolerance):
                like = 1
            
            user.likeList[row[0]] = like
            print(f"user {user.id} catalogues {like} moto {row[0]}")

    with open("./data/like.csv", "w") as f:
        f.write("USER,MOTO,LIKE\n")
        for user in userList:
            for like in user.likeList:
                print(f"checking user {user.id} for like {like} with value {user.likeList[like]}")
                f.write(f"{user.id},{like},{user.likeList[like]}\n")

        

