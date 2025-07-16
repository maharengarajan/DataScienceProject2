# source code for logging

import logging
import os
import json
from datetime import datetime

class JsonFormatter(logging.Formatter):
    """JSON formatter for structured logging"""

    def format(self, record):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
            "message": record.getMessage(),
            "process_id": os.getpid(),
            "thread_id": record.thread,
        }


        # add exception info if present
        if record.exc_info:
            log_entry["exc_info"] = self.formatException(record.exc_info)

        return json.dumps(log_entry)
    

class LoggerConfig:
    """Simple logger configuration with JSON formatter"""
    
    @staticmethod
    def get_logger(name:str = "app", level:str = "INFO") -> logging.Logger:
        logger = logging.getLogger(name)

        # avoid duplicate handlers
        if logger.handlers:
            return logger
        
        logger.setLevel(getattr(logging, level.upper()))

        # JSON formatter
        json_formatter = JsonFormatter()

        # console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(json_formatter)
        logger.addHandler(console_handler)

        # file handler
        os.makedirs("logs", exist_ok=True)
        file_handler = logging.FileHandler(f"logs/{name}.log")
        file_handler.setFormatter(json_formatter)
        logger.addHandler(file_handler)

        return logger