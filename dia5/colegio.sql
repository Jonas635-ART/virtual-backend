SELECT *
FROM ALUMNOS where CORREO LIKE '%@gmail.com';
SELECT *
FROM alumnos INNER JOIN alumnos_niveles on alumnos.id = alumnos_niveles.alumnos_id 
WHERE fecha_cursada = 2002;
SELECT * 
FROM niveles WHERE ubicacion IN('Sotano', 'Segundo Piso');
SELECT seccion, nombre
FROM niveles INNER JOIN alumnos_niveles ON niveles.id = alumnos_niveles.nivel_id
WHERE fecha_cursada = 2003;
