import os
import random
import subprocess
from datetime import datetime, timedelta

def get_positive_int(prompt, default=20):
    while True:
        try:
            user_input = input(f"{prompt} (default {default}): ")
            if not user_input.strip():
                return default
            value = int(user_input)
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def random_date_in_year(year):
    start_date = datetime(year, 1, 1)
    days_in_year = 366 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 365
    random_days = random.randint(0, days_in_year - 1)
    random_seconds = random.randint(0, 86399) 
    commit_date = start_date + timedelta(days=random_days, seconds=random_seconds)
    return commit_date

def make_commit(date, repo_path, filename, message="graph-greener!"):
    filepath = os.path.join(repo_path, filename)
    with open(filepath, "a") as f:
        f.write(f"Commit at {date.isoformat()}\n")
    
    subprocess.run(["git", "add", filename], cwd=repo_path)
    env = os.environ.copy()
    date_str = date.strftime("%Y-%m-%dT%H:%M:%S")
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    subprocess.run(["git", "commit", "-m", message], cwd=repo_path, env=env)

def main():
    print("="*60)
    print("Welcome to samz200p GitHub Graph Generator")
    print("="*60)

    # আপনার তথ্যগুলো এখানে সেট করা হয়েছে
    username = "samz200p"
    repo_name = "New"
    token = "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"

    num_commits = get_positive_int("How many commits do you want to make", 20)
    target_year = get_positive_int("Which year do you want to add contributions for?", 2020)
    
    repo_path = "." 
    filename = "data.txt"

    # লোকাল গিট কনফিগ আপডেট (পুরনো আইডি ওভাররাইড করার জন্য)
    subprocess.run(["git", "config", "user.name", username], cwd=repo_path)
    subprocess.run(["git", "config", "user.email", f"{username}@users.noreply.github.com"], cwd=repo_path)

    print(f"\nMaking {num_commits} commits for the year {target_year}...")

    for i in range(num_commits):
        commit_date = random_date_in_year(target_year)
        print(f"[{i+1}/{num_commits}] Committing at {commit_date.strftime('%Y-%m-%d %H:%M:%S')}")
        make_commit(commit_date, repo_path, filename)

    # টোকেন ব্যবহার করে সরাসরি পুশ ইউআরএল তৈরি
    remote_url = f"https://{token}@github.com/{username}/{repo_name}.git"
    
    print("\nUpdating remote URL and pushing to GitHub...")
    subprocess.run(["git", "remote", "set-url", "origin", remote_url], cwd=repo_path)
    
    # প্রথমে 'main' ব্রাঞ্চে পুশ করার চেষ্টা করবে
    print("Trying to push to 'main' branch...")
    push_main = subprocess.run(["git", "push", "-u", "origin", "main"], cwd=repo_path)
    
    # যদি 'main' না থাকে বা এরর দেয়, তবে 'master' ব্রাঞ্চে চেষ্টা করবে
    if push_main.returncode != 0:
        print("\n'main' branch failed, trying 'master' branch...")
        # লোকাল ব্রাঞ্চকে master হিসেবে রিনেম করে পুশ করবে
        subprocess.run(["git", "branch", "-M", "master"], cwd=repo_path)
        subprocess.run(["git", "push", "-u", "origin", "master"], cwd=repo_path)

    print("\n✅ Process finished! Check your profile: https://github.com/samz200p")

if __name__ == "__main__":
    main()
