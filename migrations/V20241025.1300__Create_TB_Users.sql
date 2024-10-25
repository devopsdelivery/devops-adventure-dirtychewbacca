CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

-- Index for faster lookup of email (useful for ensuring email uniqueness)
CREATE UNIQUE INDEX idx_users_email ON Users (email);

-- Add some example data
INSERT INTO Users (name, email) VALUES 
('Alice Johnson', 'alice.johnson@example.com'),
('Bob Smith', 'bob.smith@example.com'),
('Charlie Brown', 'charlie.brown@example.com');
