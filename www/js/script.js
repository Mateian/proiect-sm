var interval = 0;
var apasare = 0;
var stare = "";

function pornesteSistem() {
	if(apasare == 0) {
		apasare = 1;
		fetch("php/porneste.php")
		.then(raspuns => raspuns.text())
		.then(text => {
			document.getElementById("mesaj-returnat").innerHTML += text + "<br> &gt; ";
			interval = setInterval(actualizeazaStare, 300);
		})
		.catch(error => document.getElementById("mesaj-returnat").innerHTML += error + "<br> > ");
	} else {
		clearInterval(interval);
		apasare = 0;
	}

}

function actualizeazaStare() {
	fetch("php/citeste.php")
		.then(raspuns => raspuns.text())
		.then(text => {
			if(stare != text) {
				document.getElementById("mesaj-returnat").innerHTML += text + "<br> > ";
				stare = text;
			}
		})
		.catch(error => document.getElementById("mesaj-returnat").innerHTML += error + "<br> > ");
}
