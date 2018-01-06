__author__ = 'royrusso'
import logging.config
import logging
import json
import os

from .vendor.elasticsearch.connections import Connections
from .config import settings


def init_log():
    """
    Initializes log format and console/file appenders
    :return:
    """
    project_root = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]

    logging.config.dictConfig(json.load(open(project_root + str(os.sep) + 'elastichq' + str(os.sep) + 'config' + str(os.sep) + 'logger.json', 'r')))


LOG = logging.getLogger('elastichq')

# Global configurations loaded from setting file
CONFIG = settings

# Global connection pool to all clusters
CONNECTIONS = Connections()

# TODO: This has to be persisted and made configurable
REQUEST_TIMEOUT = 10