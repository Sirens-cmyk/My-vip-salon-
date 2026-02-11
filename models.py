from database import get_connection

def add_user(chat_id, full_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR IGNORE INTO users (chat_id, full_name) VALUES (?, ?)",
        (chat_id, full_name)
    )
    conn.commit()
    conn.close()

def update_phone(chat_id, phone):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET phone=? WHERE chat_id=?",
        (phone, chat_id)
    )
    conn.commit()
    conn.close()

def create_booking(chat_id, barber, date, time):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE chat_id=?", (chat_id,))
    user = cursor.fetchone()

    if not user:
        return False

    cursor.execute("""
        INSERT INTO bookings (user_id, barber, date, time)
        VALUES (?, ?, ?, ?)
    """, (user["id"], barber, date, time))

    conn.commit()
    conn.close()
    return True
