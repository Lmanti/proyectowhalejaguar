import React, { useState } from 'react';
import Info from '../Info/Info';
import style from './SearchBar.module.css'

//Valida el input
const validate = (input) => {
    let errors = {};
    //Solo se aceptarán números y espacios
    if (/(?=[^0-9\s])/.test(input.search)) errors.search = "Sólo se aceptan números y espacios!";
    return errors;
}

const SearchBar = () => {

    // Constantes
    const [input, setInput] = useState("")
    const [errors, setErrors] = useState({})
    const [info, setInfo] = useState("")

    // Maneja el input    
    const handleInput = (e) => {
        // Settea el input y lo actualiza
        setInput(e.target.value)

        // Settea los errores y los actualiza
        setErrors(validate({
            ...errors,
            [e.target.id]: e.target.value
        }))
    }

    // Maneja el submit
    const handleSubmit = (e) => {
        e.preventDefault()

        // Restricción si hay error
        if (errors.search) return

        // Fetch al back
        return fetch("http://127.0.0.1:8000/validator/", {
            method: 'POST',
            body: JSON.stringify({cardNumber: input}),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(res => res.json())
        // le asigna a info la respuesta que llega desde el back
        .then(json => setInfo(json.message))
    }


    console.log(errors.search)

    return (
        <div className={style.container} >
            {/* Renderiza el fromulario */}
            <form onSubmit={handleSubmit} className={style.form} >
                <input type="text" value={input} onChange={handleInput} id="search" className={`${style.input} ${errors.search && style.inputError}`} ></input>
                <button className={style.button} >Validar</button>
            </form>

            {/* Renderiza un error si el usuario ingresa un dato no aceptado */}
            {
                errors.search && <p className={style.error} >{errors.search}</p>
            }

            {/* Renderiza el resultado de la consulta */}
            <Info info={info} />
        </div>
    )
}

export default SearchBar;