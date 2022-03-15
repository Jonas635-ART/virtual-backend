#JOINS
USE prueba;
SELECT * 
FROM VACUNATORIOS INNER JOIN VACUNAS ON VACUNATORIOS.vacuna_id = VACUNAS.id;
-- WHERE vacuna_id = 1 ;

SELECT *
FROM VACUNATORIOS LEFT JOIN VACUNAS ON VACUNATORIOS.vacuna_id = VACUNAS.id;

SELECT *
FROM VACUNATORIOS RIGHT JOIN VACUNAS ON VACUNATORIOS.vacuna_id = VACUNAS.id;
INSERT INTO vacunatorios (nombre, latitud, longitud, direccionj, horario_atencion, foto, vacuna_id) VALUES
           ('POSTA JOSE GALVEZ', 14.26598, 32.2569, 'AV. EL SOL 755', 'LUN-VIE 15:00 22:00', null, null);
           
SELECT *
FROM VACUNATORIOS LEFT JOIN VACUNAS ON VACUNATORIOS.vacuna_id = VACUNAS.id UNION           
SELECT *                            
FROM VACUNATORIOS RIGHT JOIN VACUNAS ON VACUNATORIOS.vacuna_id = VACUNAS.id;


SELECT vacu.nombre, vac.nombre
FROM VACUNATORIOS AS vac JOIN vacunas AS vacu ON vac.vacuna_id = vacu.id
WHERE vacu.nombre = 'Pfizer';

SELECT *
FROM VACUNATORIOS JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE vacunas.nombre='SINOPHARM' AND horario_atencion LIKE '%LUN-VIE%';

SELECT vacunas.nombre
FROM VACUNATORIOS JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE latitud > -5 AND latitud < 10 ;

SELECT procedencia, vacunas.nombre
FROM vacunatorios RIGHT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE vacuna_id IS NULL;
































