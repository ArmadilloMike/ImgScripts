import asyncio
import sqlite3
from pydoll.browser import Chrome
from pydoll.browser.options import ChromiumOptions
from faker import Faker

def create_database():
    conn = sqlite3.connect('credentials.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_credentials(email, username, password):
    conn = sqlite3.connect('credentials.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO credentials (email, username, password)
        VALUES (?, ?, ?)
    ''', (email, username, password))
    conn.commit()
    conn.close()

async def gen_users(amount):
    options = ChromiumOptions()
    options.add_argument('--window-size=1280,800')
    options.add_argument('--disable-dev-shm-usage')  # Added to prevent shared memory issues
    options.add_argument('--no-sandbox')  # Added for better stability
    fake = Faker()

    # Create database and table if they don't exist
    create_database()

    browser = None
    try:
        browser = Chrome(options=options)
        for i in range(int(amount)):
            tab = await browser.start()
            await tab.go_to('https://imgflip.com/signup')

            email_input = await tab.find_or_wait_element('css', 'input[name="email"]')
            await email_input.click()
            email = '.'.join(fake.words(3)) + "@armadillomike.dev"
            await email_input.type_text(email)

            user_input = await tab.find_or_wait_element('css', 'input.login-user[name="user"]')
            await user_input.click()
            username = '_'.join(fake.words(4))
            await user_input.type_text(str(username))

            pass_input = await tab.find_or_wait_element('css', 'input.login-pass[name="pass"]')
            await pass_input.click()
            password = fake.password()
            await pass_input.type_text(password)

            pass_again_input = await tab.find_or_wait_element('css', 'input.login-pass-again[type="password"]')
            await pass_again_input.click()
            await pass_again_input.type_text(password)

            accept_terms_btn = await tab.find_or_wait_element('css', 'button.signup-accept-terms')
            await accept_terms_btn.click()

            signup_btn = await tab.find_or_wait_element('css', 'button.login-btn')
            await signup_btn.click()

            save_credentials(email, username, password)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise
    finally:
        if browser:
            await browser.stop()
            # Add a small delay to ensure proper cleanup
            await asyncio.sleep(1)