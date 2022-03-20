DROP DATABASE IF EXISTS vaxa;
CREATE DATABASE vaxa;
USE vaxa;

CREATE TABLE owner(orgnum VARCHAR(10), PRIMARY KEY (orgnum),
                   name VARCHAR(256), address VARCHAR(256), postal VARCHAR(256), phone VARCHAR(10));
INSERT INTO owner(orgnum, name, address, postal, phone)
            VALUES("951224", "The Alpha Company", "1 Main Street", "64542 Strängnäs", "0123456789"),
                  ("940501", "The Bravo Company", "2 Main Street", "64542 Strängnäs","0234567890"),
                  ("941226", "The Charlie Company", "3 Main Street", "64542 Strängnäs", "0345678901"),
                  ("621220", "The Delta Company", "4 Main Street", "64542 Strängnäs", "0456789012"),
                  ("870614", "The Echo Company", "5 Main Street", "64542 Strängnäs", "0567890123"),
                  ("110313", "The Foxtrot Company", "6 Main Street", "64542 Strängnäs", "0678901234"),
                  ("280914", "The Golf Company", "7 Main Street", "64542 Strängnäs","0789012345"),
                  ("400617", "The Hotel Company", "8 Main Street", "64542 Strängnäs", "0890123467"),
                  ("251227", "The India Company", "9 Main Street", "64542 Strängnäs", "0901234678"),
                  ("330306", "The Juliet Company", "10 Main Street", "64542 Strängnäs", "0012346789");
SELECT * FROM owner ORDER BY name;

CREATE TABLE farm(prodnum VARCHAR(8), PRIMARY KEY (prodnum),
                  name VARCHAR(256), address VARCHAR(256), postal VARCHAR(256), phone VARCHAR(10));
INSERT INTO farm(prodnum, name, address, postal, phone)
            VALUES("95122491", "The Kilo Farm", "1 Main Street", "64542 Strängnäs", "0123456789"),
                  ("94050167", "The Lime Farm", "2 Main Street", "64542 Strängnäs","0234567890"),
                  ("94122625", "The Mike Farm", "3 Main Street", "64542 Strängnäs", "0345678901"),
                  ("62122037", "The November Farm", "4 Main Street", "64542 Strängnäs", "0456789012"),
                  ("87061480", "The Oscar Farm", "5 Main Street", "64542 Strängnäs", "0567890123"),
                  ("11031386", "The Papa Farm", "6 Main Street", "64542 Strängnäs", "0678901234"),
                  ("28091449", "The Quebec Farm", "7 Main Street", "64542 Strängnäs","0789012345"),
                  ("40061701", "The Romeo Farm", "8 Main Street", "64542 Strängnäs", "0890123467"),
                  ("25122708", "The Sierra Farm", "9 Main Street", "64542 Strängnäs", "0901234678"),
                  ("33030601", "The Tango Farm", "10 Main Street", "64542 Strängnäs", "0012346789");
SELECT * FROM farm ORDER BY name;

CREATE TABLE ownership(orgnum VARCHAR(6), FOREIGN KEY (orgnum) REFERENCES owner(orgnum),
                       prodnum VARCHAR(8), FOREIGN KEY (prodnum) REFERENCES farm(prodnum));
INSERT INTO ownership(orgnum, prodnum)
            VALUES("951224", "95122491"),
                  ("951224", "94050167"),
                  ("940501", "94122625"),
                  ("941226", "94122625"),
                  ("621220", "62122037"),
                  ("870614", "87061480");

SELECT * FROM farm
  INNER JOIN ownership ON (ownership.orgnum = "94050167") AND
                          (ownership.prodnum = farm.prodnum) AND
                          

CREATE TABLE kind(kindid INT AUTO_INCREMENT, PRIMARY KEY (kindid), name VARCHAR(10));
INSERT INTO kind(name) VALUES("Cow"),("Bull"),("Calf"),("Heifer");
SELECT * from kind;

CREATE TABLE animal(animalid VARCHAR(10), PRIMARY KEY (animalid),
                    kindid INT, FOREIGN KEY (kindid) REFERENCES kind(kindid),
                    name VARCHAR(256));
INSERT INTO animal(animalid, kindid, name)
            VALUES("9512249112", (SELECT kindid FROM kind WHERE name = "Cow"), "Rosa"),
                  ("9405016750", (SELECT kindid FROM kind WHERE name = "Calf"), "Junior"),
                  ("9412262587", (SELECT kindid FROM kind WHERE name = "Bull"), "Jack"),
                  ("6212203738", (SELECT kindid FROM kind WHERE name = "Heifer"), "Flower");
SELECT animal.animalid, kind.name AS "kind", animal.name FROM animal
INNER JOIN kind ON animal.kindid = kind.kindid;
