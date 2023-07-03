import paramiko

global ssh
def connect_to_server(host, port, username, password):
    # Create a new SSH client
    ssh = paramiko.SSHClient()
    # Automatically add the server's host key (needed to establish a secure connection)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Establish the connection to the server
    ssh.connect(host, port, username, password)
    # Open a new SFTP session over the secure SSH connection
    sftp = ssh.open_sftp()
    # Return the SSH and SFTP client objects
    return ssh, sftp
