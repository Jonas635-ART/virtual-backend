CREATE TABLE vacunas (
id INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100) UNIQUE NOT NULL,
estado BOOL DEFAULT TRUE,
fecha_vencimiento DATE,
procedencia ENUM('USA','CHINA','RUSIA','UK'),
lote VARCHAR(10)
);

CREATE TABLE vacunatorios (
 id INT PRIMARY KEY AUTO_INCREMENT,
 nombre VARCHAR(100) NOT NULL,
 latitud FLOAT,
 longitud FLOAT,
 direccion VARCHAR(200),
 horario_atencion VARCHAR(100),
 vacuna_id INT,
FOREIGN KEY (vacuna_id) REFERENCES vacunas(id)
);
ALTER TABLE vacunatorios ADD COLUMN imagen VARCHAR(100) DEFAULT 'imagen.png' AFTER horario_atencion;
ALTER TABLE vacunatorios CHANGE imagen foto VARCHAR(100) DEFAULT 'imagen.png';

DESC vacunatorios;










