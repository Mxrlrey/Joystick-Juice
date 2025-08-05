CREATE TABLE Person (
    idPerson SERIAL PRIMARY KEY,
    name VARCHAR(45),
    email VARCHAR(255),
    birthdate DATE,
    avatar_url VARCHAR(255),
    gender VARCHAR(45),
    password VARCHAR(255)
);
