import express from "express";
import morgan from "morgan";
import mongoose from "mongoose";
import { usuariosRouter } from "./routes/usuarios.routes.js";

const app = express();
//https://www.npmjs.com/package/morgan
const logger = morgan("dev");

app.use(logger);
//Indica la data que va a poder aceptar y entender el API <-
app.use(express.json());

app.use(usuariosRouter);

const PORT = process.env.PORT ?? 3000
console.log(process.env.MONGO_URL);

mongoose
    .connect(process.env.MONGO_URL)
    .then((valor) => {
      console.log("Conectado a la base de datos 😎");
    })
    .catch((error) => {
      console.log("Error al conectarse a la base 😭");
    });

app.listen(PORT, () => {
    console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});




















































