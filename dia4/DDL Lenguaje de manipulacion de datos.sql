use prueba;
# Comentario --Comentario
INSERT INTO clientes (nombre, documento, tipo_documento, estado) VALUES
('Eduardo','34354545','DNI', true),
('Tadeo','34983745','DNI', true),
('Elena','1828122','RUC', false);
SELECT nombre, documento FROM clientes;
SELECT * FROM clientes;<
SELECT * FROM clientes WHERE documento = '1828122' AND (nombre = 'Elena' OR nombre = 'Tadeo');
SELECT * FROM clientes WHERE estado = true AND tipo_documento = 'DNI';
SELECT * FROM clientes WHERE nombre LIKE '%Ta%';

UPDATE clientes SET nombre = 'Ramiro', documento = '1212334674' WHERE id = 1 AND nombre = 'Eduardo';

SET SQL_SAFE_UPDATES = true;
DELETE FROM clientes WHERE id = 1;
SELECT * FROM clientes;



















