<?php
$file = '/var/www/python/stop.txt';
file_put_contents($file, 'true');
echo "Semnal de oprire trimis.";
?>
