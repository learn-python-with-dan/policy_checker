
CREATE TABLE IF NOT EXISTS comments (
    id UUID PRIMARY KEY,
    content VARCHAR NOT NULL,
    created_at TIMESTAMP NOT NULL
);
