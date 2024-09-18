# APP NAME

<!--fixme repository-->
![un license](https://img.shields.io/github/license/RyosukeDTomita/shadow_cracker)

## INDEX

- [ABOUT](#about)
- [ENVIRONMENT](#environment)
- [HOW TO USE](#how-to-use)

---

## ABOUT

Sample for parsing hashes in /etc/shadow using [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)

---

## ENVIRONMENT

- Python: 3.12.4

---

## HOW TO USE

1. edit [./shadow_cracer.py](./shadow_cracker.py)

  ```python3
    # FIXME: shadowには/etc/shadowの一行をそのままコピペする
    shadow = "sigma:$6$supersugoisaltda$aGNLnFiImN.8qxP2VoYYCR0Q57uwPsU1ECrLCiTw9A5y68PZKCSsx9J1.EyTjdEwvfF.eJI7.4RlcA4Hswl2./:18765:0:99999:7:::"  # FIXME: this is sample
  ```
2. run tools

```shell
docker buildx bake
docker run shadow_cracker_image
```

---
