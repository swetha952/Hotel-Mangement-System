CREATE TABLE activitybooking (
    Cid INT(11),
    BookingDate DATE,
    activity VARCHAR(30),
    actcost INT(30) DEFAULT NULL
);

CREATE TABLE bill (
    Cid INT(11) NOT NULL,
    TotalBill DECIMAL(10,2) NOT NULL
);

CREATE TABLE customer (
    Cid INT(11) NOT NULL,
    Name VARCHAR(255) NOT NULL,
    phoneno VARCHAR(20) DEFAULT NULL,
    Age INT(11) DEFAULT NULL,
    BookInDate DATE NOT NULL,
    CheckOutDate DATE NOT NULL,
    PRIMARY KEY (Cid)
);
CREATE TABLE foodorder (
    Cid INT(11) NOT NULL,
    foodtype VARCHAR(30) NOT NULL,
    fprice INT(30) DEFAULT NULL
);

CREATE TABLE roombooking (
    Cid INT(11) NOT NULL,
    BookInDate DATE NOT NULL,
    CheckOutDate DATE NOT NULL,
    roomtype VARCHAR(30) DEFAULT NULL
);
