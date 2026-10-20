import requests;
import logging;
import pathlib;

response = requests.get("https://dummyjson.com/products");
outputFilePath = pathlib.Path("apiResponseData.txt");
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        # logging.StreamHandler(),
        logging.FileHandler(outputFilePath,mode = 'w',encoding="utf-8")
    ]
);

def filteredProduts(productsList = list(), category = None, priceUpto = None):
    for productDict in productsList:
        if productDict.get('category') == category and productDict.get('price') <= priceUpto:
            logging.info(productDict);
            print(productDict);


if response.status_code == 200:
    listOfdata = list();
    products = response.json()["products"];
    # logging.info(products);

    for product in products:
        # logging.info(product["id"]);
        productData = {
            "id" : product["id"],
            "title": product["title"],
            "description" : product["description"],
            "category": product["category"],
            "price": product["price"]
        };
        listOfdata.append(productData);

    #Take input to filter out the data:
    userSelectedCategory = input("Enter Product Category: ");
    userSelectedPriceRange = float(input("Enter Your Budget: "));

    filteredProduts(listOfdata,userSelectedCategory,userSelectedPriceRange);
else:
    logging.error("Getting API Issue");

logging.info("Operation Completed!");