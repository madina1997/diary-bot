import sys
import sqlite3


CREATE_CHATS_TABLE_SQL = """
CREATE TABLE chats (
    id VARCHAR(128) PRIMARY KEY,
    created_at TEXT,
    frequency VARCHAR(16),
    language VARCHAR(16),
    tips_id INT)
"""


CREATE_QUIZES_TABLE_SQL = """
CREATE TABLE quizes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chat_id VARCHAR(128),
    created_at TEXT,
    type VARCHAR(10),
    question_number INT,
    is_selfesteem_high INT,
    is_positive INT,
    FOREIGN KEY (chat_id) REFERENCES chats (id)
    ON DELETE CASCADE ON UPDATE NO ACTION)
"""

CREATE_ANSWERS_TABLE_SQL = """
CREATE TABLE answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quiz_id UNSIGNED BIG INT,
    question_number INT,
    answer INT,
    FOREIGN KEY (quiz_id) REFERENCES quizes (id)
    ON DELETE CASCADE ON UPDATE NO ACTION)
"""

CREATE_POSITIVE_DATALOG_TABLE_SQL ="""
CREATE TABLE positive_datalog(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    chat_id VARCHAR(128),
    created_at TEXT,
    good_event TEXT,
    emotion TEXT,
    meaning TEXT)
"""

def create_database(db_name):
    conn = sqlite3.connect(db_name)
    conn.execute(CREATE_CHATS_TABLE_SQL)
    conn.execute(CREATE_QUIZES_TABLE_SQL)
    conn.execute(CREATE_ANSWERS_TABLE_SQL)
    conn.execute(CREATE_POSITIVE_DATALOG_TABLE_SQL)


if __name__ == '__main__':
    create_database(sys.argv[1])
