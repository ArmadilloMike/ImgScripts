from gen_users import *
from upvote_image import *
import asyncio
import sqlite3
import csv

def db_to_csv(db_path, table_name, csv_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch all data from the specified table
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Get column names
    column_names = [description[0] for description in cursor.description]

    # Write to CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(column_names)  # Write header
        writer.writerows(rows)         # Write data

    # Clean up
    conn.close()
    print(f"✅ Exported '{table_name}' to '{csv_path}'")


async def main():
    c_or_u = input("Would you like to create users (c) or upvote an image (u)")
    if c_or_u == "c":
        users = input("How many users would you like to create? (# only)")
        user_num = int(users)
        await gen_users(user_num)
        msvc = input("Would you like to export the usernames and passwords to a csv file? (y/n)")
        if msvc == "y":
            with open("credentials.csv", "w") as file:
                pass
            db_to_csv("credentials.db","credentials", "credentials.csv")
            print(".csv file created successfully at credentials.csv")
        else:
            pass
    elif c_or_u == "u":
        image_id = str(input("What is the image id? (This part: imgflip.com/i/-> 9geor3 <-)"))
        upvote(image_id)
        print("Upvoting Successful!")
    else:
        print("Please put c or u. Close this then run it again")

if __name__ == '__main__':
    create_database()
    asyncio.run(main())