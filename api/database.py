import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Definieer de naam van je SQLite-databasebestand
DATABASE_NAME = "voetbal.db"
SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlitedb/voetbal.db"


def create_database():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Maak tabellen voor teams en scores als deze nog niet bestaan
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS teams (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY,
                match_id INTEGER,
                team_id INTEGER,
                score INTEGER
            )
        """)

        conn.commit()
        conn.close()
        print(f"Database {DATABASE_NAME} is aangemaakt of bestaat al.")
    except Exception as e:
        print(f"Fout bij het maken van de database: {str(e)}")


def connect_to_database():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        return conn
    except Exception as e:
        print(f"Fout bij het verbinden met de database: {str(e)}")
        return None


def close_database(connection):
    if connection:
        connection.close()
        print(f"Databaseverbinding is gesloten.")


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

if __name__ == "__main__":
    create_database()

