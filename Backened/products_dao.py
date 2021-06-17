from sql_connection import get_sql_connection


def get_all_products(connection):

    cursor = connection.cursor()
    query =("select books.Book_id, books.Book_Name, books.uom_id, books.Price_per_unit, uom.uom_name "
            "from books inner join uom on books.uom_id=uom.uom_id")
    cursor.execute(query)

    response = []

    for (Book_id, Book_Name, uom_id, Price_per_Unit, uom_name) in cursor:
        response.append(
            {
                'Book_id' : Book_id,
                'Book_Name' : Book_Name,
                'uom_id' : uom_id,
                'Price_per_Unit' : Price_per_Unit,
                'uom_name' : uom_name
            }
        )

    return response

def insert_new_product(connection, books):
    cursor = connection.cursor()
    query = ("INSERT INTO books "
            "(Book_Name, uom_id, Price_per_unit)"
            "values (%s, %s, %s)")
    data = (books["Book_Name"], books["uom_id"], books["Price_per_unit"])
    cursor.execute(query, data)
    connection.commit()
    
    return cursor.lastrowid

def delete_new_product(connection, Book_id):
    cursor = connection.cursor()
    query = ("DELETE FROM books where Book_id=" + str(Book_id))
    cursor.execute(query)
    connection.commit()


if __name__ =="__main__":
    connection = get_sql_connection()
    print(delete_new_product(connection,13))

