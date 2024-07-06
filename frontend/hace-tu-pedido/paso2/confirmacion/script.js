function getQueryParams() {
  const urlParams = new URLSearchParams(window.location.search);
  const params = {};

  for (const [name, value] of urlParams.entries()) {
    params[name] = value;
  }

  return params;
}

function parse_data(content) {
  const container = document.getElementById("pedidos-parser");

  const item = document.createElement("li");

  const labels = {
    nombre: "NOMBRE",
    mail: "MAIL",
    pan: "PAN",
    base: "BASE",
    precio: "PRECIO",
    adicional: "ADICIONAL",
    salsa: "SALSA",
  };

  for (const key in content) {
    const label = labels[key];
    if (label) {
      const span = document.createElement("li");
      span.textContent = ` ${label}-> : ${content[key]}`;
      item.appendChild(span);
    } else {
      console.warn(`Ignoring unknown property: ${key}`);
    }
  }

  container.appendChild(item);
}

function response_received(response) {
  return response.json();
}

function request_error(error) {
  console.log("ERROR");
  console.log(error);
}
function fetchear() {
  const queryParams = getQueryParams();

  const mail = queryParams.mail;
  const pan = queryParams.pan;
  const base = queryParams.base;
  const adicional = queryParams.adicional;
  const salsa = queryParams.salsa;

  fetch(
    `http://localhost:5000/mostrar_datos/${mail}/${pan}/${base}/${adicional}/${salsa}`,
  )
    .then(response_received)
    .then(parse_data)
    .catch(request_error);
}

fetchear();
