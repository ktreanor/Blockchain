from datetime import datetime
from hashlib import sha256

class Block:

    # Mining details
    PROOF = "6"
    DIFFICULTY = 4

    # Block header
    __index: int
    __previous_hash: str
    __timestamp: datetime
    __nonce: int

    # Block payload
    __data: str
    #__data: list

    def __init__(self, index: int, data: str, previous_hash: str) -> None:
        """Block initializer

        Args:
            index (int): Block index
            data (str): Payload of the block
            previous_hash (str): The hash of the previous block in the chain
        """

        self.__index = index
        self.__data = data
        self.__previous_hash = previous_hash

        self.__mine()

    def __str__(self) -> str:
        """A human-readable (informal) string representation of the Block

        Returns:
            str: All the base elements of the Block
        """

        return (
            f'Index: {self.__index}\n'
            f'Previous Hash: {self.__previous_hash}\n'
            f'Data: {self.__data}\n'
            f'Nonce: {self.__nonce}\n'
            f'Hash: {self.hash}\n'
            f'Timestamp: {self.__timestamp}\n'
        )

    def __repr__(self) -> str:
        """Returns a more information-rich, or official, string representation of the Block.

        Returns:
            str: Printable representation of the object
        """
        return f'Block({self.__index}, \'{self.__previous_hash}\', \'{self.__data}\')'

    @property
    def index(self) -> str:
        """Index of the block"""

        return self.__index

    @property
    def data(self) -> str:
        """The payload of the block (WARNING, setting the data will break the block, it's to be used for testing)"""

        return self.__data

    # TODO: Change this to throw an error
    @data.setter
    def data(self, value: str) -> None:

        self.__data = value

    @property
    def nonce(self) -> int:
        """The nonce (proof of work) of the block"""
        return self.__nonce

    @property
    def hash(self) -> str:
        """The hash of the block"""

        mashed_block = str(self.__index) + self.__data + self.__previous_hash + str(self.__nonce)
        return sha256(mashed_block.encode("utf-8")).hexdigest()

    @property
    def previous_hash(self) -> str:
        """Previous block's hash (WARNING, this will break the block, it's to be used for testing only)
        """
        return self.__previous_hash

    @previous_hash.setter
    def previous_hash(self, value: str) -> None:

        self.__previous_hash = value

    @property
    def timestamp(self) -> float:
        """The timestamp of when the Block was successfully mined"""

        return self.__timestamp

    def is_valid(self) -> bool:
        """Confirms the nonce saved creates a hash that obeys the difficulty rules

        Returns:
            str: True if the block is valid, False otherwise
        """

        return self.hash[:self.DIFFICULTY] == self.PROOF * self.DIFFICULTY

    def __mine(self) -> None:
        """Function used to 'mine' the block, or create the proof of work"""

        nonce = 1
        mashed_data = str(self.__index) + self.__data + self.__previous_hash

        mashed_block_with_nonce = mashed_data + str(nonce)
        block_hash = sha256(mashed_block_with_nonce.encode("utf-8")).hexdigest()

        while block_hash[:self.DIFFICULTY] != self.PROOF * self.DIFFICULTY:
            nonce += 1
            mashed_block_with_nonce = mashed_data + str(nonce)
            block_hash = sha256(mashed_block_with_nonce.encode("utf-8")).hexdigest()

        self.__nonce = nonce
        self.__timestamp = datetime.now()

if __name__ == "__main__":
    test_block = Block(0, 'Test Block Data', '0' * 64)

    print(test_block)
    print(repr(test_block))
