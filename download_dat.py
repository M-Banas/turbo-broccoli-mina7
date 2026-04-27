from dotenv import load_dotenv
import os
import gdown

load_dotenv()

file_id = os.getenv("DRIVE_FILE_ID")

url = f"https://drive.google.com/uc?id={file_id}"

os.makedirs("data", exist_ok=True)
gdown.download(url, "data/data.csv", quiet=False)