import os
import requests

def update_svg():
    # 1. Fetch real-time data (Example: GitHub Stars)
    username = "YOUR_GITHUB_USERNAME"
    response = requests.get(f"https://github.com{username}/repos")
    stars = sum(repo['stargazers_count'] for repo in response.json())
    
    # 2. Define your dynamic values
    data = {
        "{os_val}": "Linux (Ubuntu 22.04)",
        "{uptime_val}": "Always Online",
        "{shell_val}": "zsh / python",
        "{stars_val}": str(stars)
    }

    # 3. Read template and replace placeholders
    with open("template.svg", "r") as f:
        content = f.read()
    
    for key, value in data.items():
        content = content.replace(key, value)

    # 4. Save the final SVG
    with open("profile-stats.svg", "w") as f:
        f.write(content)

if __name__ == "__main__":
    update_svg()
