function handle_response(data) {
  if (data != null) {
    alert("todo b   ien :D")
    window.location.href = `./confirmacion`;

  } else {
    console.log(data);
    alert("ERROR");
  }
}

function getQueryParam(param) {
  const urlParams = new URLSearchParams(window.location.search);
  return urlParams.get(param);
}

// Obtén el valor de 'mail' desde la URL
const mailFromUrl = getQueryParam('mail');


function crearPedido(datos) {
  datos.preventDefault();
  datosForm = new FormData(datos.target);
  const pan = datosForm.get("pan");
  const base = datosForm.get("base");
  const adicional = datosForm.get("adicional");
  const salsa = datosForm.get("salsa");
  mail = mailFromUrl;
  alert("todo mal :/")

  fetch("http://localhost:5000/pedidos", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      id_pan: pan,
      id_base: base,
      id_adicional: adicional,
      id_salsa: salsa,
      mail: mail,
    }),
  })
    .then((res) => res.json())
    .then(handle_response)
    .then((error) => console.log("Error: ", error));
}
