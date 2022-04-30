import {Prisma} from "../prisma.js";
import { usuarioRequestDTO, loginRequestDTO } from "../dtos/usuarios.dto.js"
import { hashSync, compareSync } from 'bcrypt';
import jsonwebtoken from "jsonwebtoken";
import { enviarCorreoValidacion } from "../utils/sendMail.js";


export const crearUsuario = async (req, res) => {
    try {
            const data = usuarioRequestDTO(req.body)
        const password = hashSync(data.password,10)

        const nuevoUsuario = await Prisma.usuario.create({
            data: { ...data, password },
            select: {
                id: true,
                nombre: true,
                email: true,
                rol: true,
                validado: true,
            } ,
        });
        await enviarCorreoValidacion({
            destinatario: nuevoUsuario.email,
            hash: "123123123",
          });

        return res.status(201).json(nuevoUsuario);

    } catch (error) {

    if (error instanceof Error){
        return res.status(400).json({
            message: "Error al crear el usuario",
            content: error.message,
        });
    }

    }
};

export const login = async (req, res) => {
    try {
        const data = loginRequestDTO(req.body)
        const usuarioEncontrado = await Prisma.usuario.findUnique({
            where: { email: data.email },
            rejectOnNotFound:true
        });

        if (compareSync(data.password, usuarioEncontrado.password)) {
            const token = jsonwebtoken.sign({
                id: usuarioEncontrado.id, 
                mensaje:"Api de minimarket",
            }, 
            'llave_secreta',
            {expiresIn: "1y"}
            );
            // el expiresIn recibe un numero (sera expresado en segundo) y si le pasamos un string:
      // '10' > 10 milisegundos
      // '1 days' > 1 dia
      // '1y' > 1 año
      // '7d' > 7 dias
            return res.json({
                message: "Bienvenido",
                content: token,
            });
        } else {
            throw new Error("Credenciales incorrectas");
        }

    } catch (error){
        if (error instanceof Error) {
        return res.status(400).json({
            message: "Error al hacer el inicio de sesion",
            content: error.message,
        });
        }
    }
}


















































