import hashlib


class WineProcessingBlock:

    def __init__(self, previous_block_hash, wine_data):
        self.previous_block_hash = previous_block_hash
        self.wine_data = wine_data
        self.block_data = "-".join(wine_data) + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


data_1 = "Reben Standort: Meißen, Sachsen"
data_2 = "Gedüngt mit Pflanzenschutzmittel xy am 24.04.2022"
data_3 = "Geerntet und verarbeitet am 29.07.2022"
data_4 = "Gelagert im Keller bei durchschnittlich 19.4 Grad von 01.08.2022 - 15.01.2023"
data_5 = "Geliefert zu Weinhandel Leipzig, Karl-Liebknecht- Straße am 17.01.2023 "
data_6 = "Verkauft an Kunden am 24.01.2023"

block_1 = WineProcessingBlock("0000", [data_1, data_2])
block_2 = WineProcessingBlock(block_1.block_hash, [data_3, data_4])
block_3 = WineProcessingBlock(block_2.block_hash, [data_4, data_5])

print("\n")
print("****Block 1: Block Daten und Hash****")
print(block_1.block_data)
print(block_1.block_hash)
print("\n")
print("****Block 2: Block Daten und Hash****")
print(block_2.block_data)
print(block_2.block_hash)
print("\n")
print("Block 3: Block Daten")
print(block_3.block_data)
print("\n****Hash des Blocks 3 und damit Head der Blockchain:**** ")
print(block_3.block_hash)
