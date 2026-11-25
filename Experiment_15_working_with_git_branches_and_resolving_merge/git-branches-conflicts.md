# Git Branches and Merge Conflicts

Demonstrates creating a feature branch, pulling latest main, merging, resolving conflicts, committing and pushing.

## Commands
```
git checkout -b feature-branch
# edit files
git add .
git commit -m "feature change"
git checkout main
git pull origin main
git checkout feature-branch
git merge main
# resolve conflicts
git add .
git commit -m "Resolve merge conflict"
git push origin feature-branch
```
