document.addEventListener("DOMContentLoaded", () => {
    const festivalFotosInicio = document.querySelectorAll('.festival-foto-inicio');

    festivalFotosInicio.forEach(foto => {
        foto.addEventListener('mouseenter', () => {
            // Mostrar el texto oculto con efecto de cortina
            const textoOculto = foto.querySelector('.texto-oculto');
            if (textoOculto) {
                textoOculto.classList.add('visible'); // Añade la clase para activar la animación
            }
        });

        foto.addEventListener('mouseleave', () => {
            // Ocultar el texto oculto
            const textoOculto = foto.querySelector('.texto-oculto');
            if (textoOculto) {
                textoOculto.classList.remove('visible'); // Quita la clase para ocultarlo
            }
        });
    });
});