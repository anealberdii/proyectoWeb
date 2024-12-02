document.addEventListener('DOMContentLoaded', function () {
    // Selecciona los elementos <li> dentro de .listaFest
    const festivalItems = document.querySelectorAll('.listaFest ul li');

    festivalItems.forEach(item => {
        // Configuración del diseño principal
        item.style.alignItems = 'center';
        item.style.backgroundColor = '#f0f0f0';
        item.style.borderRadius = '8px';
        item.style.padding = '10px';
        item.style.boxShadow = '0px 2px 4px rgba(0,0,0,0.1)';
        item.style.maxWidth = '1200px'; 
        item.style.marginBottom = '2px'; // Ajusta el espacio entre los bloques
       


        // Estilo en hover (resaltado)
        item.addEventListener('mouseover', () => {
            item.style.backgroundColor = '#d3d3d3';   // Fondo más oscuro al pasar
            item.style.boxShadow = '0px 4px 8px rgba(0, 0, 0, 0.2)'; // Sombra más intensa
            item.style.transform = 'scale(1.05)';     // Pequeño aumento
            item.style.transition = 'all 0.3s ease';
        });

        item.addEventListener('mouseout', () => {
            item.style.backgroundColor = '#f0f0f0';   // Fondo original
            item.style.boxShadow = '0px 2px 4px rgba(0, 0, 0, 0.1)'; // Sombra original
            item.style.transform = 'scale(1)';        // Vuelve al tamaño original
        });

        // Selección y configuración de la imagen
        const img = item.querySelector('img');
        if (img) {
            img.style.width = '100px';               // Ancho fijo para la imagen
            img.style.height = 'auto';               // Mantiene proporciones
            img.style.borderRadius = '5px';          // Bordes redondeados
            img.style.marginRight = '20px';           // Espaciado entre la imagen y el texto
        }

        // Configuración del texto dentro del elemento
        const title = item.querySelector('h2');
        if (title) {
            title.style.fontSize = '1.2em';          // Tamaño del texto
            title.style.color = '#333';             // Color del texto
            title.style.margin = '0';               // Sin márgenes
            title.style.flexGrow = '1';             // El texto ocupa el espacio sobrante
        }

        const enlace = item.querySelector('a');
        if (enlace) {
            enlace.style.textDecoration = 'none';          
            enlace.style.color = 'inherit';             
            enlace.style.width = '100%';               
            enlace.style.display = 'flex';  
            enlace.style.alignItems = 'center';            
        }

    });
});
