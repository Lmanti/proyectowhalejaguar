import React from 'react';
import style from './Info.module.css';

const Info = ({info}) => {
    return (
        <div className={style.container} >
            {/* Valida si hay respuesta y la renderiza */}
            {
                info && <div>
                    <h1>{info}</h1>
                </div>
            }
        </div>
    )
}

export default Info