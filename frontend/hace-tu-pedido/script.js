function guardarDatos() {
    const nombre = document.getElementById('nombre-apellido').value;
    const direccion = document.getElementById('direccion').value;
    const telefono = document.getElementById('telefono').value;
    const mail = document.getElementById('mail').value;

    // Guardar en localStorage
    localStorage.setItem('nombre', nombre);
    localStorage.setItem('direccion', direccion);
    localStorage.setItem('telefono', telefono);
    localStorage.setItem('mail', mail);

    // Redirigir a la siguiente página
    location.href = 'paso2/paso2.html';
}