import os
import datetime
from connect_to_server import connect_to_server
from download_file import download_file
from userCredentials import get_user_credentials
from burn_nvme import burn_nvme

def print_directory():
    # Get user credentials from input
    host, port, username, password = get_user_credentials()
    # Connect to server using credentials
    ssh, sftp = connect_to_server(host, port, username, password)

    # The remote_directory variable is an absolute path but due to 
    # security reasons at Intel, I will not share the file path.
    remote_directory = '***/****/****/****/**/****'
    # Change the working directory of the SFTP client to the remote directory
    sftp.chdir(remote_directory)
    # Get a list of directory names in the current directory
    directory_choices = sftp.listdir()
        # Get a list of directory names in the current directory
    dir_names = [d for d in sftp.listdir() if os.path.isdir(d)]

    # Check if any directory name doesn't contain the words "mev", "ci", "nvme"
    if any("mev" not in d.lower() and "ci" not in d.lower() and "nvme" not in d.lower() for d in dir_names):
        # Do not print anything
        pass
    else:
        # Print the directory names
        print(dir_names)

    print("\nWelcome to the Haifa NVMe Burning program.")
    print("Enter your user credentials to begin the burning process.\n")
    print('{:>10} {:>55}'.format("Name", "Date"))

    num = 1
    for directory_name in directory_choices:
        try:
            dir_attributes = sftp.stat(os.path.join(remote_directory, directory_name))
            creation_time = dir_attributes.st_atime
            creation_date = datetime.datetime.fromtimestamp(creation_time).strftime('%a %b %d %H:%M:%S %Y')
            print('{:<5} {:<52} | {:>25}'.format(num, directory_name, creation_date))
            num += 1
        except IOError as e:
            print("Error: could not get attributes for directory '{}': {}".format(directory_name, str(e)))

    while True:
        user_input = input("\nEnter the number of the directory you would like to access: ")
        try:
            user_choice = int(user_input)
            if user_choice < 1 or user_choice > len(directory_choices):
                print("Invalid directory number. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    chosen_directory = directory_choices[user_choice - 1]
    print("You chose directory '{}'.\n".format(chosen_directory))

    chosen_directory_files = sftp.listdir(os.path.join(remote_directory, chosen_directory))
    print('{:>25} {:>38}'.format("Name", "Date"))

    num = 1
    for image_file in chosen_directory_files:
        if image_file.endswith(".bin"):
            try:
                file_attributes = sftp.stat(os.path.join(remote_directory, chosen_directory, image_file))
                creation_time = file_attributes.st_atime
                creation_date = datetime.datetime.fromtimestamp(creation_time).strftime('%a %b %d %H:%M:%S %Y')
                print('{:<5} {:<45} | {:>25}'.format(num, image_file, creation_date))
                num += 1
            except IOError as e:
                print("Error: could not get attributes for file '{}': {}".format(image_file, str(e)))

    while True:
        user_input = input("\nEnter the number of the file you would like to download: ")
        try:
            user_choice = int(user_input)
            if user_choice < 1 or user_choice > len(chosen_directory_files):
                print("Invalid file number. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    chosen_file = chosen_directory_files[user_choice - 1]
    local_file_path = "/home/laduser/Desktop/Code/Burning/Haifa_nvme_burning/download_folder"
    remote_path = f'***/****/****/****/**/****/{chosen_directory}/{chosen_file}'
    download_file(sftp, local_file_path, remote_path)
    print("File '{}' downloaded successfully to the current directory.".format(chosen_file))
    #NVMe burning
    burn_nvme(local_file_path + chosen_file)