DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS destinations;
DROP TABLE IF EXISTS attractions; 

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    region VARCHAR(255)
);

CREATE TABLE destinations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);

CREATE TABLE attractions (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255),
    description VARCHAR(255),
    destination_id INT REFERENCES destinations(id) ON DELETE CASCADE,
    date VARCHAR(255),
    visited BOOLEAN
);