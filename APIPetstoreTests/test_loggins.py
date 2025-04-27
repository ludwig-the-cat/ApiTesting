import logging
LOGGER = logging.getLogger(__name__)

def test_mylog():
    LOGGER.info('пойдет')
    LOGGER.warning('Warning logs')
    LOGGER.error('Jesus!')
    LOGGER.critical('!!!!')
    assert True