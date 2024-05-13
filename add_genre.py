from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        
        new_genre = (2, "Jk Rowling", "Scary dark book", "Book" )
        
        query = "INSERT INTO genres (id, name, description, category) VALUES (%s, %s, %s, %s)"
        
        cursor.execute(query,new_genre)
        conn.commit()
        print("New genre added successfully.")
        
    finally:
        cursor.close()
        conn.close()
        