import sys

def error_message_detail(exception, error_details:sys):
    """
    This function is used to format the error message with details.
    :param exception: Exception object
    :param error_details: sys object
    :return: Formatted error message
    """
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] with message: [{str(exception)}]"
    return error_message

class CustomException(Exception):
    def __init__(self, exception, error_details:sys):
        super.__init__(exception)
        self.error_message = error_message_detail(exception, error_details)
    
    def __str__(self):
        return self.error_message