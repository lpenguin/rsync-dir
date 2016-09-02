class RsyncError(Exception):
    def __init__(self, reason):
        # type: (str)->RsyncError
        self.reason = reason
