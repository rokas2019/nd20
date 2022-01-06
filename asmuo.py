import logging

logging.basicConfig(filename='asmens.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


class Asmuo:

    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        logging.info(f'Sukurtas darbuotojas: {self.vardas} {self.pavarde}')


darbuotojai = [Asmuo("Tomas", "Kucinskas"),
               Asmuo("Rokas", "Radzevicius")]
