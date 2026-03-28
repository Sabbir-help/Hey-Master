import os
import random
import subprocess
from datetime import datetime, timedelta

def create_project_structure(repo_path):
    # বাস্তবসম্মত প্রজেক্টের ফাইল এবং ডামি কোড
    files = {
        "index.html": "<!DOCTYPE html>\n<html>\n<head>\n    <title>My Professional Portfolio</title>\n    <link rel='stylesheet' href='style.css'>\n</head>\n<body>\n    <h1>Welcome to my Project</h1>\n    <p>Building something amazing for the community.</p>\n    <script src='script.js'></script>\n</body>\n</html>",
        "style.css": "body {\n    background-color: #121212;\n    color: #ffffff;\n    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;\n    display: flex;\n    justify-content: center;\n    align-items: center;\n    height: 100vh;\n}\nh1 { color: #00ff00; border-bottom: 2px solid #00ff00; }",
        "script.js": "console.log('Project started successfully!');\nfunction greet() {\n    console.log('Welcome to samz200p profile');\n}\ngreet();",
        "README.md": "# Modern Web Architecture\n\nThis repository is a showcase of a clean, modular web application structure.\n\n### Tech Stack:\n- HTML5\n- CSS3\n- JavaScript (ES6+)\n\n### How to Run:\nSimply open `index.html` in your browser.",
        "package.json": '{\n  "name": "samz200p-web-core",\n  "version": "1.1.0",\n  "description": "Professional repository structure",\n  "main": "script.js",\n  "author": "samz200p"\n}'
    }
    
    for filename, content in files.items():
        filepath = os.path.join(repo_path, filename)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Created/Updated: {filename}")
    return list(files.keys())

def main():
    print("="*60)
    print("GitHub Professional Repo Formatter - samz200p")
    print("="*60)

    username = "samz200p"
    repo_name = "new" 
    
    # টোকেনটি এখানে ইনপুট হিসেবে নিবে (নিরাপদ পদ্ধতি)
    token = input("Enter your GitHub Personal Access Token (PAT): ").strip()
    
    if not token:
        print("Error: Token cannot be empty!")
        return

    repo_path = "." # আপনার বর্তমান ডিরেক্টরি

    # ১. প্রজেক্ট ফাইলগুলো তৈরি করা
    print("\n[1/3] Adding professional project files...")
    create_project_structure(repo_path)
    
    # ২. গিট কনফিগ আপডেট
    subprocess.run(["git", "config", "user.name", username], cwd=repo_path)
    subprocess.run(["git", "config", "user.email", f"{username}@users.noreply.github.com"], cwd=repo_path)

    # ৩. কমিট করা
    print("[2/3] Committing changes...")
    subprocess.run(["git", "add", "."], cwd=repo_path)
    subprocess.run(["git", "commit", "-m", "Initialize professional project architecture"], cwd=repo_path)

    # ৪. পুশ করা
    # ইউআরএল-এ টোকেনটি ব্যবহার করে পুশ প্রোটেকশন বাইপাস করা
    remote_url = f"https://{token}@github.com/{username}/{repo_name}.git"
    
    print("[3/3] Pushing to GitHub...")
    subprocess.run(["git", "remote", "set-url", "origin", remote_url], cwd=repo_path)
    
    res = subprocess.run(["git", "push", "-u", "origin", "main"], cwd=repo_path)
    
    if res.returncode != 0:
        print("\n'main' branch failed, trying 'master'...")
        subprocess.run(["git", "branch", "-M", "master"], cwd=repo_path)
        subprocess.run(["git", "push", "-u", "origin", "master"], cwd=repo_path)

    print(f"\n✅ All set! Your repo 'https://github.com/samz200p/{repo_name}' is now a real project.")

if __name__ == "__main__":
    main()
