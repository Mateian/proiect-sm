<?php
$lcd_text = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $lcd_text = $_POST['lcd-text'] ?? '';
    $text_scurtat = escapeshellarg($lcd_text); // protejează textul împotriva caracterelor speciale

    echo "Trimis: " . htmlspecialchars($lcd_text) . "<br>";

    // Concatenează și trimite ca parametru în shell_exec
    if($lcd_text == "") {
    	$cmd = "sudo /usr/bin/python3 /var/www/python/main.py > /var/www/out.log 2>&1 &"; 
    } else {
    	$cmd = "sudo /usr/bin/python3 /var/www/python/main.py $text_scurtat > /var/www/out.log 2>&1 &";
    }
    shell_exec($cmd);

    echo "Alarma a fost pornită.";
}
?>
