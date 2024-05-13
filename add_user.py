from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        
        new_author = (2, "Jk Rowling", 233 )
        
        query = "INSERT INTO users (id, name,library_id) VALUES (%s, %s, %s)"
        
        cursor.execute(query,new_author)
        conn.commit()
        print("New user added successfully.")
        
    finally:
        cursor.close()
        conn.close()
        