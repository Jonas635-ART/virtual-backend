import bcryptjs from "bcryptjs";
import {Usuario} from "../models/usuarios.models.js"

export const registrarUsuario = async (req, res) => {
    const data = req.body
    try {
        //
    const nuevoUsuario = await Usuario.create(data);

    console.log(nuevoUsuario.toJSON());
    console.log(Object.keys(nuevoUsuario));

    const result = nuevoUsuario.toJSON();
    delete result["password"];

    delete nuevoUsuario["_doc"]["password"];

    return res.status(201).json({
        message: "Usuario creado exitosamente😁",
        content: result, // nuevoUsuario,
    });
    } catch (e) {
        return res.status(400).json({
            message:"Error al crear el usuario😫",
            content: e.message,
        });
    }
};
export const login = async (req, res) => {
    // validar que se envie la pwd y el correo
    const data = req.body;
    // primero busco el usuario en la bd
    const usuarioEncontrado = await Usuario.findOne({ correo: data.correo });
  
    if (!usuarioEncontrado) {
      return res.status(400).json({
        message: "Credenciales incorrectas",
      });
    }
    // valido su pwd
    if (bcryptjs.compareSync(data.password, usuarioEncontrado.password)) {
      return res.json({
        message: "Bienvenido",
      });
    } else {
      return res.status(400).json({
        message: "Credenciales incorrectas",
      });
    }
  };




















































