# Step 1: Initialize a Git repository (if not already initialized)
git init

# Step 2: Add all files to the staging area
git add .

# Step 3: Commit the changes
git commit -m "Initial commit"

# Step 4: Add the remote repository URL (replace with your GitHub repository URL)
git remote add origin https://github.com/your-username/your-repository.git

# Step 5: Push the changes to the GitHub repository
git branch -M main  # Rename the branch to 'main' if needed
git push -u origin main