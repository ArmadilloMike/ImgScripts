import os
import sqlite3
from imgbyte import *


def get_credentials():
    try:
        conn = sqlite3.connect(os.path.abspath(os.path.join(os.path.dirname(__file__), 'credentials.db')))
        cursor = conn.cursor()
        cursor.execute('SELECT email, username, password FROM credentials')
        columns = [desc[0] for desc in cursor.description]
        results = cursor.fetchall()
        return [dict(zip(columns, row)) for row in results]
    except Exception as e:
        print(f"Error accessing credentials: {e}")
        return []
    finally:
        if 'conn' in locals():
            conn.close()

def upvote_post(creds, driver, vote_type, post_id):
    for cred in creds:
        email = cred['username']
        password = cred['password']
        login(driver, email, password)
        post_vote(driver, vote_type, post_id)

def upvote(image_id):
    driver = createWindow()
    creds = get_credentials()
    vote_type = 1
    upvote_post(creds, driver, vote_type, image_id)