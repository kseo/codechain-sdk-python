import hashlib
from typing import Union


def blake256(data: Union[bytearray, bytes, str]):
    if isinstance(data, str):
        data = bytes.fromhex(data)

    h = hashlib.blake2b(digest_size=32)
    h.update(data)
    return h.digest()


def blake256_with_key(
    data: Union[bytearray, bytes, str], key: Union[bytearray, bytes, str]
):
    if isinstance(data, str):
        data = bytes.fromhex(data)

    if isinstance(key, str):
        key = bytes.fromhex(key)

    h = hashlib.blake2b(key=key, digest_size=32)
    h.update(data)
    return h.digest()


def blake160(data: Union[bytearray, bytes, str]):
    if isinstance(data, str):
        data = bytes.fromhex(data)

    h = hashlib.blake2b(digest_size=20)
    h.update(data)
    return h.digest()


def blake160_with_key(
    data: Union[bytearray, bytes, str], key: Union[bytearray, bytes, str]
):
    if isinstance(data, str):
        data = bytes.fromhex(data)

    if isinstance(key, str):
        key = bytes.fromhex(key)

    h = hashlib.blake2b(key=key, digest_size=20)
    h.update(data)
    return h.digest()


def blake128(data: Union[bytearray, bytes, str]):
    if isinstance(data, str):
        data = bytes.fromhex(data)

    h = hashlib.blake2b(digest_size=16)
    h.update(data)
    return h.digest()


def blake128_with_key(
    data: Union[bytearray, bytes, str], key: Union[bytearray, bytes, str]
):
    if isinstance(data, str):
        data = bytes.fromhex(data)

    if isinstance(key, str):
        key = bytes.fromhex(key)

    h = hashlib.blake2b(key=key, digest_size=16)
    h.update(data)
    return h.digest()


def ripemd160(data: Union[bytearray, bytes, str]):
    if isinstance(data, str):
        data = bytes.fromhex(data)

    h = hashlib.new("ripemd160")
    h.update(data)
    return h.digest()
