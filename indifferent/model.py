
class LogEntry(object):
    """
    Represents an audit log entry
    """

    def __init__(self, key, message, code, value):
        self.key = key
        self.message = message
        self.code = code
        self.value = value

    def as_kv_dict(self):
        if self.value:
            return { self.key : self.value }
        else:
            raise Exception('No value')
