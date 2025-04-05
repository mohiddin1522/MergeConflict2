import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    filemode='a',
    format = '%(name)s - %(levelname)s - %(message)s'   
)

logging.debug('Debug message')
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")


