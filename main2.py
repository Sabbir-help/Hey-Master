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

# নতুন ফাংশন: নির্দিষ্ট বছরের র‍্যান্ডম তারিখ তৈরি করার জন্য
def random_date_in_year(year):
    start_date = datetime(year, 1, 1)
    # বছরের শেষ দিন নির্ধারণ (৩৬৫ বা ৩৬৬ দিন)
    days_in_year = 366 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 365
    random_days = random.randint(0, days_in_year - 1)
    random_seconds = random.randint(0, 86399) # এক দিনের মোট সেকেন্ড
    commit_date = start_date + timedelta(days=random_days, seconds=random_seconds)
    return commit_date

def make_commit(date, repo_path, filename, message="graph-greener!"):
    filepath = os.path.join(repo_path, filename)
    with open(filepath, "a") as f:
        f.write(f"Commit at {date.isoformat()}\n")
    
    # Git commands
    subprocess.run(["git", "add", filename], cwd=repo_path)
    env = os.environ.copy()
    date_str = date.strftime("%Y-%m-%dT%H:%M:%S")
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    subprocess.run(["git", "commit", "-m", message], cwd=repo_path, env=env)

def main():
    print("="*60)
    print("Welcome to graph-greener - GitHub Year-Wise Commit Generator")
    print("="*60)

    num_commits = get_positive_int("How many commits do you want to make", 20)
    
    # বছর ইনপুট নেওয়ার অপশন
    target_year = get_positive_int("Which year do you want to add contributions for? (e.g. 2018)", 2020)
    
    repo_path = input("Enter the path to your local git repository (default .): ") or "."
    filename = input("Enter the filename to modify (default data.txt): ") or "data.txt"

    print(f"\nMaking {num_commits} commits for the year {target_year}...")

    for i in range(num_commits):
        commit_date = random_date_in_year(target_year)
        print(f"[{i+1}/{num_commits}] Committing at {commit_date.strftime('%Y-%m-%d %H:%M:%S')}")
        make_commit(commit_date, repo_path, filename)

    print("\nPushing commits to your remote repository...")
    subprocess.run(["git", "push"], cwd=repo_path)
    print("✅ All done! Check your GitHub graph for the specific year.")

if __name__ == "__main__":
    main()
