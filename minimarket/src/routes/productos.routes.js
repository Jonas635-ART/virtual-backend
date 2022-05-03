import { Router } from "express";
import { 
    crearProducto, 
    listarProductos,
    actualizarProducto,
    eliminarProducto, 
} from "../controllers/productos.controller.js";
import { validarAdmin, verificarToken } from "../utils/validador.js";

export const productosRouter = Router();

productosRouter
    .route("/productos")
    .post(crearProducto, validarAdmin, verificarToken)
    .get(listarProductos);
productosRouter
    .route("/productos/:id")
    .all(verificarToken, validarAdmin)
    .put(actualizarProducto)
    .delete(eliminarProducto);









