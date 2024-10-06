import requests

# DefectDojo API Configuration
defectdojo_url = "https://<your-defectdojo-url>/api/v2/import-scan/"
api_token = "<your-api-token>"
headers = {
    "Authorization": f"Token {api_token}",
    "Content-Type": "application/json"
}

# Upload VulnWhisperer results to DefectDojo
def upload_scan_result(file_path, engagement_id):
    url = defectdojo_url
    
    # Prepare the file and data payload
    files = {
        "file": open(file_path, 'rb')
    }
    data = {
        "engagement": engagement_id,
        "scan_type": "OpenVAS Scan",
        "active": True,
        "verified": True
    }
    
    # Send POST request to DefectDojo
    response = requests.post(url, headers=headers, files=files, data=data)
    
    # Check response
    if response.status_code == 201:
        print("Scan result successfully uploaded to DefectDojo.")
    else:
        print(f"Failed to upload scan result: {response.status_code} - {response.text}")

if __name__ == "__main__":
    # Example Usage
    file_path = "/path/to/vulnwhisperer/results/openvas_report.xml"
    engagement_id = 1  # Replace with actual engagement ID in DefectDojo
    
    upload_scan_result(file_path, engagement_id)
import requests

# DefectDojo API Configuration
defectdojo_url = "https://<your-defectdojo-url>/api/v2/import-scan/"
api_token = "<your-api-token>"
headers = {
    "Authorization": f"Token {api_token}",
    "Content-Type": "application/json"
}

# Upload VulnWhisperer results to DefectDojo
def upload_scan_result(file_path, engagement_id):
    url = defectdojo_url
    
    # Prepare the file and data payload
    files = {
        "file": open(file_path, 'rb')
    }
    data = {
        "engagement": engagement_id,
        "scan_type": "OpenVAS Scan",
        "active": True,
        "verified": True
    }
    
    # Send POST request to DefectDojo
    response = requests.post(url, headers=headers, files=files, data=data)
    
    # Check response
    if response.status_code == 201:
        print("Scan result successfully uploaded to DefectDojo.")
    else:
        print(f"Failed to upload scan result: {response.status_code} - {response.text}")

if __name__ == "__main__":
    # Example Usage
    file_path = "/path/to/vulnwhisperer/results/openvas_report.xml"
    engagement_id = 1  # Replace with actual engagement ID in DefectDojo
    
    upload_scan_result(file_path, engagement_id)
