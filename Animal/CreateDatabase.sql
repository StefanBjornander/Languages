DROP DATABASE IF EXISTS vaxa;
CREATE DATABASE vaxa;
USE vaxa;

CREATE TABLE owner(id VARCHAR(6), PRIMARY KEY (id), name VARCHAR(256),
                   address VARCHAR(256), postal VARCHAR(256), phone VARCHAR(10));
INSERT INTO owner(id, name, address, postal, phone)
  VALUES("951224", "The Alpha Company", "1 Main Street", "12345 Arboga", "0123456789"),
        ("940501", "The Bravo Company", "2 Main Street", "23456 Boden","0234567890"),
        ("941226", "The Charlie Company", "3 Main Street", "34567 Chrisianstad", "0345678901"),
        ("621220", "The Delta Company", "4 Main Street", "45678 Dandereyd", "0456789012"),
        ("870614", "The Echo Company", "5 Main Street", "56789 Eskilstuna", "0567890123"),
        ("110313", "The Foxtrot Company", "6 Main Street", "67890 Fagerst", "0678901234"),
        ("280914", "The Golf Company", "7 Main Street", "78901 Grönköping","0789012345"),
        ("400617", "The Hotel Company", "8 Main Street", "89012 Hjo", "0890123467"),
        ("251227", "The India Company", "9 Main Street", "90123 Innanå", "0901234678"),
        ("330306", "The Juliet Company", "10 Main Street", "01234 Jakobsberg", "0012346789");
SELECT * FROM owner ORDER BY name;

CREATE TABLE farm(id VARCHAR(8), PRIMARY KEY (id), name VARCHAR(256),
                  address VARCHAR(256), postal VARCHAR(256), phone VARCHAR(10));
INSERT INTO farm(id, name, address, postal, phone)
  VALUES("95122491", "The Kilo Farm", "11 Main Street", "12345 Karlstad", "0123456789"),
        ("94050167", "The Lime Farm", "12 Main Street", "23456 Lindesberg","0234567890"),
        ("94122625", "The Mike Farm", "13 Main Street", "34567 Motala", "0345678901"),
        ("62122037", "The November Farm", "14 Main Street", "45678 Niklasberg", "0456789012"),
        ("87061480", "The Oscar Farm", "15 Main Street", "56789 Oskarberg", "0567890123"),
        ("11031386", "The Papa Farm", "16 Main Street", "67890 Papa Nya Guinea", "0678901234"),
        ("28091449", "The Quebec Farm", "17 Main Street", "78901 Quebec","0789012345"),
        ("40061701", "The Romeo Farm", "18 Main Street", "89012 Rogersfors", "0890123467"),
        ("25122708", "The Sierra Farm", "19 Main Street", "90123 Strängnäs", "0901234678"),
        ("33030601", "The Tango Farm", "20 Main Street", "01234 Skövde", "0012346789");
SELECT * FROM farm ORDER BY name;

CREATE TABLE ownership(owner_id VARCHAR(6), FOREIGN KEY (owner_id) REFERENCES owner(id),
                       farm_id VARCHAR(8), FOREIGN KEY (farm_id) REFERENCES farm(id));
INSERT INTO ownership(owner_id, farm_id)
  VALUES("951224", "95122491"),
        ("951224", "94050167"),
        ("251227", "40061701"),
        ("940501", "94122625"),
        ("941226", "94122625"),
        ("621220", "62122037"),
        ("870614", "62122037"),
        ("110313", "11031386"),
        ("280914", "28091449"),
        ("400617", "40061701"),
        ("251227", "25122708"),
        ("251227", "33030601");

SELECT * FROM ownership;

CREATE TABLE kind(id INT AUTO_INCREMENT, PRIMARY KEY (id), name VARCHAR(10));
INSERT INTO kind(name) VALUES("Cow"),("Bull"),("Calf"),("Heifer");
SELECT * from kind;

CREATE TABLE animal(animal_id VARCHAR(10), PRIMARY KEY (animal_id),
                    kind_id INT, FOREIGN KEY (kind_id) REFERENCES kind(id),
                    name VARCHAR(256),
                    farm_id VARCHAR(8), FOREIGN KEY (farm_id) REFERENCES farm(id));
INSERT INTO animal(animal_id, kind_id, name, farm_id)
  VALUES("9512249112", (SELECT id FROM kind WHERE name = "Cow"), "Rosa", "95122491"),
        ("9405016750", (SELECT id FROM kind WHERE name = "Calf"), "Junior", "94050167"),
        ("2512270824", (SELECT id FROM kind WHERE name = "Bull"), "Senior", "94050167"),
        ("3303060101", (SELECT id FROM kind WHERE name = "Calf"), "Kid", "94122625"),
        ("9412262587", (SELECT id FROM kind WHERE name = "Bull"), "Jack", "94122625"),
        ("6212203738", (SELECT id FROM kind WHERE name = "Heifer"), "Flower", "62122037");
SELECT animal.animal_id, kind.name AS "kind", animal.name, animal.farm_id FROM animal
  INNER JOIN kind ON animal.kind_id = kind.id;
