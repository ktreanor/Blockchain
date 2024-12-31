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
    #__data: tuple

    def __init__(self, index, data, previous_hash):
        """Block initialization

        :param index: Block index
        :type index: int
        :param data: Payload of the block
        :type data: str
        :param previous_hash: The hash key of the previous block in the chain
        :type previous_hash: str
        """

        self.__index = index
        self.__data = data
        self.__previous_hash = previous_hash

        self.__mine()

    def __str__(self):
        """Returns a human-readable (informal) string representation of the Block

        :return: String with all the base elements of the Block
        :rtype: str
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
    def index(self):
        """Index of the block

        :return: Block index
        :rtype: int
        """
        return self.__index

    @property
    def data(self):
        """The payload of the block

        :returns: Payload of the block
        :rtype: str
        """
        return self.__data

    # TODO: Remove this, it's for testing only
    @data.setter
    def data(self, value):
        """Sets the data of the block (WARNING, this will break the block, it's to be used for testing)

        :param value: Data to be set in the block
        :type value: str
        """

        self.__data = value

    @property
    def nonce(self):
        """Nonce (proof of work) of the block

        :returns: Nonce of the block
        :rtype: int
        """
        return self.__nonce

    @property
    def hash(self):
        """Hash of the block

        :return: Hash of the block
        :rtype: str
        """
        mashed_block = str(self.__index) + self.__data + self.__previous_hash + str(self.__nonce)
        return sha256(mashed_block.encode("utf-8")).hexdigest()

    @property
    def previous_hash(self):
        """Previous block's hash

        :return: Hash of the previous block
        :rtype: str
        """
        return self.__previous_hash

    @previous_hash.setter
    def previous_hash(self, value):
        """Sets the previous hash of the block (WARNING, this will break the block, it's to be used for testing)

        :param value: Hash of the previous block
        :type value: str
        """

        self.__previous_hash = value

    @property
    def timestamp(self):
        """Returns the timestamp of the block when successfully mined

        :return: Timestamp of the block
        :rtype: datetime
        """
        return self.__timestamp

    def is_valid(self):
        """Confirms the nonce saved creates a hash that obeys the difficulty rules

        :return: True if the block is valid, False if not
        :rtype: bool
        """

        return self.hash[:self.DIFFICULTY] == self.PROOF * self.DIFFICULTY

    def __mine(self):
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
