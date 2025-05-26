# Sistem de Alarmă Incendiu cu Raspberry Pi Zero

**Nume student:** Bejenaru Matei-Andrei  
**E-mail:** [matei-andrei.bejenaru@student.tuiasi.ro](mailto:matei-andrei.bejenaru@student.tuiasi.ro)  
**Repo GitHub cu proiectul complet:** [https://github.com/Mateian/proiect-sm](https://github.com/Mateian/proiect-sm)

---

## 1. Motivația alegerii temei

Siguranța împotriva incendiilor reprezintă o preocupare majoră, esențială pentru protejarea vieților omenești și a bunurilor materiale. Soluțiile comerciale sunt adesea costisitoare și dificil de adaptat în spații mici, precum camere de cămin sau apartamente.

Tema **„Sistem de alarmă incendiu cu Raspberry Pi Zero”** a fost aleasă din dorința de a dezvolta un sistem eficient, accesibil și ușor de integrat. Acesta servește și ca suport practic pentru aprofundarea cunoștințelor în domeniul **sistemelor embedded**, incluzând:

- senzori de detecție (fum și flacără)
- semnalizare vizuală (LED-uri)
- afișaj pe LCD
- interacțiune printr-o interfață web
- activare pompă

---

## 2. Rezumat

Proiectul presupune construirea unui sistem de alarmă pentru incendii folosind **Raspberry Pi Zero WH**, cu următoarele componente:

- **Senzor MQ-2** – detecție de fum/gaze
- **Senzor IR** – detecție de flacără
- **LCD 16x2** – afișare mesaje de stare
- **LED-uri** – semnalizare vizuală
- **Mini Pompă submersibilă** - stingere incendiu
- **Interfață web** – control și monitorizare sistem

Funcționalitate generală:

- Monitorizarea continuă a senzorilor
- Afișarea mesajelor de stare pe LCD
- Stingerea incendiului cu ajutorul pompei
- LED verde = sistem activ, LED roșu / verde alternativ = alarmă
- Notificare în interfața web și posibilitatea de trimitere email către autorități

---

## 3. Importanță / Utilitate în domeniul Embedded Systems - SM

Proiectul demonstrează aplicabilitatea **sistemelor embedded** în:

- protecția locuințelor și birourilor
- detectarea automată și rapidă a incendiilor
- interacțiunea om-mașină prin web și ecran

Este un exemplu concret de integrare hardware-software și de automatizare, oferind experiență practică în:

- achiziția și prelucrarea datelor de la senzori
- control hardware (GPIO, LED-uri, LCD, pompă)
- dezvoltare backend & frontend pentru interfață utilizator
- comunicare web și trimitere de notificări

---

## 4. Analiză – Design – Implementare

### 🔍 Analiză

Cerințe inițiale:

- Detectarea simultană a fumului și flăcării
- Activare pompă în caz de incendiu
- Semnalizare vizuală și afișare pe LCD
- Control din interfață web
- Trimiterea automată a unui email în caz de urgență

### 🧩 Design

- **Platformă:** Raspberry Pi Zero WH
- **Senzori:** MQ-2 pentru fum/gaz, senzor IR pentru flacără
- **LED-uri:** Verde (activ), Roșu (alarmă)
- **LCD 16x2:** Mesaje de stare și alertă
- **Pompă submersibilă** Stingere incendiu
- **Web server:** PHP + HTML + JS pentru interfață control

### ⚙️ Implementare

- Script **Python** rulează permanent, monitorizează senzori, actualizează LCD și LED-uri, pornește pompa
- **Fișiere text** utilizate pentru comunicarea dintre scriptul Python și serverul PHP
- **Server web:** HTML + PHP pentru afișare, control sistem și notificări
- **Email alert:** PHP `mail()` configurat cu antete și server local

---

## 5. Probleme întâmpinate și soluții

| Problemă | Soluție |
|----------|---------|
| **Zgomot electric pe GPIO** | Adăugare de rezistențe pull-up/pull-down și ajustare timpi de citire |
| **Sincronizare Python ↔ Web** | Utilizare fișiere `.txt` pentru schimb de stare între procese |
| **Limitare LCD 16x2** | Implementare logică de split text pe 2 rânduri de max. 16 caractere |
| **Trimitere email din PHP** | Configurare server mail local, antete corecte pentru email valid |
| **Control pornire/oprire script** | Fișier flag `stop.txt` pentru controlul execuției scriptului Python |

---

## 6. Prezentare componente

- 🧠 **Raspberry Pi Zero WH**
- 🌫️ **Senzor MQ-2 (fum/gaz)**
- 🔥 **Senzor IR digital (flacără)**
- 📺 **LCD1602 HD44780**
- ⛽ **Mini Pompă de apă submersibilă**
- 💡 **LED-uri** (verde și roșu)

---

## 7. Ce se învață replicând proiectul

- Configurare și citire GPIO pe Raspberry Pi
- Programare în Python pentru interacțiune cu senzori
- Sincronizare inter-proces și comunicare software
- Crearea unei interfețe web simple (HTML + PHP)
- Trimiterea automată de emailuri dintr-un sistem embedded

---

## 8. Bibliografie

- 📘 [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/)
- 💬 [Raspberry Pi Forum](https://forums.raspberrypi.com/)
- 📄 [Pi Zero Hardware Guide (PDF)](https://cdn.sparkfun.com/assets/learn_tutorials/6/7/6/PiZero_1.pdf)
- 🛠️ [Raspberry Pi Spy](https://www.raspberrypi-spy.co.uk/)
- 🤖 [OpenAI](https://openai.com/)

---

📽️ **Prezentare video + Cod sursă complet:**  
👉 [https://github.com/Mateian/proiect-sm](https://github.com/Mateian/proiect-sm)

