document.addEventListener('DOMContentLoaded', function () {
    // Selecciona todos los elementos <li> dentro de la clase .listaFest
    const festivalItems = document.querySelectorAll('.listaFest ul li');

    // Itera por cada elemento para agregar los eventos de hover
    festivalItems.forEach(item => {
        // Agrega el evento al pasar el ratón
        item.addEventListener('mouseenter', function() {
            // Cambia el estilo del fondo y escala al pasar el ratón
            item.style.backgroundColor = '#c0c0c0'; // Gris más oscuro
            item.style.transform = 'scale(1.1)';   // Escala ligera
            item.style.transition = 'all 0.3s ease'; // Transición suave
        });

        // Agrega el evento al quitar el ratón
        item.addEventListener('mouseleave', function() {
            // Restaura el estilo original
            item.style.backgroundColor = '#f0f0f0'; // Fondo original
            item.style.transform = 'scale(1)';      // Tamaño original
        });
    });
});