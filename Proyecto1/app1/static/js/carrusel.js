document.addEventListener('DOMContentLoaded', function () {
    const carrusel = document.querySelector('.carrusel');
    const items = document.querySelectorAll('.carrusel-item');
    const prevButton = document.querySelector('.carrusel-button.prev');
    const nextButton = document.querySelector('.carrusel-button.next');
    const itemsToShow = 3; // Mostrar 3 elementos por vez
    const totalItems = items.length;
    let index = 0;

    function updateCarrusel () {
        const itemWidth = items[0].clientWidth + 20; // Incluye el margen de 10px a cada lado
        const totalVisibleWidth = itemWidth * itemsToShow;
        carrusel.style.transform = `translateX(-${index * itemWidth}px)`;

        // Revisamos si es el final y hacemos el loop
        if (index >= totalItems) {
            setTimeout(() => {
                carrusel.style.transition = 'none'; // Eliminamos la transición para el salto instantáneo
                index = 0; // Volvemos al inicio
                carrusel.style.transform = `translateX(0)`; // Reiniciamos la posición
            }, 500); // Esperamos un pequeño intervalo para no interferir con la animación
        } else {
            carrusel.style.transition = 'transform 0.5s ease-in-out'; // Animación normal
        }
    }

    nextButton.addEventListener('click', () => {
        if (index < totalItems) {
            index++; // Avanzar
        }
        updateCarrusel();
    });

    prevButton.addEventListener('click', () => {
        if (index > 0) {
            index--; // Retroceder
        } else {
            index = totalItems - itemsToShow; // Ir al final en caso de retroceso desde el inicio
            carrusel.style.transition = 'none'; // Eliminar animación
            carrusel.style.transform = `translateX(-${index * (items[0].clientWidth + 20)}px)`;
            setTimeout(() => carrusel.style.transition = 'transform 0.5s ease-in-out', 50); // Rehabilitar animación
        }
        updateCarrusel();
    });

    // Auto-scroll continuo
    setInterval(() => {
        if (index < totalItems) {
            index++; // Avanza
        }
        updateCarrusel();
    }, 3000); // Cada 3 segundos
});



