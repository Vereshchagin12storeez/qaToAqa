import requests
import jsonschema
from pprint import pprint
from JsonSchemas import GET_ALL_PRODUCTS_SCHEMA

BEARER_TOKEN = "5382db931b9a4d88bfe4484da0163835"
URL = "https://mercaux.12stz.dev/api/v1/catalog"
MERCAUX_HEADERS = {'Authorization': f'Bearer {BEARER_TOKEN}',
                   'Content-Type': 'application/json'}


def check_article(products_lst, article):
    for product in products_lst:
        product_article = product.get("article")
        if product_article == article:
            return True
    return


def validate_json_schema(instance: dict, schema):
    try:
        jsonschema.validate(instance=instance, schema=schema)
    except jsonschema.exceptions.ValidationError:
        testit.addMessage("Json-схема response не соответствует ожидаемой.")
        return False
    return True


def test_get_products_list():
    response = requests.request(method="GET",
                                url=URL,
                                headers=MERCAUX_HEADERS)
    assert response.status_code == 200  # Проверка статус кода

    response_dict = response.json()
    product_lst = response_dict.get("results")
    assert product_lst != []  # Проверка что список(массив) не является пустым

    article = "111147"

    check_result = check_article(product_lst, article)  # Проверка наличия элемента в списке(массиве)
    assert check_result

    assert isinstance(article, str)  # Проверка элемента на тип данных

    assert len(product_lst) == 50  # Проверка длины списка(массива)

    assert validate_json_schema(response_dict, GET_ALL_PRODUCTS_SCHEMA)  # Валидация Json-схемы
