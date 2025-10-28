import logging
import logging.config
import colorlog
import yaml
from pathlib import Path

def set_logger_config():
    path_to_config = (Path(__file__).resolve().parent.parent / "config" / "logger_config.yaml")
    try:
        with open(path_to_config, "r") as f:
            config = yaml.safe_load(f)
        logging.config.dictConfig(config)
    except Exception:
        pass

set_logger_config()
app_logger = logging.getLogger("app_logger")
app_logger.info("Logger has been configured and initialized.")