import getpass

def get_user_credentials():
    """Prompts the user to enter their credentials and returns them as a tuple."""
    # The IP used here was originally used inside Intel's domain 
    # and will not be shared in the source code for security reasons.
    host = "192.168.***.***"
    port = 22
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    return (host, port, username, password)