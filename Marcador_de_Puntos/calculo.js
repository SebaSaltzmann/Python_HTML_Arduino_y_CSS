function actualizarPuntaje() {
    var ajedrezRojo = document.getElementById('ajedrezRojo').valueAsNumber || 0;
    var handballRojo = document.getElementById('handballRojo').valueAsNumber || 0;
    var resistenciaRojo = document.getElementById('resistenciaRojo').valueAsNumber || 0;
    var ajedrezNegro = document.getElementById('ajedrezNegro').valueAsNumber || 0;
    var handballNegro = document.getElementById('handballNegro').valueAsNumber || 0;
    var resistenciaNegro = document.getElementById('resistenciaNegro').valueAsNumber || 0;
    var puntajeRojoElemento = document.getElementById('puntajeRojo');
    var puntajeNegroElemento = document.getElementById('puntajeNegro');
    var puntajeRojoActual = parseInt(puntajeRojoElemento.innerText) || 0;
    var puntajeNegroActual = parseInt(puntajeNegroElemento.innerText) || 0;
    var totalRojo = puntajeRojoActual + ajedrezRojo + handballRojo + resistenciaRojo;
    var totalNegro = puntajeNegroActual + ajedrezNegro + handballNegro + resistenciaNegro;
    puntajeRojoElemento.innerText = totalRojo.toString();
    puntajeNegroElemento.innerText = totalNegro.toString();
    var resultadoElemento = document.getElementById('resultado');
    if (totalRojo > totalNegro) {
        resultadoElemento.innerText = "¡La Tribu Roja es la ganadora!";
    }
    else if (totalNegro > totalRojo) {
        resultadoElemento.innerText = "¡La Tribu Negra es la ganadora!";
    }
    else {
        resultadoElemento.innerText = "Es un empate.";
    }
}
var actualizarPuntajeBtn = document.getElementById('actualizarPuntajeBtn');
actualizarPuntajeBtn.addEventListener('click', actualizarPuntaje);
