<?php
header('Content-Type: application/json');

if($_SERVER['REQUEST_METHOD'] === 'POST') {
	$data = json_decode(file_get_contents('php://input'), true);

	$to = $data['to'];
	$subject = $data['subject'];
	$message = $data['message'];
	$headers = 'From: Matei <your@email.com>' . "\r\n" .
		'Reply-To: your@email.com' . "\r\n" .
		'Content-Type: text/plain; charset=UTF-8';

	if(mail($to, $subject, $message, $headers)) {
		echo json_encode(['status' => 'success', 'message' => 'Email trimis cu succes!']);
	} else {
		echo json_encode(['status' => 'error', 'message' => 'Eroare la trimiterea emailului.']);
	}
} else {
	echo json_encode(['status' => 'error', 'message' => 'Metoda invalida.']);	
}

?>
