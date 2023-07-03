import os
import subprocess

def burn_nvme(local_path, image_burn):
    # Change the current working directory to local_path
    os.chdir(local_path)
    # Define the dd command to write the image_burn to the NVMe device at /dev/nvme0n1
    command1 = ["sudo", "dd", "if=" + image_burn, "of=/dev/nvme0n1"]
    command2 = ["echo", "-e", "\\n"]
    # Execute the dd command
    subprocess.run(command1)
    # Execute an echo command to insert a new line in the terminal
    subprocess.run(command2)
