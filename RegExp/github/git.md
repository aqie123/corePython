一： the usage of git and github
	1. git remote -v
	2. git fetch remote
	3. git fetch remote 10-12
	4. git remote show origin
	5. git branch -r  view remote branch
	6. git branch -a  view all branches
	7. git checkout -b newBranch origin/master based fetched branch to create a new branch
	8. git pull origin dev:master   merge remote branch dev to local master
	9. git pull origin dev          merge remote branch to current local branch
	10. Manually establish tracking relationships
		git branch --set-upstream master origin/next (local master auto tracking origin/next)
	11. Deletes the specified remote branch
		git push origin :master && git push origin --delete master 
	12. Delete local branch
		git branch -D master
	13. Pull down branches from remote and merge with local branch
		git pull origin master equals
		git fetch origin master
		git checkout master
		git merge origin/master
	14. Local code library rollback 代码库中的文件完全覆盖本地工作版本
		git reset --hard commit-id 
	15. 保留生产服务器上所做的改动,仅仅并入新配置项
		git stash
		git pull
		git stash pop
		用git diff -w +文件名 来确认代码自动合并的情况
