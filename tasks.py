from invoke import run, task
from invoke.exceptions import Failure

@task
def test():
	run("python -m unittest discover test")

@task
def freeze():
	run("pip freeze > requirements.txt")

@task(post=[freeze])
def install(pkg, upgrade=False):
	upgrade = "--upgrade" if upgrade else ""
	run("pip install " + pkg + " " + upgrade, pty=True)

@task(post=[freeze])
def uninstall(pkg):
	run("pip uninstall " + pkg, pty=True)

@task
def setup():
	run("pip install -r requirements.txt", pty=True)

@task
def rerun():
	 try:
	 	return run("rerun -xp '**/*.py' invoke test").exited
	 except Failure as e:
	 	print "The tool rerun isnt installed, installing it now, please try again."
	 	run("gem install rerun --no-ri --no-rdoc")

@task
def register_pypi(test=False):
	pypi = "pypi"
	if test:
		pypi = pypi + "test"
	run("python setup.py register -r " + pypi)

@task
def upload_pypi(test=False):
	pypi = "pypi"
	if test:
		pypi = pypi + "test"
	run("python setup.py sdist upload -r " + pypi)