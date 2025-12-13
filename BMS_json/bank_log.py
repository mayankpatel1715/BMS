import logging

logging.basicConfig(
    filename = 'bank_logs.log',
    level = logging.DEBUG,
    format = '%(asctime)s | %(levelname)s | %(module)s | %(function)% | %(message)s'
)
