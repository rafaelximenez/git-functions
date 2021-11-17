from src.gitfunctions.gitfunctions import Git

git = Git(repo_path='.')
git.check_updates()