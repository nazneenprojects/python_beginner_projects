SELECT table_name 
FROM information_schema.tables 
WHERE table_type = 'BASE TABLE';

SELECT * FROM sys.database_principals WHERE name = CURRENT_USER;

SELECT table_name, table_schema
FROM information_schema.tables;


CREATE TABLE users (
    id INT IDENTITY(1,1) PRIMARY KEY,       -- Auto-incrementing primary key
    username VARCHAR(255) UNIQUE,           -- Unique constraint on username
    full_name VARCHAR(255),                 -- Full name column
    email VARCHAR(255) UNIQUE,              -- Unique constraint on email
    hashed_password VARCHAR(255),           -- Stores the hashed password
    disabled BIT DEFAULT 0,                 -- Boolean field, default set to false (0)
    INDEX ix_users_username (username),     -- Index on username
    INDEX ix_users_full_name (full_name),   -- Index on full name
    INDEX ix_users_email (email)            -- Index on email
);


INSERT INTO users (username, full_name, email, hashed_password, disabled)
VALUES ('nazneenmulani', 'Nazneen Mulani', 'nazneenmulani@example.com', '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW', 0);

select * from users


CREATE TABLE auto_info (
    id INT IDENTITY(1,1) PRIMARY KEY,        -- Auto-incrementing primary key
    vehicle_name NVARCHAR(255),              -- Vehicle name as string
    vehicle_model NVARCHAR(255),             -- Vehicle model as string
    num_wheel INT,                           -- Number of wheels as number
    type NVARCHAR(50) CHECK (type IN ('ev', 'non-ev')),  -- Type as either 'ev' or 'non-ev'
    year INT CHECK (year >= 1886),           -- Year as YYYY (vehicles from 1886 onward)
    brand NVARCHAR(255),                     -- Brand as string
    price DECIMAL(18, 2),                    -- Price in Euros
    available BIT DEFAULT 1,                 -- Available as bit (1 for true, 0 for false)
    reserved BIT DEFAULT 0,                  -- Reserved flag as bit (1 for true, 0 for false)
    count INT DEFAULT 0                      -- Count of available vehicles
);

INSERT INTO auto_info (
    vehicle_name, vehicle_model, num_wheel, type, year, brand, price, available, reserved, count
) 
VALUES (
    'Maserati Indy', '4200', 4, 'non-ev', 1970, 'Maserati', 57500.00, 1, 1, 2
);


--drop table auto_info

select * from auto_info

--delete from auto_info where id =2



