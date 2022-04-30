import {Prisma} from "../prisma.js";
import { usuarioRequestDTO, loginRequestDTO,  } from "../dtos/usuarios.dto.js"
import { hashSync, compareSync } from 'bcrypt';
import jsonwebtoken from "jsonwebtoken";
import { enviarCorreoValidacion } from "../utils/sendMail.js";
import cryptojs from "crypto-js";


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
        const hash = cryptojs.AES.encrypt(JSON.stringify({
            nombre: nuevoUsuario.nombre, 
            email: nuevoUsuario.email }),
        process.env.LLAVE_ENCRIPTACION,
        ).toString();

        await enviarCorreoValidacion({
            destinatario: nuevoUsuario.email,
            hash,
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
};

export const confirmarCuenta = async (req, res) => {
    try {
        const data = req.body;
        const informacion = JSON.parse(cryptojs.AES.decrypt(
            data.hash,
            process.env.LLAVE_ENCRIPTACION
        ).toString(cryptojs.enc.Utf8));

        console.log(informacion)
        
        const usuarioEncontrado = await Prisma.usuario.findFirst({
            where: {
                email: informacion.email, 
                validado:false},
            select:{ id:true
            },
        });
        if(!usuarioEncontrado){
            throw new Error("El usuario ya fue validado");
        }
        await Prisma.usuario.update({
            where: { id: usuarioEncontrado.id },
            data: { validado: true },
        });

        return res.json({
            message: "Cuenta validada exitosamente"
        });
    } catch(error){
        if(error instanceof Error){
            return res.status(400).json({
                message: "Error al validar la cuenta.",
                content: error.message,
            });
        }

    }
};
















































