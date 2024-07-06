/*function getQueryParams() {
    const urlParams = new URLSearchParams(window.location.search);
    const params = {}; // Object to store parameters
  
    // Loop through each parameter name
    for (const [name, value] of urlParams.entries()) {
      params[name] = value; // Add parameter to the object
    }
  
    return params; // Return the object containing all parameters
  }
  
  const queryParams = getQueryParams();
  
  const mail = queryParams.mail;
  const pan = queryParams.pan;
  const base = queryParams.base;
  const adicional = queryParams.adicional;
  const salsa = queryParams.salsa;
  
  console.log(`Mail: ${mail}`);
  console.log(`Pan: ${pan}`);
  
function crearPedido(datos) {
    datos.preventDefault();
    datosForm = new FormData(datos.target);
    const pan = datosForm.get("pan");
    const base = datosForm.get("base");
    const adicional = datosForm.get("adicional");
    const salsa = datosForm.get("salsa");
    mail = mailFromUrl;
    alert("todo mal :/");
  
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
*/
function response_received(response) {
  return response.json();
}

function request_error(error) {
  console.log("ERROR");
  console.log(error);
}

function parse_data(content) {
    console.log(content);
    const container = document.getElementById("pedidos-parser");

    for (let index = 0; index < content.length; index++) {

        const item = document.createElement("li");  

        const price = document.createElement("span");
        price.textContent = ` - precio : ${content[index].nombre}`;


        item.appendChild(price);
        alert(item);
        container.appendChild(item);
    }
}

fetch("http://localhost:5000/pedidos")
.then(response_received)
.then(parse_data)
.catch(request_error);
