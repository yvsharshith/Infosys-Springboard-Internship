from fastapi import FastAPI, HTTPException
from sql import get_db
from mysql.connector import Error  # type: ignore

app = FastAPI()

@app.post("/users")
def create_user(name: str, email: str, password: str):
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)

        query = "INSERT INTO tbluser(name, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, password))
        db.commit()

        return {"message": "user created successfully"}
    except Error as e:  # type: ignore
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        db.close()

@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)

        query = "SELECT id, name, email, password FROM tbluser WHERE id=%s"
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return {"message": "user fetched successfully", "data": user}
    except Error as e:  # type: ignore
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        db.close()

@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, email: str):
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)

        query = "UPDATE tbluser SET name=%s, email=%s WHERE id=%s"
        cursor.execute(query, (name, email, user_id))
        db.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")

        return {"message": "user updated successfully"}
    except Error as e:  # type: ignore
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        db.close()

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    try:
        db = get_db()
        cursor = db.cursor(dictionary=True)

        query = "DELETE FROM tbluser WHERE id=%s"
        cursor.execute(query, (user_id,))
        db.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")

        return {"message": "user deleted successfully"}
    except Error as e:  # type: ignore
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        db.close()
