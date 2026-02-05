PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS files;

CREATE TABLE files
(
volume_id INTEGER NOT NULL,
file_id INTEGER NOT NULL,
name TEXT NOT NULL,
path TEXT NOT NULL,
size INTEGER,

PRIMARY KEY (volume_id, file_id)
);
