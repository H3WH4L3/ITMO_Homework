import sqlite3
from flask import Flask, g, render_template, request, redirect, url_for

app = Flask(__name__)
DATABASE = "todo.db"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                description TEXT NOT NULL,
                priority INTEGER NOT NULL,
                start_date DATE NOT NULL,
                complete BOOLEAN NOT NULL CHECK (complete IN (0, 1))
            )
        """
        )
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    db = get_db()
    cur = db.execute(
        "SELECT id, task, description, priority, start_date, complete FROM tasks"
    )
    tasks = [
        {
            "id": row[0],
            "task": row[1],
            "description": row[2],
            "priority": row[3],
            "start_date": row[4],
            "complete": bool(row[5]),
        }
        for row in cur.fetchall()
    ]
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    task = request.form["task"]
    priority = int(request.form["priority"])
    description = request.form["description"]
    start_date = request.form["start_date"]
    db = get_db()
    db.execute(
        "INSERT INTO tasks (task, description, priority, start_date, complete) VALUES (?, ?, ?, ?, ?)",
        (task, description, priority, start_date, False),
    )
    db.commit()
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete(task_id):
    db = get_db()
    db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    db.commit()
    return redirect(url_for("index"))


@app.route("/complete/<int:task_id>")
def complete(task_id):
    db = get_db()
    db.execute("UPDATE tasks SET complete = NOT complete WHERE id = ?", (task_id,))
    db.commit()
    return redirect(url_for("index"))


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):
    db = get_db()
    if request.method == "POST":
        task = request.form["task"]
        description = request.form["description"]
        priority = int(request.form["priority"])
        start_date = request.form["start_date"]
        db.execute(
            "UPDATE tasks SET task = ?, description = ?, priority = ?, start_date = ? WHERE id = ?",
            (task, description, priority, start_date, task_id),
        )
        db.commit()
        return redirect(url_for("index"))
    else:
        cur = db.execute(
            "SELECT task, description, priority, start_date FROM tasks WHERE id = ?",
            (task_id,),
        )
        task_data = cur.fetchone()
        return render_template(
            "edit.html",
            task=task_data[0],
            description=task_data[1],
            priority=task_data[2],
            start_date=task_data[3],
            task_id=task_id,
        )


# ------------------------
if __name__ == "__main__":
    app.run(debug=True)
