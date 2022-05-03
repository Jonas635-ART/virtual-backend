import prisma from '@prisma/client'
import jsonwebtoken from "jsonwebtoken";
import { Prisma } from "../prisma.js";

export async function verificarToken(req, res, next) {
    //https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/split
    if(!req.headers.authorization){
        return res.status(401).json({
            message: " Se necesita una token para la peticion"
        });
    }
    try {
        const token = req.headers.authorization.split(" ")[1]
        const payload = jsonwebtoken.verify(token, process.env.JWT_SECRET);
        const usuarioEncontrado = await Prisma.usuario.findUnique({
            where: { id: payload.id },
            rejectOnNotFound:true,
        });
        req.user = usuarioEncontrado;
        next();
    }
    catch(error){
        return res.status(400).json({
            message: "Token invalida",
            content: error.message,
        });
    }
};

export const validarAdmin = async (req, res, next) => {
    // se ejecutara luego del middleware de verificacion
    if (req.user.rol !== prisma.USUARIO_ROL.ADMINISTRADOR){
        return res.status(401).json({
            message:
            "El usuarios no tiene privilegios para esta operacion",
        });
    } else {
        next();
    }
};
export const validarCliente = async (req, res, next) => {
    if (req.user.rol !== prisma.USUARIO_ROL.CLIENTE){
        return res.status(401).json({
            message:
            "El usuarios no tiene privilegios para esta operacion",
        });
    } else {
        next();
    }
};



























