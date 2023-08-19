/** 
document.getElementByIdv).onclick = function () {
    console.log("capturamos el evento click");
    document.getElementById("demo").innerHTML = "Estamos probando nuestro primer evento en js";
}
*/
/** 
document.addEventListener('click', function() {
    console.log("hola mundo desde EventListener")
    document.getElementById("demo").innerHTML = "Estamos probando nuestro primer evento en js";
})*/
                 
document.getElementById('boton').addEventListener('click', function() {
    console.log("hola mundo desde EventListener");
    document.getElementById("demo").innerHTML = "Estamos probando nuestro primer evento en js";
});

document.getElementById('boton_color').addEventListener('click', function(){
    document.body.style.backgroundColor = '#ff0000';
});

document.getElementById('boton_default').addEventListener('click', function(){
    document.body.style.backgroundColor = '#0000ff';
});

document.getElementById('boton_ocultar').addEventListener('click', function(){
    document.getElementById("demo").style.display = 'none';
});

document.getElementById('boton_mostrar').addEventListener('click', function(){
    document.getElementById("demo").style.display= 'block';
});

const collection = document.getElementsByClassName("prueba");
for (let i = 0; i < collection.length; i++) {
  collection[i].style.backgroundColor = "green";
}