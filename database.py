import os
import psycopg2
import mysql.connector


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

        conn = psycopg2.connect(DATABASE_URL)

        return conn

    else:
        # 🏠 LOCAL DATABASE (XAMPP MySQL)

        conn = mysql.connector.connect(**LOCAL_DB_CONFIG)

        return conn