import sqlite3
import os

currentWorkingDirectory = os.getcwd()



dbLink = currentWorkingDirectory + "/data.db"
###
insertTable = { "LifeGoals": "(title, description, objectives, colour, picture)",
                "Goals": "(title, description, objectives, colour, lifeGoalId)",
                "Projects": "(title, description, objectives, goalId)",
                "WorkTasks": "(title, objectives, projectId, order)",
                "ScheduledTasks": "(title, objectives, timeSet, deadline, length)",
                "RoutineTasks": "(title, colour, timeOfDay, reoccourance, length)",
                "Messages": "(timeStamp, message, about)",
                "Rules": "(title, lastBroken, order)"
        }
###

def setup():
    conn = sqlite3.connect(dbLink)
    cur = conn.cursor()

    # Project Manager
    cur.execute("""
        CREATE TABLE IF NOT EXISTS LifeGoals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            objectives TEXT NOT NULL,
            colour TEXT NOT NULL,
            picture TEXT NOT NULL,
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            objectives TEXT NOT NULL,
            colour TEXT NOT NULL,
            lifeGoalId INT NOT NULL,
            status INT DEFAULT 0 NOT NULL 
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            objectives TEXT NOT NULL,
            goalId INT NOT NULL,
            status INT DEFAULT 0 NOT NULL 
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS WorkTasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            objectives TEXT NOT NULL,
            projectId INT NOT NULL,
            order INT NOT NULL,
            status INT DEFAULT 0 NOT NULL 
        )
    """)
    # Day Organiser
    cur.execute("""
        CREATE TABLE IF NOT EXISTS RoutineTasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            colour TEXT NOT NULL,
            timeOfDay TEXT NOT NULL,
            reoccourance TEXT NOT NULL,
            length INT NOT NULL,
            status INT DEFAULT 0 NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS ScheduledTasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            objectives TEXT NOT NULL,
            timeSet TEXT DEFAULT NULL,
            deadline TEXT NOT NULL,
            length INT NOT NULL,
            status INT DEFAULT 0 NOT NULL
        )
    """)
    # Review System 
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timeStamp TEXT NOT NULL,
            message TEXT NOT NULL,
            about TEXT NOT NULL,
        )
    """)
    # Rule System
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            lastBroken TEXT NOT NULL,
            order INT NOT NULL
        )
    """)


    conn.commit()
    conn.close()

    
def select(table: str, fields : str = "*", orderBy = "id", asc = True, wierdConditions=None, **conditions):
    conn = sqlite3.connect(dbLink)
    cur = conn.cursor()
    if wierdConditions is not None or conditions:
        where = f"WHERE {' AND '.join([cond + ' = ?' for cond in conditions] + ([wierdConditions[0]] if wierdConditions is not None else []))}"
    else:
        where = ""
       
    data = cur.execute(f"""
            SELECT {fields}
            FROM {table}
            {where}
            ORDER BY {orderBy} {('ASC' if asc else 'DESC')}
            """, tuple([conditions[cond] for cond in conditions]+[x for x in (wierdConditions[1] if wierdConditions is not None else [])])).fetchall()

    conn.commit()
    conn.close()
    return data



def update(table: str, rowId: int, **changes):
    conn = sqlite3.connect(dbLink)
    cur = conn.cursor()

    cur.execute(f"""
            UPDATE {table}
            SET {', '.join([chan + ' = ?' for chan in changes])}
            WHERE id = {rowId}
                """, tuple([changes[chan] for chan in changes]))

    conn.commit()
    conn.close()


def insert(table: str, data: tuple):
    conn = sqlite3.connect(dbLink)
    cur = conn.cursor()

    cur.execute(f"""
            INSERT INTO {table} {insertTable[table]}
            VALUES {'(' + ', '.join(['?']*len(data)) + ')'}
                """, data)

    conn.commit()
    conn.close()


def delete(table: str, rowId: int):
    conn = sqlite3.connect(dbLink)
    cur = conn.cursor()

    cur.execute(f"""
            DELETE FROM {table}
            WHERE id = {rowId}
                """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    pass
