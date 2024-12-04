document.addEventListener('DOMContentLoaded', function () {
    // Selecciona todos los elementos <td> dentro de la clase .promotores-table
    const promotorItems = document.querySelectorAll('.promotores-table td');

    // Itera por cada elemento para agregar los eventos de hover
    promotorItems.forEach(item => {
        // Agrega el evento al pasar el ratón
        item.addEventListener('mouseenter', function() {
            // Cambia el estilo de fondo y escala al pasar el ratón
            item.style.backgroundColor = '#c0c0c0'; // Gris más oscuro
            item.style.transform = 'scale(1.05)';   // Escala ligera
            item.style.transition = 'all 0.3s ease'; // Transición suave
        });

        // Agrega el evento al quitar el ratón
        item.addEventListener('mouseleave', function() {
            // Restaura el estilo original
            item.style.backgroundColor = ''; // Restaura el fondo original
            item.style.transform = '';      // Restaura el tamaño original
        });
    });
});