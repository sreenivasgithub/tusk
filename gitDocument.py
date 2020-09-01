# git clone url
# git status
# git add filename.py
# git commit -m 'message'
# git push
#
# Undoing/Reverting/Resetting CODE:----
#
# Undoing:-- before adding, do you want to undo your changes in a file
# git status
# git checkout -- filename.py
# git checkout -- .    [do you want to undo your changes in a Multiple files]
#
# Reverting:--
# git status
# git add filename.py
# git commit -m 'message'
# git log          [it will get commit history wit ids]
# git revert id    [id: commit id]
# git revert -n id [changes are cleared but not commited]
#
# Resetting:--
# git log
# git reset --hard id

# Create new Branch & Merge branch & delete branch
# Create Branch:--
# git branch   [we will get list of branches]
# git branch branchname
# git checkout branchname  [switch to branch]
# git checkout master  [switch to masterbranch]

# Merge:--
# git merge branchname

# Delete:--
# git branch -d branchname
#------------------------------------

# git checkout -b branchname [creating a new branch and active that branch]
