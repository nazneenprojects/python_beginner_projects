SELECT table_name 
FROM information_schema.tables 
WHERE table_type = 'BASE TABLE';

SELECT * FROM sys.database_principals WHERE name = CURRENT_USER;

SELECT table_name, table_schema
FROM information_schema.tables;





drop table dev.v_details



-- Create the v_details table
CREATE TABLE v_details (
    id INT PRIMARY KEY,  -- Primary key
    photo VARBINARY(MAX),  -- Photo stored as binary data (for image storage)
    history NVARCHAR(MAX)  -- History stored as JSON string
);



INSERT INTO auto_info (
    vehicle_name, vehicle_model, num_wheel, type, year, brand, price, available, reserved, count
) 
VALUES (
    'Maserati Indy', '4200', 4, 'non-ev', 1970, 'Maserati', 57500.00, 1, 1, 2
);

-- Create the v_details table
CREATE TABLE v_details (
    id INT PRIMARY KEY,  -- Primary key
    photo VARBINARY(MAX),  -- Photo stored as binary data (for image storage)
    history NVARCHAR(MAX)  -- History stored as JSON string
);


ALTER TABLE auto_info
ADD CONSTRAINT FK_auto_info_v_details
FOREIGN KEY (v_id) REFERENCES v_details(id)
ON DELETE CASCADE;




drop table auto_info




SELECT id FROM auto_info WHERE vehicle_name = 'Tesla Model 3';


INSERT INTO v_details (id, photo, history) 
VALUES (
    4,  -- Foreign key to auto_info
    NULL,
    '{
        "name": "Porsche Boxter",
        "manufactured": 2022,
        "sound_level": 45,
        "emission": 0,
        "Tech spec": {
            "engine_speed": 0.0,
            "torque": 660.0,
            "max_load": 500.0
        }
    }'  -- History as JSON data
);


select * from v_details





--drop table auto_info

select * from auto_info

select * from  v_details

ALTER TABLE auto_info ADD v_id INT ;



--delete from auto_info where id =2

----------------------  Playground ---------------------------------
SELECT * FROM [SRC].[stock_list_fmp]

SELECt count(*) from src.stock_list_fmp



SELECT * FROM [SRC].[stock_profile]

SELECt count(*) from src.stock_profile




SELECT * FROM [SRC].[ratios]

SELECt count(*) from src.ratios



SELECT * FROM [SRC].[income_statement]

SELECt count(*) from src.income_statement



SELECT * FROM [SRC].[historical_price] 

where symbol='AMD'

SELECt count(*) from src.historical_price


SELECT DISTINCT symbol FROM src.historical_price;

-----------------------------------------------------------------------------------------------

CREATE TABLE dev.users (
    id INT IDENTITY(1,1) PRIMARY KEY,       -- Auto-incrementing primary key
    username VARCHAR(255) UNIQUE NOT NULL,           -- Unique constraint on username
    full_name VARCHAR(255),                 -- Full name column
    email VARCHAR(255) UNIQUE NOT NULL,              -- Unique constraint on email
    hashed_password VARCHAR(255) NOT NULL,           -- Stores the hashed password
    disabled BIT DEFAULT 0,                 -- Boolean field, default set to false (0)
    INDEX ix_users_username (username),     -- Index on username
    INDEX ix_users_full_name (full_name),   -- Index on full name
    INDEX ix_users_email (email)            -- Index on email
);

Drop table dev.users;


INSERT INTO dbo.users (username, full_name, email, hashed_password, disabled)
VALUES ('nazneenmulani', 'Nazneen Mulani', 'nazneenmulani@example.com', '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW', 0);

INSERT INTO dbo.users (username, full_name, email, hashed_password, disabled)
VALUES ('arshads', 'Arshad Shaikh', 'arshads@example.com', '$2b$12$qRRtHkdHY5G55G.r/DFW1uYRkhhamWL.R4xRdSCNUiPeyp687XFae', 0);


select * from dbo.users

CREATE SCHEMA dev;



CREATE TABLE dbo.ev.auto_info (
    id INT IDENTITY(1,1) PRIMARY KEY,         -- Auto-incrementing primary key
    vehicle_name NVARCHAR(255) NOT NULL,      -- Vehicle name as string
    vehicle_model NVARCHAR(255) NOT NULL,     -- Vehicle model as string
    num_wheel INT NOT NULL,                   -- Number of wheels as number
    type NVARCHAR(50) CHECK (type IN ('ev', 'non-ev')),  -- Type as either 'ev' or 'non-ev'
    year INT CHECK (year >= 1886) NOT NULL,   -- Year as YYYY (vehicles from 1886 onward)
    brand NVARCHAR(255) NOT NULL,             -- Brand as string
    price DECIMAL(18, 2),                     -- Price in Euros
    available BIT DEFAULT 1,                  -- Available as bit (1 for true, 0 for false)
    reserved BIT DEFAULT 0,                   -- Reserved flag as bit (1 for true, 0 for false)
    count INT DEFAULT 1,                      -- Count of available vehicles (starts at 1)
    v_id INT,  -- Foreign key column
    CONSTRAINT FK_auto_info_v_details
    FOREIGN KEY (v_id) REFERENCES dev.v_details(id)
    ON DELETE CASCADE
);


-- Create the v_details table
CREATE TABLE dev.v_details (
    id INT IDENTITY(1,1) PRIMARY KEY,  -- Primary key
    photo VARBINARY(MAX),  -- Photo stored as binary data (for image storage)
    history NVARCHAR(MAX)  -- History stored as JSON string
);
   

      




 drop table dbo.auto_info

drop table dbo.v_details

drop table dev.users
 
 
ALTER TABLE dev.auto_info 
    ADD CONSTRAINT FK_auto_info_v_details
    FOREIGN KEY(v_id) REFERENCES dev.v_details(id)
ON DELETE CASCADE

ALTER TABLE dev.auto_info 
    DROP CONSTRAINT FK_auto_info_v_details;

select * from dev.auto_info

select * from dev.v_details


INSERT INTO dev.v_details ( photo, history)
VALUES ( 0x1234567890ABCDEF, '{"name": "VW XZ", "manufactured": "2023", "sound_level": "low", "emission": "zero", "Tech_spec": {"engine_speed": 400.0, "torque": 450.0, "max_load": 1000.0}}');

INSERT INTO dbo.auto_info (vehicle_name, vehicle_model, num_wheel, type, year, brand, price, available, reserved, count)
VALUES ('VW camper Z', 'VW XZ', 4, 'ev', 2023, 'VW', 39990.00, 1, 0, 1);

CREATE INDEX ix_users_full_name ON dev.users (full_name);