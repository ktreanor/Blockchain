from block import Block
import pickle

class Blockchain:

    def __init__(self):
        """Blockchain initializer
        """
        self.__chain = []

    def __iter__(self):
        """Makes the blockchain iterable

        Yields:
            _type_: Block
        """
        for current_block in self.__chain:
            yield current_block

    def __getitem__(self, key: int) -> Block:
        """Allows a block in a blockchain to be referenced via index

        Args:
            key (int): The index location of the block in the blockchain

        Returns:
            Block: The bloc being indexed
        """
        return self.__chain[key]

    def __len__(self) -> int:

        return len(self.__chain)

    def __append_genesis(self) -> None:
        """Creates the genesis block of a blockchain (the first block)
        """

        # All genesis blocks' previous hash value is all 0
        genesis_block = Block(0, "Genesis Block", "0" * 64)
        self.__chain.append(genesis_block)

    def append(self, data: str):
        """Adds a new block to the blockchain

        Args:
            data (str): The data packet of the block
        """

        # If this is an empty blockchain a genesis block must be created first
        if len(self.__chain) == 0:
            self.__append_genesis()

        # Get the index and hash of the last block in the chain
        index = self.__chain[-1].index + 1
        prev_hash = self.__chain[-1].hash

        # Create a new block with the next index number, included data, and the previous' block's hash
        new_block = Block(index, data, prev_hash)

        # Add the new block to the chain
        self.__chain.append(new_block)

    def refresh_chain(self) -> None:
        """Runs through the blockchain recreating all hash's using the nonce
        """

        # Genesis blocks always have a previous hash value of all 0
        previous_hash = "0" * 64

        # Loop through the chain setting the previous hash from the value of the last block
        for current_block in self.__chain:
            current_block.previous_hash = previous_hash
            previous_hash = current_block.hash

    def save(self, file_name: str):
        """Saves the blockchain to a file

        Args:
            file_name (str): Nave of teh blockchain file
        """
        
        # Check to see if the file name has the right extension, if not add it 
        if file_name[-4:] != '.blk':
            file_name += '.blk'
        
        with open(file_name, 'wb') as f:
            pickle.dump(self.__chain, f)

    def read(self, file_name: str):
        """Opens a saved blockchain

        Args:
            file_name (str): Name of the blockchain file
        """

        # Check to see if the file name has the right extension, if not add it 
        if file_name[-4:] != '.blk':
            file_name += '.blk'

        with open(file_name, 'rb') as f:
            self.__chain = pickle.load(f)

    def is_valid(self) -> bool:
        """Checks the blockchain to insure it's valid.

        Returns:
            bool: True if the blockchain is valid, False if it is not
        """

        # The genesis block always has a hash of all 0
        previous_hash = "0" * 64
        valid_blockchain = True

        for current_block in self.__chain:
            if previous_hash != current_block.previous_hash:
                valid_blockchain = False
            previous_hash = current_block.hash
        return valid_blockchain

def main():

    test_chain = Blockchain()
    test_chain.read('test_chain')

    """
    test_chain.append("The first block in my test block chain")
    test_chain.append("This is the second block in my test block chain")
    test_chain.append("This is the third block")
    test_chain.append("Number 4")

    test_chain.save('test_chain')
    """
    
    for block in test_chain:
        print(block)

if __name__ == "__main__":
    main()