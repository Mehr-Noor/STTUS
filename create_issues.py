import pandas as pd
import requests

# ========= CONFIG =========
GITHUB_TOKEN = "hp_Z6iKyYSlNnxvIRhEzbGTorbFpoTx2y1lDSgx"
OWNER = "MehrNoor"
REPO = "Intelligent-Ultrasound-Dictation-System"
CSV_FILE = "issues_import (2).csv"
# ==========================

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

df = pd.read_csv(CSV_FILE)

for index, row in df.iterrows():
    issue_data = {
        "title": row["Title"],
        "body": row["Body"],
        "labels": [label.strip() for label in row["Labels"].split(",")],
        "assignees": [row["Assignee"]]
    }

    response = requests.post(
        f"https://api.github.com/repos/{OWNER}/{REPO}/issues",
        json=issue_data,
        headers=headers
    )

    if response.status_code == 201:
        print(f"✅ Created issue: {row['Title']}")
    else:
        print(f"❌ Failed: {row['Title']} -> {response.text}")
