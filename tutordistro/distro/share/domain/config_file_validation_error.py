class ConfigFileValidationError(Exception):
    def __init__(self, setting, error_message):
        self.setting = setting
        self.error_message = error_message

    def __str__(self):
        return f"Syntax error in {self.setting}: {self.error_message}"
