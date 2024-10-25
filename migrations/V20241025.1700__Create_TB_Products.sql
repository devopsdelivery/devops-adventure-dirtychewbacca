
CREATE TABLE Products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Index for faster lookup of product name
CREATE INDEX idx_products_name ON Products (name);

-- Add some example data
INSERT INTO Products (name, price) VALUES 
('Laptop', 999.99),
('Smartphone', 699.99),
('Headphones', 199.99);
