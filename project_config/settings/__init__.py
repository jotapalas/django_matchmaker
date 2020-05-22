from os import environ
from logging import getLogger

logger = getLogger(__name__)

env = environ.get('MATCHMAKER_ENV', 'PRO')

logger.info(f'Loading settings for {env} environment...')
if env == 'DEV':
    from .development import *
else:
    from .production import *
logger.info('Settings loaded.')
