from datetime import datetime
from hashlib import sha256

class Block:

    # Mining details
    PROOF = "6"
    DIFFICULTY = 4

    # Block header
    __index: int
    __previous_hash: str
    __timestamp: float
    __nonce: int

    # Block payload
    __data: str

    def __init__(self, index: int, data: str, previous_hash: str) -> None:
        """Block initialization 

        Args:
            index (int): Block index
            data (str): Payload of the block
            previous_hash (str): The hash key of the previous block in the chain
        """

        self.__index = index
        self.__data = data
        self.__previous_hash = previous_hash

        self.__mine()

    def __str__(self) -> str:
        """Returns a human-readable, or informal, string representation of the Block

        Returns:
            str: String with all the base elements of the Block
        """
        return (
            f'Index: {self.__index}\n'
            f'Previous Hash: {self.__previous_hash}\n'
            f'Data: {self.__data}\n'
            f'Nonce: {self.__nonce}\n'
            f'Hash: {self.hash}\n'
            f'Timestamp: {self.__timestamp}\n'
        )
    
    def __repr__(self):
        """Returns a more information-rich, or official, string representation of the Block. 
        """
        return f'Block({self.__index}, \'{self.__previous_hash}\', \'{self.__data}\')'

    @property
    def index(self) -> int:
        """Gets the index of the block

        Returns:
            int: Block index
        """
        return self.__index

    @property
    def data(self) -> str:
        """Gets the data of the block

        Returns:
            str: Data
        """
        return self.__data

    # TODO: Remove this, it's for testing only
    @data.setter
    def data(self, value: str):
        """Sets the data of the block (WARNING, this will break the block, it's to be used for testing)

        Args:
            value (str): Data to be set in the blocK
        """

        self.__data = value

    @property
    def nonce(self) -> int:
        """Gets the Nonce (proof of work) of the block

        Returns:
            int: Nonce
        """
        return self.__nonce

    @property
    def hash(self) -> str:
        """
        Returns the block hash
        """
        mashed_block = str(self.__index) + self.__data + self.__previous_hash + str(self.__nonce)
        return sha256(mashed_block.encode("utf-8")).hexdigest()

    @property
    def previous_hash(self) -> str:
        """
        Returns the previous block's hash
        """
        return self.__previous_hash

    @previous_hash.setter
    def previous_hash(self, value):
        self.__previous_hash = value

    @property
    def timestamp(self) -> float:
        """
        Returns the timestamp when the block was mined
        """
        return self.__timestamp

    @property
    def valid(self) -> bool:
        """
        Check to see if the nonce saved creates a hash that obeys the difficulty rules
        :return: True if the block is valid, false if not
        """

        return self.hash[:self.DIFFICULTY] == self.PROOF * self.DIFFICULTY

    def __mine(self) -> None:
        """Function used to 'mine' the block, or create the proof of work
        """

        nonce = 1
        mashed_data = str(self.__index) + self.__data + self.__previous_hash

        mashed_block_with_nonce = mashed_data + str(nonce)
        block_hash = sha256(mashed_block_with_nonce.encode("utf-8")).hexdigest()

        while block_hash[:self.DIFFICULTY] != self.PROOF * self.DIFFICULTY:
            nonce += 1
            mashed_block_with_nonce = mashed_data + str(nonce)
            block_hash = sha256(mashed_block_with_nonce.encode("utf-8")).hexdigest()

        self.__nonce = nonce
        self.__timestamp = datetime.now().timestamp()

def main():
    test_block = Block(0, 'Test Block Data', '0' * 64)

    print(test_block)
    print(repr(test_block))

if __name__ == "__main__":
    main()

