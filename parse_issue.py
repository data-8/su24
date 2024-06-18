import os
import re

issue_body = os.getenv('ISSUE_BODY')

lecture_number = re.search(r'Lecture Number: (\d+)', issue_body).group(1).strip()
demo = re.search(r'Demo: (.+)', issue_body).group(1).strip()
slides = re.search(r'Slides: (.+)', issue_body).group(1).strip()

print(f"::set-env name=Lecture_Number::{lecture_number}")
print(f"::set-env name=Demo::{demo}")
print(f"::set-env name=Slides::{slides}")
