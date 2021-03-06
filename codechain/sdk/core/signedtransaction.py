import binascii
from dataclasses import dataclass
from typing import Union

from rlp import encode

from ..utils import recover_ecdsa
from .transaction import TransactionJSON
from codechain.crypto import blake160
from codechain.crypto import blake256
from codechain.primitives import H160
from codechain.primitives import H256
from codechain.primitives import H512
from codechain.primitives import PlatformAddress


@dataclass
class SignedTransactionJSON(TransactionJSON):
    block_number: Union[int, None]
    block_hash: Union[str, None]
    transaction_index: Union[int, None]
    sig: str
    transaction_hash: str


class SignedTransaction:
    from .transaction import Transaction

    def __init__(
        self,
        unsigned: Transaction,
        signature: Union[bytes, bytearray],
        block_number: int = None,
        block_hash: H256 = None,
        transaction_index: int = None,
    ):
        self.unsigned = unsigned
        if isinstance(signature, str):
            if signature.startswith("0x"):
                signature = signature[2:]
            signature = bytes.fromhex(signature)
        self.signature = signature
        self.block_number = block_number
        self.block_hash = block_hash
        self.transaction_index = transaction_index

    def to_encode_object(self):
        result = self.unsigned.to_encode_object()
        result.append(self.signature)
        return result

    def rlp_bytes(self):
        return encode(self.to_encode_object())

    def hash(self):
        return H256(blake256(self.rlp_bytes()))

    def get_asset(self):
        raise ValueError("Not implemented")

    def get_signer_account_id(self):
        public_key = recover_ecdsa(self.unsigned, self.signature)
        return H160(blake160(public_key))

    def get_signer_address(self, network_id: str):
        return PlatformAddress.from_account_id(
            self.get_signer_account_id(), network_id=network_id
        )

    def get_signer_public(self):
        return H512(recover_ecdsa(self.unsigned, self.signature))

    def to_json(self):
        json = self.unsigned.to_json().update(
            {
                "blockNumber": self.block_number,
                "blockHash": self.block_hash,
                "transactionIndex": self.transaction_index,
                "sig": "0x" + binascii.hexlify(self.signature).decode("ascii"),
                "hash": self.hash().to_json(),
            }
        )

        return json
