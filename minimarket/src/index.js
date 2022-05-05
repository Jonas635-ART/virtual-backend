import express, { json } from "express";
import { detallePedidoRouter } from "./routes/detalle-pedido.routes.js";
import { productosRouter } from "./routes/productos.routes.js"
import { usuarioRouter } from "./routes/usuarios.routes.js"
import { pedidosRouter } from "./routes/pedidos.routes.js";
import { pagosRouter } from "./routes/pagos.routes.js";

import mercadopago from "mercadopago";

const app = express();

// configuro las credenciales que van a servir para hacer la pasarela de pagos
// integrator_id > es el id del desarrollador que esta haciendo esta integracion (servira para que MP nos de bonificaciones a cambio de la integracion)
// access_token > es la token que se creara al generar una nueva integracion y sera la encargada de cuando se pague algo ese dinero sea redirigido a la cuenta de la empresa
mercadopago.configure({
    access_token: process.env.MP_ACCESS_TOKEN,
    integrator_id: process.env.MP_INTEGRATOR_ID,
  });

app.use(json());

const PORT = process.env.PORT ?? 3000;

app.get('/', (req, res) => {
    res.json({
        message: "Bienvenido a mi api de minimarket"
    });
});

app.use(productosRouter);
app.use(usuarioRouter);
app.use(pedidosRouter);
app.use(detallePedidoRouter);
app.use(pagosRouter);

app.listen(PORT, () => {
    console.log(`Servidor corriendo en el puerto ${PORT}`);
});

 

















