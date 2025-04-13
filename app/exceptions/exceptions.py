class CoreException(Exception):
    def __init__(self, message: str = "An unexpected error has occurred."):
        self.message = message
        super().__init__(message)


class RepositoryException(CoreException): ...
