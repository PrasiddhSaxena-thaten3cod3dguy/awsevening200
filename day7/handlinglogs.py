import logging

logging.basicConfig(filename="test.log",format='%(asctime)s %(message)s',filemode="w")

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

logger.debug("Hi are you guys cleear with logging?")
logger.critical("HI this is critical")
logger.warning("This is warning")
logger.info("This is info")
logger.error("This Is error")
