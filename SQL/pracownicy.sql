CREATE TABLE premia (
    id VARCHAR(20) PRIMARY KEY,
    premia NUMERIC
);

CREATE TABLE dzialy (
    id INTEGER PRIMARY KEY,
    nazwa VARCHAR(50),
    siedziba VARCHAR(30)
);

CREATE TABLE pracownicy (
    id VARCHAR(6) PRIMARY KEY,
    nazwisko VARCHAR(50),
    imie VARCHAR(30),
    stanowisko VARCHAR(20)
    data_zatrudnienia VARCHAR(23),
    placa NUMERIC,
    premia NUMERIC,
    id_dzial INTEGER,
    FOREIGN KEY (stanowisko) REFERENCES premia(id),
    FOREIGN KEY (id_dzial) REFERENCES dzial(id)
    );
