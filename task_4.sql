-- task_4.sql

-- Create a new table
CREATE TABLE IF NOT EXISTS mytable (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255)
);

-- Insert some data into the table
INSERT INTO mytable (id, name, email) VALUES
  (1, 'John Doe', 'john@example.com'),
  (2, 'Jane Doe', 'jane@example.com'),
  (3, 'Bob Smith', 'bob@example.com');

-- Select all data from the table
SELECT * FROM mytable;

-- Update a row in the table
UPDATE mytable SET name = 'John Smith' WHERE id = 1;

-- Delete a row from the table
DELETE FROM mytable WHERE id = 2;