<?php
shell_exec("sudo /usr/bin/python3 /var/www/python/main.py > /var/www/out.log 2>&1 &");
echo "Alarma a fost pornita";
?>

