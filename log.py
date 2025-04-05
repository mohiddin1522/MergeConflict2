import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

# output: 
# DEBUG:root:Debug message
# INFO:root:Info message
# WARNING:root:Warning message
# ERROR:root:Error message
# CRITICAL:root:Critical message
