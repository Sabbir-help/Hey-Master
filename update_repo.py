import os
import random
import subprocess
from datetime import datetime, timedelta

def create_project_structure(repo_path):
    # বাস্তবসম্মত প্রজেক্টের ফাইল এবং কিছু ডামি কোড
    files = {
        "index.html": "<!DOCTYPE html>\n<html>\n<head>\n    <title>My Professional Portfolio</title>\n    <link rel='stylesheet' href='style.css'>\n</head>\n<body>\n    <h1>Welcome to my Project</h1>\n    <script src='script.js'></script>\n</body>\n</html>",
        "style.css": "body {\n    background-color: #121212;\n    color: #ffffff;\n    font-family: Arial, sans-serif;\n}\nh1 { color: #00ff00; }",
        "script.js": "console.log('Project started successfully!');\nfunction init() {\n    alert('Welcome to my GitHub Project');\n}\n// init();",
        "README.md": "# Modern Web Project\n\nThis repository contains a professional web-based project architecture.\n\n### Features:\n- Clean Codebase\n- Responsive Design\n- Optimized Assets",
        "package.json": '{\n  "name": "my-project",\n  "version": "1.0.0",\n  "description": "A real professional project",\n  "main": "script.js"\n}'
    }
    
    for filename, content in files.items():
        filepath = os.path.join(repo_path, filename)
        # যদি ফাইলটি আগে থেকে না থাকে তবেই তৈরি করবে
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                f.write(content)
            print(f"Created: {filename}")
    return list(files.keys())

def main():
    username = "samz200p"
    repo_name = "New" 
    token = "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"
    
    repo_path = "." # আপনার পিসিতে যে ফোল্ডারে 'New' রেপোটি আছে

    # ১. প্রজেক্ট ফাইলগুলো তৈরি করা
    print("Adding real project files to your existing repo...")
    file_list = create_project_structure(repo_path)
    
    # ২. গিট কনফিগ (নিশ্চিত করা যে samz200p হিসেবে পুশ হচ্ছে)
    subprocess.run(["git", "config", "user.name", username], cwd=repo_path)
    subprocess.run(["git", "config", "user.email", f"{username}@users.noreply.github.com"], cwd=repo_path)

    # ৩. সব ফাইল গিট-এ অ্যাড করা
    subprocess.run(["git", "add", "."], cwd=repo_path)
    
    # ৪. একটি "Real" কমিট মেসেজ দেওয়া
    commit_msg = "Initial architecture setup for the project"
    subprocess.run(["git", "commit", "-m", commit_msg], cwd=repo_path)

    # ৫. পুশ করা
    remote_url = f"https://{token}@github.com/{username}/{repo_name}.git"
    subprocess.run(["git", "remote", "set-url", "origin", remote_url], cwd=repo_path)
    
    print("\nPushing real project files to GitHub...")
    res = subprocess.run(["git", "push", "-u", "origin", "main"], cwd=repo_path)
    if res.returncode != 0:
        subprocess.run(["git", "push", "-u", "origin", "master"], cwd=repo_path)

    print(f"\n✅ Done! Now open https://github.com/samz200p/{repo_name} to see the real files.")

if __name__ == "__main__":
    main()
