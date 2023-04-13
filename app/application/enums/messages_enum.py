from enum import Enum


class MessagesEnum(str, Enum):
    """
    Enum for messages sent by the server.
    """

    PRODUCT_NOT_FOUND = "Product not found"
    PRODUCT_ALREADY_EXIST = "Product already exists"
    CLIENT_NOT_FOUND = "Client not found"
    INVALID_PASSWORD = "Invalid password"
    CLIENT_NOT_UPDATED = "Client not updated"
    EMAIL_ALREADY_EXIST = "Email already exists"
    PARAMETERS_NOT_FOUND = "Parameters filter not found for this request."
    VERIFICATION_SENT = "Verification code sent successfully"
    EXPIRED_VERIFICATION_CODE = "Your Code has expired. Request to send a new code."
    INVALID_VERIFICATION_CODE = "Code invalid."
    UPDATED_PASSWORD = "Updated password."
