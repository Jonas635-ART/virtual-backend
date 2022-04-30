import jsonwebtoken from "jsonwebtoken";
import { Prisma } from "../prisma";

export async function verificarToken(req, res, next) {
    //https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/split
    if(req.headers.authorization){
        return res.status(401).json({
            message: " Se necesita una token para lapeticion"
        });
    }
    try {
        const token = req.headers.authorization.split(' ')[1]
        const payload = jsonwebtoken.verify(token, process.env.JWT_SECRET);
        const usuarioEncontrado = await Prisma.usuario.findUnique({
            where: { id: payload.id },
            rejectOnNotFound:true
        });
        req.user = usuarioEncontrado;
        next();
    }
    catch(error){
        return res.status(400).json({
            message: "Token invalida",
            content: error.message
        });
    }
};





























