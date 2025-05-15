var interval = 0;
var apasare = 0;
var stare = "";

function changeText() {
	const text = document.getElementById("lcd-text").value;
	fetch("php/schimba_text.php", {
		method: "POST",
		headers: {
			"Content-Type": "application/x-www-form-urlencoded"
		},
		body: "lcd-prompt=" + encodeURIComponent(text)
	})
	.then(raspuns => raspuns.text())
	.then(text => {
		document.getElementById("mesaj-returnat").innerHTML += text + "<br> &gt; ";
	})
}

function pornesteSistem() {

	const text = document.getElementById("lcd-text").value;
	if(text.length > 16) {
		alert("Introduceti o valoare de maxim 16 caractere!");
		return;
	}
	if(apasare == 0) {
		apasare = 1;
		fetch("php/porneste.php", {
			method: "POST",
			headers: {
				"Content-Type": "application/x-www-form-urlencoded"
			},
			body: "lcd-text=" + encodeURIComponent(text)
		})
		.then(raspuns => raspuns.text())
		.then(text => {
			document.getElementById("mesaj-returnat").innerHTML += text + "<br> &gt; ";
			interval = setInterval(actualizeazaStare, 300);
		})
		.catch(error => document.getElementById("mesaj-returnat").innerHTML += error + "<br> > ");
	} else {
		console.log("deja ruleaza un script");
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
			if(stare == "Foc detectat!") {
                       		if(confirm("Alerta de incendiu! Doriti sa anuntati autoritatile?")) {
                                	const emailData = {
                                        	to: "matei-andrei.bejenaru@student.tuiasi.ro",
                                                subject: "Proiect SM - Sistem incendiu",
                                                message: "Acesta este un test. Sistemul a detectat un incendiu!"
                                        };
                                        fetch("php/trimite_email.php", {
                                                method: "POST",
                                                headers: {
                                                        "Content-Type": "application/json"
                                                },
                                                body: JSON.stringify(emailData)
                                        })
                                        .then(raspuns => raspuns.json())
                                        .then(data => {
                                                console.log(data);
                                                alert(data.message);
                                        })
                                        .catch(error => {
                                                console.error("Eroare: ", error);
                                        });
                                }
                        }

		})
		.catch(error => document.getElementById("mesaj-returnat").innerHTML += error + "<br> > ");
}

function opresteSistem() {
	apasare = 0;
	clearInterval(interval);
	fetch("php/opreste.php")
	.then(raspuns => raspuns.text())
	.then(text => {
		document.getElementById("mesaj-returnat").innerHTML += text + "<br> > "
	})
}
