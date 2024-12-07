document.addEventListener("DOMContentLoaded", function () {
    const formulario = document.getElementById("formulario-reserva");

    if (formulario) {
        formulario.addEventListener("submit", function (event) {
            event.preventDefault(); // Evita el envío tradicional del formulario

            // Crear un objeto FormData con los datos del formulario
            const formData = new FormData(formulario);

            // Enviar los datos al servidor utilizando fetch
            fetch(formulario.action, { // Usamos el atributo 'action' del formulario para saber a qué URL enviar los datos
                method: 'POST',
                body: formData
            })
            .then(response => response.json()) // Esperamos una respuesta JSON del servidor
            .then(data => {
                if (data.success) {
                    // Mostrar el mensaje de éxito
                    document.getElementById("mensaje-exito-text").innerText = data.message;
                    const modal = document.getElementById("mensaje-exito");
                    if (modal) {
                        modal.style.display = "flex"; // Muestra el modal centrado
                    }

                    // Limpiar el formulario después de mostrar el modal
                    formulario.reset();
                } else {
                    // Mostrar el mensaje de error del servidor
                    alert(data.error || 'Hubo un problema al procesar tu reserva.');
                }
            })
            .catch(error => {
                // Manejo de errores de red o de la API
                console.error('Error al enviar los datos:', error);
                alert("Hubo un error al intentar enviar los datos.");
            });
        });
    }
});

function cerrarModal() {
    const modal = document.getElementById("mensaje-exito");
    if (modal) {
        modal.style.display = "none"; // Ocultar el modal
    }
}
