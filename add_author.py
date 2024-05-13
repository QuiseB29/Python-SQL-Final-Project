from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        
        new_author = (1, "Jk Rowling", "New York")
        
        query = "INSERT INTO authors (id, name, biography) VALUES (%s, %s, %s)"
        
        cursor.execute(query,new_author)
        conn.commit()
        print("New author added successfully.")
        
    finally:
        cursor.close()
        conn.close()
        