DROP TABLE airwaves;
CREATE TABLE airwaves (
airplane_id INTEGER PRIMARY KEY,
x INTEGER,
y INTEGER,
z INTEGER,
speed INTEGER,
cardinality INTEGER);
INSERT INTO "airwaves" VALUES(1,0,10000,0,200,45);
INSERT INTO "airwaves" VALUES(2,282,10000,282,200,225);

DROP TABLE stage;
CREATE TABLE stage (
airplane_id INTEGER PRIMARY KEY,
x INTEGER,
y INTEGER,
z INTEGER);
INSERT INTO stage VALUES (1,0,0,0);
INSERT INTO stage VALUES (2,0,0,0);