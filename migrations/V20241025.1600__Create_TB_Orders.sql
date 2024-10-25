-- SQL Script to Create Orders Table in PostgreSQL

CREATE TABLE Orders (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
);

-- Index for faster lookup of user orders
CREATE INDEX idx_orders_user_id ON Orders (user_id);

-- Add some example data
INSERT INTO Orders (user_id) VALUES 
(1),
(2),
(3);
