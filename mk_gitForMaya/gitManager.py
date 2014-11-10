__author__ = 'Marley Kudiabor'

import pymel.core
import git
import unittest
import json
import os

workingDirectory = pm.workspace.path
gitDirectory = workingDirectory + "/.git"
if not os.path.exists(workingDirectory):
	os.mkdir(workingDirectory)
	if not os.path.exists(gitDirectory):
		os.mkdir(gitDirectory)


def startGit():
	repo = git.Repo.create(gitDirectory)

def save():
    pass

class GitSaver():

	def saveAsGit(self, gitManager):
		pm.saveFile( f = True, type = "mayaAscii")
		gitManager.Commit

	def saveAndSaveHardBackupGit(self):
		pass

	def autoSaveGit(self):
		pass

	def gitTag(self):
		pass
