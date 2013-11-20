import IPython
import shutil
import os
import sys


"""
	This script will modify the default profile of iPython to automatically import Rosetta and toolbox methods everytime a new interactive iPython shell is started. It uses iPythonStartupMod.ipy which is dropped into the startup folder of default profile.
	To modify the start up behavior of iPython, you can add or remove lines to the file iPythonStartupMod.ipy and then RUN THIS SCRIPT AGAIN to apply your changes.
	WARNING: when running script again, current startup file will be overwritten if user selects yes.
	"""


def confirm(prompt=None, resp=False):
    """
		A method that prompts the user for confimration when file already exists.
		"""
    if resp:
        prompt = '%s [%s]|%s: ' % (prompt, 'y', 'n')
    else:
        prompt = '%s [%s]|%s: ' % (prompt, 'n', 'y')
	
    while True:
        ans = raw_input(prompt)
        if not ans:
            return resp
        if ans not in ['y', 'Y', 'n', 'N']:
            print 'please enter y or n.'
            continue
        if ans == 'y' or ans == 'Y':
            return True
        if ans == 'n' or ans == 'N':
            return False

#create default profile if it isn not already present
os.system("python ipython.py profile create")

#find and store the ipython working directory; modify to go directly to startup dir
j = IPython.utils.path.get_ipython_dir()
location_of_startups = j + '/profile_default/startup'

#find and save the current directory; modify to copy current iPythonStartupMod.ipy
current_directory = os.getcwd()
location_of_startup_file = current_directory + "/iPythonStartupMod.ipy"

continutation_question = 'A startup file already exists and will be overwritten, would you still like to continue? \n \'y\' to continue; default is \'n\' to quit.'

if os.path.isfile(location_of_startups + "/iPythonStartupMod.ipy"):
	if confirm(prompt = continutation_question, resp = False) == False:
		print "\nProcess quit, original startup file was not modified with new startup file."
		sys.exit(0)
	print "\n...continuing with startup update..."


#copy file to startups folder
shutil.copy(location_of_startup_file, location_of_startups)

print "\nStartup file updated successfully!"
print "File was copied to %s" % (location_of_startups)
