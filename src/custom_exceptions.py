import traceback
import sys


class customException(Exception):
    def __init__(self, error_message, error_detail: sys):
        #if error present in Exception class then only call the super class else pass the message to custom exception class
        super().__init__(error_message) #inheriting from Exception class
        self.error_message = self.get_detailed_error_message(
            error_message, error_detail
        )

    @staticmethod #since we are not creating custom exception class again and again we can use static method
    def get_detailed_error_message(error_message, error_detail: sys) -> str:
        #see below example of traceback module
        '''(venv) PS D:\Swapnil\Scaler\MLOps\Hotel_reservation_prediction_GCP> python test.py
            Traceback (most recent call last):
        File "D:\Swapnil\Scaler\MLOps\Hotel_reservation_prediction_GCP\test.py", line 1, in <module>
            print(10/0)
          ~~^~
        ZeroDivisionError: division by zero'''
        _, _, exc_tb = traceback.sys.exc_info() #to get the exception info traceback details only
        line_number = exc_tb.tb_lineno # to get the line number where error occurred like line 1 in test.py
        file_name = exc_tb.tb_frame.f_code.co_filename #to get the file name where error occurred like test.py

        detailed_message = f"Error occurred in script: {file_name} at line number: {line_number} with message: {error_message}"
        return detailed_message

    #magic method to print the error message when we print the object of custom exception class
    def __str__(self):
        return self.error_message

# Custom error for data download
class DataDownloadError(customException):
    pass

# Custom error for data ingestion init
class DataIngestionInitError(customException):
    pass

class DataSplitError(customException):
    pass