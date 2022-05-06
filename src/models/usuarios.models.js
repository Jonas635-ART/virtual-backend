import mongoose from "mongoose";
// Toda esta configuracion que estamos haciendo es solamente a nivel de mongoose
const usuarioSchema = new mongoose.Schema({
    correo: {
        type: mongoose.Schema.Types.String,
        required: true, // para que si o si me pase el valor de esta columna
        unique: true, // el correo no se va a poder repetir en esta coleccion

        lowercase: true,
        maxlength: 100,
    },
    nombre: mongoose.Schema.Types.String,
    
    telefono: {
        type: mongoose.Schema.Types.Number,
        required: false,
    },
    password: {
        type: mongoose.Schema.Types.String,
        set: (valorActual) => {
            console.log(valorActual); 
            return "hola";
        },
    },
});

export const Usuario = mongoose.model("usuarios", usuarioSchema);














































