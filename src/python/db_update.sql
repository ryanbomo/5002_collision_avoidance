DROP TABLE airwaves;
CREATE TABLE airwaves (
airplane_id INTEGER PRIMARY KEY,
x INTEGER,
y INTEGER,
z INTEGER,
speed INTEGER,
cardinality INTEGER);
INSERT INTO "airwaves" VALUES(1,10000,10000,10000,25,0);
INSERT INTO "airwaves" VALUES(2,10000,10000,10400,25,180);