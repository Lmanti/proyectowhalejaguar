import React from 'react';

const Info = ({info}) => {
    return (
        <div>
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