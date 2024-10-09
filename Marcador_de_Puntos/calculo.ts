function actualizarPuntaje(): void {
    const ajedrezRojo = (document.getElementById('ajedrezRojo') as HTMLInputElement).valueAsNumber || 0;
    const handballRojo = (document.getElementById('handballRojo') as HTMLInputElement).valueAsNumber || 0;
    const resistenciaRojo = (document.getElementById('resistenciaRojo') as HTMLInputElement).valueAsNumber || 0;

    const ajedrezNegro = (document.getElementById('ajedrezNegro') as HTMLInputElement).valueAsNumber || 0;
    const handballNegro = (document.getElementById('handballNegro') as HTMLInputElement).valueAsNumber || 0;
    const resistenciaNegro = (document.getElementById('resistenciaNegro') as HTMLInputElement).valueAsNumber || 0;

    const puntajeRojoElemento = document.getElementById('puntajeRojo') as HTMLElement;
    const puntajeNegroElemento = document.getElementById('puntajeNegro') as HTMLElement;

    const puntajeRojoActual = parseInt(puntajeRojoElemento.innerText) || 0;
    const puntajeNegroActual = parseInt(puntajeNegroElemento.innerText) || 0;

    const totalRojo = puntajeRojoActual + ajedrezRojo + handballRojo + resistenciaRojo;
    const totalNegro = puntajeNegroActual + ajedrezNegro + handballNegro + resistenciaNegro;

    puntajeRojoElemento.innerText = totalRojo.toString();
    puntajeNegroElemento.innerText = totalNegro.toString();
    
    const resultadoElemento = document.getElementById('resultado') as HTMLElement;

    if (totalRojo > totalNegro) {
        resultadoElemento.innerText = "¡La Tribu Roja es la ganadora!";
    } else if (totalNegro > totalRojo) {
        resultadoElemento.innerText = "¡La Tribu Negra es la ganadora!";
    } else {
        resultadoElemento.innerText = "Es un empate.";
    }
}

const actualizarPuntajeBtn = document.getElementById('actualizarPuntajeBtn') as HTMLButtonElement;
actualizarPuntajeBtn.addEventListener('click', actualizarPuntaje);
