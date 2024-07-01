let indiceImagen = 0;

mostrarImagen(indiceImagen); /*muestra la primera imagen*/

function deslizarImagen(i) {
  indiceImagen += i;
  mostrarImagen(indiceImagen);
}

function mostrarImagen(indice) {
  let imagenes = document.getElementsByClassName("img-carrusel");
  let cantidadImagenes = imagenes.length;

  if (indice >= cantidadImagenes) {
    indiceImagen = 0;
  }
  if (indice < 0) {
    indiceImagen = cantidadImagenes - 1;
  }
  for (let x = 0; x < cantidadImagenes; x++) {
    /*oculta inicialmente todas las imagenes*/
    imagenes[x].style.display = "none";
  }

  imagenes[indiceImagen].style.display =
    "block"; /*muestra la imagen que indica el indice*/
}

function response_received(response) {
  return response.json();
}

function request_error(error) {
  console.log("ERROR");
  console.log(error);
}

function parse_data(content) {
  console.log(content);
  const container = document.getElementById("clientes");

  for (let index = 0; index < content.length; index++) {
    const item = document.createElement("p");
    item.innerHTML = `<a href="/clientes?${content[index].id}" target=blank> ${content[index].nombre}</a> - direccion: ${content[index].direccion}`;

    container.append(item);
  }
}

fetch("http://localhost:5000/clientes")
  .then(response_received)
  .then(parse_data)
  .catch(request_error);
