import psycopg2


def insert_category(title, link):
    with psycopg2.connect(
            database="OOP_parsing", host="localhost",
            port=5432, user="postgres",
            password=123456
    ) as database:
        cursor = database.cursor()

        cursor.execute("""
        INSERT INTO category(category_title, category_link)
        VALUES (%s, %s);
        """, (title, link))

        database.commit()


def get_category_id(title):
    with psycopg2.connect(
            database="OOP_parsing", host="localhost",
            port=5432, user="postgres",
            password=123456
    ) as database:
        cursor = database.cursor()

        cursor.execute("""
        SELECT category_id FROM category WHERE category_title = (%s);
        """, (title,))

        category_id = cursor.fetchone()[0]

        return category_id


def insert_product_data(category_id, product_title, product_link,
                        product_price, product_image, product_description):
    with psycopg2.connect(
            database="OOP_parsing", host="localhost",
            port=5432, user="postgres",
            password=123456
    ) as database:
        cursor = database.cursor()

        cursor.execute("""
        INSERT INTO product(category_id, product_title, product_link,
                        product_price, product_image, product_description)
        VALUES(%s, %s, %s, %s, %s, %s)
        """, (category_id, product_title, product_link,
              product_price, product_image, product_description))
        database.commit()


def get_product_id(title):
    with psycopg2.connect(
            database="OOP_parsing", host="localhost",
            port=5432, user="postgres",
            password=123456
    ) as database:
        cursor = database.cursor()

        cursor.execute("""
        SELECT product_id FROM product WHERE product_title = (%s);
        """, (title,))

        product_id = cursor.fetchone()[0]

        return product_id


def insert_characteristic(product_id, characteristics: dict):
    with psycopg2.connect(
            database="OOP_parsing", host="localhost",
            port=5432, user="postgres",
            password=123456
    ) as database:
        cursor = database.cursor()

        for key, value in characteristics.items():
            cursor.execute("""
                INSERT INTO characteristic(product_id, characteristic_title, characteristic_text)
                VALUES(%s, %s, %s)
            """, (product_id, key, value))

            database.commit()
