import logging
from nd_20 import sum_of_numbers, number_division, root_of_number, counting_symbols

logger = logging.getLogger("Bloger")

file_handler = logging.FileHandler("20.log")
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s ---- %(message)s")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

logger.info("LOG")


