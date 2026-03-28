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

    # আপনার নতুন তথ্যগুলো এখানে দেওয়া আছে
    username = "samz200p"
    repo_name = "New"
    token = "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" # আপনার দেওয়া টোকেন

    num_commits = get_positive_int("How many commits do you want to make", 20)
    target_year = get_positive_int("Which year do you want to add contributions for?", 2020)
    
    repo_path = "." 
    filename = "data.txt"

    # লোকাল কনফিগ অটো আপডেট (যাতে আগের আইডি sabbiritdm বাধা না দেয়)
    subprocess.run(["git", "config", "user.name", username], cwd=repo_path)
    subprocess.run(["git", "config", "user.email", "samz200p@users.noreply.github.com"], cwd=repo_path)

    print(f"\nMaking {num_commits} commits for the year {target_year}...")

    for i in range(num_commits):
        commit_date = random_date_in_year(target_year)
        make_commit(commit_date, repo_path, filename)

    # টোকেন ব্যবহার করে অটোমেটিক রিমোট সেটআপ এবং পুশ
    remote_url = f"https://{username}:{token}@github.com/{username}/{repo_name}.git"
    print("\nUpdating remote URL and pushing to GitHub...")
    
    subprocess.run(["git", "remote", "set-url", "origin", remote_url], cwd=repo_path)
    
    # সাধারণত নতুন রেপোজিটরিতে 'main' ব্রাঞ্চ থাকে, সেটি চেষ্টা করবে
    push_result = subprocess.run(["git", "push", "-u", "origin", "main"], cwd=repo_path)
    
    # যদি 'main' না থাকে, তবে 'master' ব্রাঞ্চে চেষ্টা করবে
    if push_result.returncode != 0:
        subprocess.run(["git", "push", "-u", "origin", "master"], cwd=repo_path)

    print("\n✅ Process finished! check https://github.com/samz200p")

if __name__ == "__main__":
    main()
