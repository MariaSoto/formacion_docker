-- CREATE DATABASE mydb;
-- GRANT ALL PRIVILEGES ON mydb.* TO 'myuser'@'%' IDENTIFIED BY 'mysql';
-- GRANT ALL PRIVILEGES ON mydb.* TO 'myuser'@'localhost' IDENTIFIED BY 'mysql';
USE destinations_clients
CREATE TABLE destinations_clients (
    id bigint GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    calldate  DateTime,
    uniqueid  varchar(255),
    destination  varchar(255),
    prefix  int,
    outcallerid  varchar(255),
    days_last_call  int,
    diff_seconds  Float,   
    disposition  varchar(255),
    billsec  int,
    duration  int,
    called_hangup  TINYINT,
    amd  TINYINT,
    npv  TINYINT,
    siren  int
);
INSERT INTO destinations_clients VALUES
('2023-08-10 07:17:39','tast51-1691644659.264,0033556847743',0,'+33189616983',1,56704,'ANSWERED',7,7,0,0,0,495334567),
('2023-08-10 07:17:48','tast36-1691644668.208,0033556847728',0,'+33189616983',1,73846,'NO ANSWER',0,24,0,0,0,495334567),
('2023-08-10 07:18:14','tast52-1691644694.244,0033556847709',0,'+33189616983',1,49824,'ANSWERED',6,13,0,0,0,495334567)
