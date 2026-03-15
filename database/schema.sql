CREATE TABLE IF NOT EXISTS properties (

property_id TEXT PRIMARY KEY,
owner TEXT,
location TEXT

);

CREATE TABLE IF NOT EXISTS blocks (

block_index INTEGER,
timestamp REAL,
transaction_data TEXT,
previous_hash TEXT,
hash TEXT

);