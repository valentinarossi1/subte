function parse_data(content) {
  console.log(content);
  const container = document.getElementById("pedidos-parser");

  const labels = {
    adicional: "ADICIONAL",
    base: "BASE",
    pan: "PAN",
    salsa: "SALSA",
  };

  for (let index = 0; index < content.length; index++) {
    const item = document.createElement("li");
    item.style.marginBottom = "10px";

    const link = document.createElement("a");
    link.textContent = `${content[index].mail}`;
    link.setAttribute("href", `/cclientes?${content[index].id}`);
    link.setAttribute("target", "_blank");
    item.appendChild(link);

    for (const key in content[index]) {
      const label = labels[key];

      if (label) {
        const span = document.createElement("li");

        span.textContent = ` ${label}-> : ${content[index][key]}`;
        item.appendChild(span);
      } else {
        console.warn(`Igorando propiedad desconocida ${key}`);
      }
    }
    container.appendChild(item);
  }
}

fetch("http://localhost:5000/pedidos")
  .then((res) => res.json())
  .then(parse_data)
  .catch((error) => console.log("Error: ", error));
