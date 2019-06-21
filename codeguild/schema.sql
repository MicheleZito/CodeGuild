DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS comments;

CREATE TABLE posts(
    id_post INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_surname TEXT NOT NULL,
    created DATETIME NOT NULL DEFAULT (datetime(CURRENT_TIMESTAMP, 'localtime')) ,
    subject TEXT NOT NULL,
    title TEXT NOT NULL,
    body TEXT NOT NULL
);

CREATE TABLE comments(
    id_comment INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER NOT NULL,
    comm_first_name TEXT NOT NULL,
    comm_last_surname TEXT NOT NULL,
    comm_created TIMESTAMP  NOT NULL DEFAULT (datetime(CURRENT_TIMESTAMP, 'localtime')),
    comm_body TEXT NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts (id_post)
);