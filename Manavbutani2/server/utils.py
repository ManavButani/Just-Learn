"""Contains utils like encrypt and decrypt
"""
import base64
import os
from pathlib import Path

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from dotenv import load_dotenv
from constants import PADDING

env_path = Path("./", ".env")
load_dotenv(dotenv_path=env_path)

IV = os.getenv("IV").encode("utf-8")
KEY = os.getenv("KEY")


def encrypt(data):
        """encrypt method use for encrypt the any string and also use KEY and IV for encryption 

        Args:
                data (str): original string

        Returns:
                str: encrypted string
        """
        data = pad(data.encode(), PADDING)
        cipher = AES.new(KEY.encode("utf-8"), AES.MODE_CBC, IV)
        return base64.b64encode(cipher.encrypt(data))


def decrypt(enc):
        """decrypt method use for decrypt the any string and also use KEY and IV for decryption

        Args:
            enc (str): encrypted string

        Returns:
            str: original string
        """
        enc = base64.b64decode(enc)
        cipher = AES.new(KEY.encode("utf-8"), AES.MODE_CBC, IV)
        return unpad(cipher.decrypt(enc), PADDING)
