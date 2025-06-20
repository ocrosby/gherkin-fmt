import logging
import os

# Create a logger
logger = logging.getLogger("gherkin_fmt.logger")
logger.setLevel(logging.DEBUG)

# Create log directory if it doesn't exist
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "app.log")

# File handler
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Example usage
# if __name__ == "__main__":
#    logger.info("Logger is configured and ready to use.")
#    logger.debug("This is a debug message.")
#    logger.error("This is an error message.")
