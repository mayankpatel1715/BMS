import logging

logging.basicConfig(
    filename = 'file.log',
    level = logging.DEBUG,
    format = '%(asctime)s | %(levelname)s | %(message)s'
)