from sql import get_db

def create_user(name, email, password):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    # cursor is used to execute sql commands in py
    
    query = "Insert into tbluser(name, email, password) values(%s, %s, %s)"
    cursor.execute(query,(name, email, password))
    db.commit()
    cursor.close()
    return {"message":"user created sucessfully"}

# results = create_user("harshith", "harshith@gmail.com", "harsh123")
# print(results)

def get_user_by_id(user_id):
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        query = "select id, name, password, email from tbluser where id=%s"
        cursor.execute(query,(user_id),)
        user = cursor.fetchone()
        
        return {"message":"user fetched successfully", "data": user}
    except Error as e: # type: ignore
        return {"error": str(e)}
    finally:
        cursor.close()
        db.close()

result2 = get_user_by_id(4)
print(result2)