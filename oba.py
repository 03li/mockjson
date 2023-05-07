import re

def extract_data(file_content):
    pattern = r"LIGW-(\d+).*?OBA-(\d+).*?EMA-(\d+)"
    matches = re.findall(pattern, file_content, re.DOTALL)
    
    result = ''
    for match in matches:
        result += "{\"snb\":"+ match[0] +",\"OBA\":"+match[1]+",\"EMA\":"+match[2]+"},\n"
    
    return result

# Read the file content from a file
file_path = "/content/netema.log"
with open(file_path, "r") as file:
    file_content = file.read()

# Extract the data
extracted_data = extract_data(file_content)
print(extracted_data)
