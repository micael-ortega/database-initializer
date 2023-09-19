CREATE TABLE IF NOT EXISTS task
(id INTEGER PRIMARY KEY,
description TEXT NOT NULL,
created_at TEXT NOT NULL,
status INTEGER NOT NULL,
user_id INTEGER NOT NULL,
FOREIGN KEY(user_id) REFERENCES user(id)
);

CREATE TABLE IF NOT EXISTS user
(id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
password TEXT NOT NULL,
created_at TEXT NOT NULL,
token TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS test
(id INTEGER PRIMARY KEY,
value INTEGER NOT NULL
);
