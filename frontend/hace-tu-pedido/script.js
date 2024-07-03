function handle_response(data) {
    if (data != null) {
      window.location.href = 'paso2/paso2.html';
    } else {
      console.log(data);
      alert("ERROR");
    }
  }
  
  function crearCliente(datos) {
    datos.preventDefault();
  
    datosForm = new FormData(datos.target);
  
    const nombreApellido = datosForm.get("nombre-apellido");
    const direccion = datosForm.get("direccion");
    const telefono = datosForm.get("telefono");
    const mail = datosForm.get("mail");
  
    fetch("http://localhost:5000/clientes", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        nombre_apellido: nombreApellido,
        direccion: direccion,
        telefono: telefono,
        mail: mail,
      }),
    })
      .then((res) => res.json())
      .then(handle_response)
      .then((error) => console.log("Error: ", error));
  }
  

