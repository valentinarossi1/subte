let mail;
let pan;
let base;
let adicional;
let salsa;

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

function fetchear() {
  const queryParams = getQueryParams();

  mail = queryParams.mail;
  pan = queryParams.pan;
  base = queryParams.base;
  adicional = queryParams.adicional;
  salsa = queryParams.salsa;

  fetch(
    `http://localhost:5000/mostrar_datos/${mail}/${pan}/${base}/${adicional}/${salsa}`,
  )
    .then((res) => res.json())
    .then(parse_data)
    .catch((error) => console.log("Error: ", error));
}

function redirigrPedidos(data) {
  if (data != null) {
    window.location.href = "../../../ver-pedidos/";
  } else {
    alert("ERor" + data);
  }
}

function confirmar() {
  alert(pan);
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
    .then(redirigrPedidos)
    .then((error) => console.log("Error: ACA ACA ", error));
}

fetchear();
