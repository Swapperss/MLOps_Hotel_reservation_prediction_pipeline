from src.logger import get_logger
from src.custom_exceptions import customException
import sys # to pass the system details to custom exception class


logger = get_logger(__name__)

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        logger.info(f"Division successful: {num1} / {num2} = {result}")
        return result
    except Exception as e:
        logger.error("Error occurred during division.")
        raise customException(e, sys) from e
    
# Test the function
if __name__ == "__main__":
    try:
        logger.info("Attempting to divide 10 by 2.")
        divide_numbers(10, 2)
    except customException as ce:
        logger.error(f"Caught a custom exception: {ce}")