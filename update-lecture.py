import os
import re
import subprocess

# Get environment variables
issue_body = os.getenv('ISSUE_BODY')
config_file = "_config.yml"
issue_number = os.getenv('GITHUB_ISSUE_NUMBER')

# Parse issue body
lecture_number = re.search(r'Lecture Number: (\d+)', issue_body).group(1).strip()
demo = re.search(r'Demo: (.+)', issue_body).group(1).strip()
slides = re.search(r'Slides: (.+)', issue_body).group(1).strip()

# Create demo link if demo is not 'None'
if demo.lower() != "none":
    demo_link = f"https://data8.datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https://github.com/data-8/materials-su24&urlpath=tree/materials-su24/lec/{demo}/{demo}.ipynb&branch=main"
else:
    demo_link = "None"

# Replace text in config file
with open(config_file, 'r') as file:
    config_content = file.read()

slide_line = f"    slide{lecture_number}: \"Slides\""
demo_line = f"    demo{lecture_number}: \"&#8226; Demo\""

if demo_link == "None":
    demo_replacement = f"    demo{lecture_number}: \"\""
else:
    demo_replacement = f"    demo{lecture_number}: \"&#8226; [Demo]({demo_link})\""

slides_replacement = f"    slide{lecture_number}: \"[Slides]({slides})\""

config_content = config_content.replace(slide_line, slides_replacement)
config_content = config_content.replace(demo_line, demo_replacement)

with open(config_file, 'w') as file:
    file.write(config_content)

# Git operations
subprocess.run(["git", "config", "--global", "user.name", "jonathanferrari"])
subprocess.run(["git", "config", "--global", "user.email", "jonathanferrari@berkeley.edu"])
subprocess.run(["git", "add", config_file])
subprocess.run(["git", "commit", "-m", f"Update _config.yml for lecture {lecture_number} materials"])
subprocess.run(["git", "push"])

# Writing to environment file
with open(os.getenv('GITHUB_ENV'), 'a') as env_file:
    env_file.write(f"Lecture_Number={lecture_number}\n")
    env_file.write(f"Demo={demo}\n")
    env_file.write(f"Demo_Link={demo_link}\n")
    env_file.write(f"Slides={slides}\n")

# Create GitHub issue comment and close issue
if demo_link == "None":
    demo_text = "None"
else:
    demo_text = f"&#8226; [Demo]({demo_link})"

comment_body = f"Updated `_config.yml` for lecture {lecture_number}:\n- Slides: [Slides]({slides})\n- Demo: {demo_text}"

subprocess.run(["gh", "issue", "comment", issue_number, "--body", comment_body])
subprocess.run(["gh", "issue", "close", issue_number])