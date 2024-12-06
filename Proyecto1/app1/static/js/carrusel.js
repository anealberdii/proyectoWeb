document.addEventListener('DOMContentLoaded', function () {
    // Código para el carrusel
    const carrusel = document.querySelector('.carrusel');
    const items = document.querySelectorAll('.carrusel-item');
    const prevButton = document.querySelector('.carrusel-button.prev');
    const nextButton = document.querySelector('.carrusel-button.next');
    const itemsToShow = 3; // Mostrar 3 elementos por vez
    const totalItems = items.length;
    let index = 0;

    function updateCarrusel() {
        const itemWidth = items[0].getBoundingClientRect().width; // Ancho exacto del item
        carrusel.style.transform = `translateX(-${index * itemWidth}px)`;

        // Rehabilitar la transición para el loop al final
        carrusel.style.transition = 'transform 0.5s ease-in-out';

        // Si estamos al final del carrusel
        if (index >= totalItems - itemsToShow) {
            setTimeout(() => {
                carrusel.style.transition = 'none'; // Deshabilitar transición para el salto inmediato
                index = 0; // Reiniciar al inicio
                carrusel.style.transform = 'translateX(0)';
            }, 500); // Tiempo igual al de la animación
        }
    }

    nextButton.addEventListener('click', () => {
        if (index < totalItems - itemsToShow) {
            index++; // Avanzar
        }
        updateCarrusel();
    });

    prevButton.addEventListener('click', () => {
        if (index > 0) {
            index--; // Retroceder
        } else {
            index = totalItems - itemsToShow; // Ir al final en caso de retroceso desde el inicio
            carrusel.style.transition = 'none'; // Deshabilitar animación
            const itemWidth = items[0].getBoundingClientRect().width;
            carrusel.style.transform = `translateX(-${index * itemWidth}px)`;
            setTimeout(() => carrusel.style.transition = 'transform 0.5s ease-in-out', 50); // Rehabilitar animación
        }
        updateCarrusel();
    });

    // Auto-scroll continuo
    setInterval(() => {
        if (index < totalItems - itemsToShow) {
            index++; // Avanza
        }
        updateCarrusel();
    }, 3000); // Cada 3 segundos


    // Bloque que chequea la cantidad de entradas disponibles
    const entradasDisponiblesElement = document.getElementById('entradas-disponibles');
    const entradasDisponibles = parseInt(entradasDisponiblesElement.getAttribute('data-entradas'));
    const comprarBtn = document.getElementById('comprar-btn');

    if (entradasDisponibles === 0) {
        // Cambiar el texto del botón y su estilo
        comprarBtn.textContent = 'Agotado';
        comprarBtn.classList.add('agotado-btn'); // Clase CSS para el estilo gris
        comprarBtn.disabled = true; // Deshabilitar el botón
    } else if (entradasDisponibles <= 10 && entradasDisponibles>0) {
        // Mostrar alerta si hay 10 o menos entradas
        alert(`¡Date prisa, solo quedan ${entradasDisponibles} entradas para el festival!`);
    }

});
