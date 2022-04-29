import express, { json } from "express";
import { productosRouter } from "./routes/productos.routes.js"

const app = express();

app.use(json());

const PORT = process.env.PORT ?? 3000;

app.get('/', (req, res) => {
    res.json({
        message: "Bienvenido a mi api de minimarket"
    });
});

app.use(productosRouter);

app.listen(PORT, () => {
    console.log(`Servidor corriendo en el puerto ${PORT}`);
});

 

















