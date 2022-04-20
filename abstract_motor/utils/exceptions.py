class _AddendumException(Exception):
    """
    Exception with addendum for user guidance.
    """
    def __init__(self, msg, add='', lst=[], ind='    '):
        
        underline = max([len(f"{ind*2}- {item}") for item in lst] + [len(add)])

        message = f"{msg}" + \
                  (f"\n\n{ind+add}\n" if add else '') + \
                  (("\n" + f"\n".join([f"{ind*2}- {item}" for item in lst]) + "\n\n") if lst else '') + \
                  (f"{ind+'-'*underline}" if add else '')
        
        super().__init__(message)


class ConfigurationError(_AddendumException):
    """
    Raised when configuration errors are detected.
    """
    pass


class SafetyException(_AddendumException):
    """
    Raised when operational safety is compromised.
    """
    pass