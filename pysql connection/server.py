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

def update_user(user_id, name, email):
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        
        query = "update tbluser set name=%s, email=%s where id=%s"
        cursor.execute(query, (name, email, user_id))
        db.commit()
        
        return {"message": "user updated successfully"}
    except Error as e: # type: ignore
        return {"error": str(e)}
    finally:
        cursor.close()
        db.close()

def delete_user(user_id):
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        
        query = "delete from tbluser where id=%s"
        cursor.execute(query, (user_id,))
        db.commit()
        
        return {"message": "user deleted successfully"}
    except Error as e: # type: ignore
        return {"error": str(e)}
    finally:
        cursor.close()
        db.close()
