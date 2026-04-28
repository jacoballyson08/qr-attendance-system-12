from dotenv import load_dotenv
import os
import psycopg2
import mysql.connector

load_dotenv()

# -----------------------------
# SWITCH MODE HERE
# -----------------------------
USE_CLOUD = True  # True = Supabase, False = XAMPP


# -----------------------------
# LOCAL XAMPP CONFIG (MySQL)
# -----------------------------
LOCAL_DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "qr_attendance_db"
}


# -----------------------------
# CLOUD SUPABASE CONFIG
# -----------------------------
DATABASE_URL = os.getenv("DATABASE_URL")


# -----------------------------
# GET DATABASE CONNECTION
# -----------------------------
def get_db():

    if USE_CLOUD:
        # 🌐 CLOUD DATABASE (Supabase PostgreSQL)

        connection = psycopg2.connect(DATABASE_URL)

        return connection

    else:
        # 🏠 LOCAL DATABASE (XAMPP MySQL)

        connection = mysql.connector.connect(**LOCAL_DB_CONFIG)

        return connection
