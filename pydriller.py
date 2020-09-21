# Learning PyDriller, Python Git repository data mining tool

import pydriller

def test_local():
	for commit in pydriller.RepositoryMining('/home/tim/projects/linux-tips').traverse_commits():
		print('Hash {}, Author {}'.format(commit.hash, commit.author.name))

if __name__ == "__main__":
	test_local()
