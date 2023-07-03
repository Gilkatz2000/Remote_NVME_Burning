# NVMe Drive Burning Automation Project

## Introduction

This project provides an automated solution for downloading files from a server and burning them onto NVMe drives. It is designed with a Command Line Interface (CLI) and utilizes Python scripts to handle SSH connections to a remote server, file download through SFTP, and finally, writing the files onto NVMe drives.

The project is divided into several Python files, each responsible for a specific functionality in the system. These functionalities include connecting to a server, downloading files, and burning the files onto NVMe drives. 

## Modules

Here are the main modules and a brief explanation of each:

- `connect_to_server.py`: Establishes an SSH connection to a remote server, and returns an SFTP client for file operations.

- `download_file.py`: Utilizes an SFTP client to download a file from a specified remote path to a local path. 

- `burn_nvme.py`: Changes the working directory to a specified local path, then writes a given image file to the NVMe device at /dev/nvme0n1.

- `print_directory.py`: Prints the directory structure of the remote path on the server, and initiates the NVMe burning process.

- `remove_file.py`: Removes a file from a given file path.

- `userCredentials.py`: Prompts the user to enter their credentials for the SSH server connection.

- `main.py`: The main entry point of the system that ties everything together. It imports the necessary functions from the other Python files and executes the program.

## Usage

The system is initiated by running the `main.py` script. The user will then be prompted to enter their username and password for the server. Upon successful authentication, the system retrieves the directory structure from the remote server and prints it to the user. The user can then choose which directory and file they would like to download and burn onto the NVMe drive.

The downloaded file is saved to a predefined local path, and then `burn_nvme.py` is invoked to write the file onto the NVMe drive. After the burning process, the downloaded file can optionally be removed.

## Conclusion

This system automates the process of downloading and burning files onto NVMe drives. It leverages Python's ability to interact with SSH and SFTP protocols and handle file and directory operations. The use of clear and modular Python scripts also makes the system easy to understand and modify according to the needs of the user.
