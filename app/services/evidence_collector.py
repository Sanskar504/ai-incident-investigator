import os


def collect_log_evidence(incident_id,log_file_path):
    
    if not os.path.exists(log_file_path):
        raise FileNotFoundError("Log file does not exist")
    
    with open(log_file_path, "r") as file:
        content = file.read()

    return {
        "source" : "application_logs",
        "content" : content ,
        "incident_id" : incident_id
    }


    