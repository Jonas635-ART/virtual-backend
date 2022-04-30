import prisma from "@prisma/client";
import validator from "validator";

export function usuarioRequestDTO({nombre , email , password , rol}){
    //https://github.com/validatorjs/validator.js
    const errores = []
    if (!validator.isEmail(email)){
        errores.push("El email del correo no es valido");
    }
    if (validator.isEmpty(password)){
        errores.push("No puede el password estar vacio");
    }
    if (validator.isEmpty(nombre)){
        errores.push("No puede el nombre estar vacio");
    }

    if (rol !== prisma.USUARIO_ROL.ADMINISTRADOR && 
        rol !== prisma.USUARIO_ROL.CLIENTE
        ){
        errores.push(`El rol puede ser ${prisma.USUARIO_ROL.ADMINISTRADOR} o ${prisma.USUARIO_ROL.CLIENTE}`
        );
    }

    if (errores.length !=0) {
        throw Error(errores);
    } else {
        return {
            nombre,
            email,
            password,
            rol,
        };
    }
}
export function loginRequestDTO({email, password}) {
    const errores = []
    if (!validator.isEmail(email)){
        errores.push("El email del correo no es valido");
    }
    if (validator.isEmpty(password)){
        errores.push("No puede el password estar vacio");
    }

    if (errores.length !=0) {
        throw Error(errores);
    } else {
        return {
            email,
            password,
        };
    }
}














































