function parse_data(content) {
  console.log(content);
  const container = document.getElementById("pedidos-parser");

  const labels = {
    pan: "PAN",
    base: "BASE",
    adicional: "ADICIONAL",
    salsa: "SALSA",
    /*id_pedido: "ID",*/
  };

  for (let index = 0; index < content.length; index++) {
    const item = document.createElement("ul");

    const link = document.createElement("h4");
    link.textContent = `${content[index].mail}`;
    item.appendChild(link);

    for (const key in content[index]) {
      const label = labels[key];

      if (label) {
        const span = document.createElement("li");

        span.textContent = ` ${label}: ${content[index][key]}`;
        item.appendChild(span);
      } else {
        console.log(`Igorando propiedad desconocida ${key}`);
      }
    }
    container.appendChild(item);

    const editar = document.createElement("a");
    editar.textContent = `editar   `;
    editar.setAttribute("href", `../hace-tu-pedido/paso2?id=${content[index].id_pedido}`);
    editar.classList.add('editar');
    editar.setAttribute("target", "_blank");

    item.appendChild(editar);
    const iconoEditar = document.createElement("i");
    iconoEditar.classList.add("fa-regular", "fa-pen-to-square");
    editar.classList.add("editar");
    editar.appendChild(iconoEditar);

    const eliminar = document.createElement("a");
    eliminar.textContent = `eliminar   `;
    eliminar.setAttribute("href", `editar?${content[index].id_pedido}`);
    eliminar.setAttribute("target", "_blank");
    eliminar.classList.add("basura");
    item.appendChild(eliminar);

    const iconoEliminar = document.createElement("i");
    iconoEliminar.classList.add("fa-regular", "fa-trash-can");
    iconoEliminar.classList.add("basura");
    eliminar.appendChild(iconoEliminar);
  }
}

fetch("http://localhost:5000/pedidos")
  .then((res) => res.json())
  .then(parse_data)
  .catch((error) => console.log("Error: ", error));
