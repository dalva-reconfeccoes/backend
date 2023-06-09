from enum import Enum


class MessagesEnum(str, Enum):
    """
    Enum for messages sent by the server.
    """

    CLIENT_NOT_FOUND = "Client not found"
    INVALID_PASSWORD = "Invalid password"
    CLIENT_NOT_UPDATED = "Client not updated"
    EMAIL_ALREADY_EXIST = "Email already exists"
