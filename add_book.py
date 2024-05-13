from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        
        new_book = ("Hallow", 4, 455, "12222", "2012-03-14" )
        
        query = "INSERT INTO books (title, author_id, genre_id, isbn,publication_date) VALUES (%s, %s, %s, %s, %s)"
        
        cursor.execute(query, new_book)
        conn.commit()
        print("New book added successfully.")
        
    except Exception as e:
        print("Error:", e)
        
    finally:
        cursor.close()
        conn.close()


