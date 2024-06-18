import os
import re

issue_body = os.getenv('ISSUE_BODY')

lecture_number = re.search(r'Lecture Number: (\d+)', issue_body).group(1).strip()
demo = re.search(r'Demo: (.+)', issue_body).group(1).strip()
slides = re.search(r'Slides: (.+)', issue_body).group(1).strip()

with open(os.getenv('GITHUB_ENV'), 'a') as env_file:
    env_file.write(f"Lecture_Number={lecture_number}\n")
    env_file.write(f"Demo={demo}\n")
    env_file.write(f"Slides={slides}\n")
