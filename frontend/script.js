let indiceImagen = 0;
mostrarImagen(indiceImagen);   /*muestra la primera imagen*/

function deslizarImagen(i){
  indiceImagen += i
  mostrarImagen(indiceImagen)
}

function mostrarImagen(indice){

  let imagenes = document.getElementsByClassName("img-carrusel");
  let cantidadImagenes = imagenes.length

  if (indice >= cantidadImagenes){ 
    indiceImagen=0;
  }
  if (indice < 0){
    indiceImagen = cantidadImagenes -1;
  }
  for (let x = 0; x<cantidadImagenes; x++){    /*oculta inicialmente todas las imagenes*/
    imagenes[x].style.display = "none";
  }

  imagenes[indiceImagen].style.display = "block";  /*muestra la imagen que indica el indice*/

}


