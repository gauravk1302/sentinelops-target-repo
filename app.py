import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Scanner Test 1: Hardcoded dummy AWS secret (Gitleaks pakdega)
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"

@app.route("/user")
def get_user():
    user_id = request.args.get("id")
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    # Scanner Test 2: Unsanitized SQL Query / SQLi (Semgrep pakdega)
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    
    results = cursor.fetchall()
    conn.close()
    return str(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)