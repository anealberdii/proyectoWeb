document.addEventListener("DOMContentLoaded", function () {
    const formulario = document.getElementById("formulario-reserva");

    if (formulario) {
        formulario.addEventListener("submit", function (event) {
            event.preventDefault(); // Evita el envío tradicional del formulario

            let isFormValid = true;
            
            // Limpiar errores previos
            const inputs = formulario.querySelectorAll("input, select, textarea");
            inputs.forEach(input => {
                input.classList.remove("error"); // Elimina los errores previos
            });

            // Verificar cada campo
            inputs.forEach(input => {
                if (!input.validity.valid) {
                    input.classList.add("error"); // Resalta en rojo los campos inválidos
                    isFormValid = false;
                }
            });

            // Si el formulario es válido, enviar los datos
            if (isFormValid) {
                const formData = new FormData(formulario);

                fetch(formulario.action, {
                    method: 'POST',
                    body: formData
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        document.getElementById("mensaje-exito-text").innerText = data.message;
                        const modal = document.getElementById("mensaje-exito");
                        if (modal) {
                            modal.style.display = "flex"; // Muestra el modal centrado
                        }
                        formulario.reset(); // Limpiar el formulario después de mostrar el modal
                    } else {
                        alert(data.error || 'Hubo un problema al procesar tu reserva.');
                    }
                })
                .catch(error => {
                    console.error('Error al enviar los datos:', error);
                    alert("Hubo un error al intentar enviar los datos.");
                });
            }
        });
    }
});

function cerrarModal() {
    const modal = document.getElementById("mensaje-exito");
    if (modal) {
        modal.style.display = "none"; // Ocultar el modal
    }
}
