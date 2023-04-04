import base64
import hashlib
import os
import re
from datetime import datetime, timedelta


def md5(value: str):
    hash_value = hashlib.md5(value.encode()).hexdigest()
    return hash_value


def sha1(value: str):
    hash_value = hashlib.sha1(value.encode()).hexdigest()
    return hash_value


def base64_decode(value: str):
    decode_value = os.popen(f'echo "{value}" | base64 --decode').read()
    return decode_value


def base64_encode(value: str):
    encode_value = base64.b64encode(value.encode()).decode()
    return encode_value


def generate_token(mac_address: str) -> str:
    hash_generated = base64_encode(sha1(md5(mac_address.upper())))
    return hash_generated


def generate_token_response(mac_address: str, ip_addres: str, port: int) -> str:
    mixe_strings = f"{mac_address}:{ip_addres}:{port}"
    hash_generated = base64_encode(sha1(md5(mixe_strings)))
    return hash_generated


def is_valid_token(token: str, mac_address: str) -> bool:
    return token == generate_token(mac_address)


def check_sum_response(token: str, mac_address: str) -> str:
    hash_generated = sha1(md5(f"{token}:{mac_address}"))
    check_sum = base64_encode(hash_generated)
    return check_sum[:8]


def is_valid_mac_address(mac_address: str) -> bool:
    regex = re.compile(r"^([0-9a-fA-F]{2}[:]){5}([0-9a-fA-F]{2})$")
    return regex.match(mac_address) is not None


def is_valid_ip_address(ip_address: str) -> bool:
    regex = re.compile(
        r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    )
    return regex.match(ip_address) is not None


async def clean_none_values_dict(kargs: dict) -> dict:
    cp_dict = kargs.copy()
    for key, value in kargs.items():
        if not value:
            del cp_dict[key]
    return cp_dict


def generate_verification_code():
    code = ""
    datetime_now = datetime.now()
    datetime_expiration = datetime_now + timedelta(minutes=5)
    return code, datetime_expiration
