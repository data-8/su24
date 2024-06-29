import os
import re
import subprocess

# Get environment variables
issue_body = os.getenv('ISSUE_BODY')
issue_number = os.getenv('GITHUB_ISSUE_NUMBER')

# Parse issue body for worksheet number and link
worksheet_number = re.search(r'Worksheet Number: (\d+)', issue_body).group(1).strip()
worksheet_link = re.search(r'Worksheet Link: (.+)', issue_body).group(1).strip()

# Construct the link in the desired format
worksheet_link_formatted = f"[Lab {worksheet_number} Worksheet]({worksheet_link})"

# Replace text in appropriate file or location (modify as per your repo structure)
config_file = "_config.yml"
with open(config_file, 'r') as file:
    config_content = file.read()

worksheet_line = f"    wksht{worksheet_number}:"

worksheet_replacement = f"    wksht{worksheet_number}: \"{worksheet_link_formatted}\""

config_content = re.sub(f"{worksheet_line}.*", worksheet_replacement, config_content)

with open(config_file, 'w') as file:
    file.write(config_content)

# Git operations
subprocess.run(["git", "config", "--global", "user.name", "jonathanferrari"])
subprocess.run(["git", "config", "--global", "user.email", "jonathanferrari@berkeley.edu"])
subprocess.run(["git", "add", config_file])
subprocess.run(["git", "commit", "-m", f"Update _config.yml for worksheet {worksheet_number} link"])
subprocess.run(["git", "push"])

# Writing to environment file (optional)
# Modify based on your environment setup if necessary

# Create GitHub issue comment and close issue
comment_body = f"Updated `_config.yml` for worksheet {worksheet_number} link:\n- Worksheet: {worksheet_link_formatted}"

subprocess.run(["gh", "issue", "comment", issue_number, "--body", comment_body])
subprocess.run(["gh", "issue", "close", issue_number])
