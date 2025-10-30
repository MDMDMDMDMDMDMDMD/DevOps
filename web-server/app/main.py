from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from typing import List, Dict

app = FastAPI(title="DevOps Lab API")

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "db-server"),
    "port": os.getenv("DB_PORT", "5432"),
    "database": os.getenv("DB_NAME", "devops_lab"),
    "user": os.getenv("DB_USER", "devops"),
    "password": os.getenv("DB_PASSWORD", "devops123")
}

def get_db_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

@app.get("/", response_class=HTMLResponse)
async def root():
    conn = get_db_connection()
    if not conn:
        return "<h1>Ошибка подключения к базе данных</h1>"
    
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM users ORDER BY id")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>DevOps Lab - Users</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; background: #f0f0f0; }
                h1 { color: #333; }
                table { width: 100%; border-collapse: collapse; background: white; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
                th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
                th { background-color: #4CAF50; color: white; }
                tr:hover { background-color: #f5f5f5; }
                .info { background: white; padding: 20px; margin-bottom: 20px; border-radius: 5px; }
            </style>
        </head>
        <body>
            <div class="info">
                <h1>🚀 DevOps Lab - User Management System</h1>
                <p><strong>Web Server:</strong> NGINX + FastAPI</p>
                <p><strong>Database:</strong> PostgreSQL</p>
                <p><strong>Total Users:</strong> {}</p>
            </div>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Created At</th>
                </tr>
        """.format(len(users))
        
        for user in users:
            html += f"""
                <tr>
                    <td>{user['id']}</td>
                    <td>{user['name']}</td>
                    <td>{user['email']}</td>
                    <td>{user['created_at']}</td>
                </tr>
            """
        
        html += """
            </table>
        </body>
        </html>
        """
        
        return html
        
    except Exception as e:
        return f"<h1>Ошибка выполнения запроса: {e}</h1>"

@app.get("/api/users")
async def get_users() -> List[Dict]:
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection error")
    
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM users ORDER BY id")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/users/{user_id}")
async def get_user(user_id: int) -> Dict:
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection error")
    
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        return user
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    conn = get_db_connection()
    db_status = "connected" if conn else "disconnected"
    if conn:
        conn.close()
    
    return {
        "status": "healthy",
        "database": db_status
    }