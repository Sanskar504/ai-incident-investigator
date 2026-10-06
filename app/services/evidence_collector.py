import os


def collect_log_evidence(incident_id,log_file_path):
    
    if not os.path.exists(log_file_path):
        raise FileNotFoundError("Log file does not exist")
    
    with open(log_file_path, "r") as file:
        lines = file.readlines()

    error_index = None

    for i in range(len(lines)-1,-1,-1):
        if "ERROR" in lines[i]:
            error_index = i
            break;

    if error_index is None:
        return {
            "source": "application_logs",
            "content": "No ERROR found in application logs",
            "incident_id": incident_id
        }

    start = max(0, error_index - 5)
    end = min(len(lines), error_index + 6)

    relevant_lines = lines[start:end]

    content = "".join(relevant_lines)

    error_line = lines[error_index]

    errors = error_line.split()

    timestamp = errors[0] + " " + errors[1]
    severity = errors[2]
    message = " ".join(errors[3:])
    

    return {
        "source" : "application_logs",
        "severity" : severity,
        "message" : message,
        "timestamp" : timestamp,
        "content" : content,
        "incident_id" : incident_id
    }


    