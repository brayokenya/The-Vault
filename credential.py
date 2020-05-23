
class Credential:
    """
    class that creates instances of credentials
    """
    credentials = []

    def __init__(self, service_provider, username, password):
        self.service_provider = service_provider
        self.username = username
        self.password = password

    def save_credential(self):
        """
        This method saves user objects to the users list
        """
        self.new_credential.save_credential()
        Credential.credentials.append(self)
