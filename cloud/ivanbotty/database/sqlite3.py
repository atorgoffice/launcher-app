import sqlite3
import os

# Path to the SQLite database
DB_PATH = os.path.expanduser("~/.config/cloud.ivanbotty.Launcher/settings.db")

def init_db():
    """
    Initializes the database and creates tables if they do not exist.
    """
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Table for user preferences
    c.execute("""
        CREATE TABLE IF NOT EXISTS preferences (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)
    # Table for installed extensions
    c.execute("""
        CREATE TABLE IF NOT EXISTS extensions (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            enabled BOOLEAN
        )
    """)
    # Table for API keys of external services
    c.execute("""
        CREATE TABLE IF NOT EXISTS api_keys (
            service TEXT PRIMARY KEY,
            key TEXT
        )
    """)
    conn.commit()
    conn.close()

# ----- Preferences -----
def set_pref(key, value):
    """
    Sets a preference (key, value) in the database.
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("REPLACE INTO preferences (key, value) VALUES (?, ?)", (key, str(value)))
    conn.commit()
    conn.close()

def get_pref(key, default=None):
    """
    Retrieves the value of a preference. Returns 'default' if not found.
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT value FROM preferences WHERE key=?", (key,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else default

# ----- Extensions -----
def set_extension_enabled(ext_id, enabled: bool):
    """
    Enables or disables an extension. If it does not exist, creates it with name equal to id.
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Retrieve the extension name if already present
    c.execute("SELECT name FROM extensions WHERE id=?", (ext_id,))
    row = c.fetchone()
    name = row[0] if row else ext_id  # Use ext_id as name if not found
    c.execute("REPLACE INTO extensions (id, name, enabled) VALUES (?, ?, ?)", (ext_id, name, int(enabled)))
    conn.commit()
    conn.close()

def get_extensions():
    """
    Returns a dictionary with extension id and enabled/disabled state.
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, enabled FROM extensions")
    result = {row[0]: (row[1] == 1) for row in c.fetchall()}
    conn.close()
    return result

# ----- API Keys -----
def set_api_key(service, key):
    """
    Saves the API key for a service.
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("REPLACE INTO api_keys (service, key) VALUES (?, ?)", (service, key))
    conn.commit()
    conn.close()

def get_api_key(service):
    """
    Retrieves the API key for a service. Returns None if not found.
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT key FROM api_keys WHERE service=?", (service,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else None
