import subprocess, os

os.chdir(r"C:\Users\tale0\Desktop\class_event_signup")

# Step 1: git init
r = subprocess.run(["git", "init"], capture_output=True, text=True)
print("git init:", r.stdout.strip(), r.stderr.strip())

# Step 2: git branch -M main
r = subprocess.run(["git", "branch", "-M", "main"], capture_output=True, text=True)
print("git branch -M main:", r.stdout.strip(), r.stderr.strip())

# Step 3: git add .
r = subprocess.run(["git", "add", "."], capture_output=True, text=True)
print("git add .:", r.stdout.strip(), r.stderr.strip())

# Step 4: git status
r = subprocess.run(["git", "status", "--short"], capture_output=True, text=True)
print("git status:", r.stdout.strip())

# Step 5: git commit
r = subprocess.run(["git", "commit", "-m", "initial Flask event signup app"], capture_output=True, text=True)
print("git commit:", r.stdout.strip(), r.stderr.strip())

# Step 6: git remote add origin
r = subprocess.run(["git", "remote", "add", "origin", "https://github.com/litinfyao/class_event_signup.git"], capture_output=True, text=True)
print("git remote add:", r.stdout.strip(), r.stderr.strip())

# Step 7: git remote -v
r = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True)
print("git remote -v:", r.stdout.strip())

# Step 8: git push
r = subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True, text=True)
print("git push stdout:", r.stdout.strip())
print("git push stderr:", r.stderr.strip())
print("git push returncode:", r.returncode)
