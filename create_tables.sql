CREATE TABLE IF NOT EXISTS Tech(
    techID varchar(30) NOT NULL PRIMARY KEY,
    "password" TEXT NOT NULL,
    locationZip  VARCHAR(5) NOT NULL,
    techTypeID INT NOT NULL,
    rating INT NULL,
    contactNumber VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS TechType(
    typeID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    typeName VARCHAR(30) NOT NULL,
    typeDescription TEXT NULL
);


