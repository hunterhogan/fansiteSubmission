fansiteSubmission
=================

Python wrapper for Tyrant Fansite deck simulation and submission

## Installation (Windows)

* Download and install Python 2.7 from http://www.python.org/download/
* For iteratedecks, download and unzpip the latest version from http://www.hunterthinks.com/id/
* For Tyrant Optimizer, download and unzpip the latest version from http://www.hunterthinks.com/to/
* Download and unzip the fansiteSubmission files from https://nodeload.github.com/iteratedecks/fansiteSubmission/zip/master
* For iteratedecks, put the fansiteSubmission folder in the iteratedecks folder
* For Tyrant Optimizer, put the fansiteSubmission folder in the Tyrant Optimizer folder

## Configuring the "Python Wrapper" to submit result from your computer--for iteratedecks

* Open a command prompt (Start -> Cmd)
* Navigate to the iteratedecks directory
* Type "fansiteSubmission-master\fansiteSims.py" at the command line without the quotes
* The program will call you an idiot and then create a fansite_config.txt file in the iteratedecks directory
* There are more steps, see below

## Configuring the "Python Wrapper" to submit result from your computer--for Tyrant Optimizer

* Open a command prompt (Start -> Cmd)
* Navigate to the Tyrant Optimizer directory
* Type "fansiteSubmission-master\fansiteSims.py" at the command line without the quotes
* The program will call you an idiot and then create a fansite_config.txt file in the Tyrant Optimizer directory
* There are more steps, see below

## There are two ways to configure your fansite_config.txt file

* IMPORTANT: each file is a seperate file, if you have tokens for both iteratedeck and Tyrant Optimizer, you must cofigure each file independtly
* Method one: Open fansite_config.txt with notpad or notpad++, add your simulator token, and try not to try break things
* Method two: From the directory of the program you want to configure, type "fansiteSubmission-master\fansiteSims.py -h" at the command line without the quotes
* Read the screen, follow the instructions. 

## How to download and start submitting results

* If you only want to run 10 simulation at a time (lazy punk!), then from the diretory of the simulator progtam, Type "fansiteSubmission-master\fansiteSims.py" at the command line without the quotes
* If you want to fun simulations until reboot your computer to until you tell the simulator to stop, then Type "fansiteSubmission-master\fansiteSims.py --runForever" at the command line without the quotes
* If you didn't see the differnce, then maybe this is not the job for you
* To make your like easier I, hunterhogan, wrote a batch file. It is cleverly called "fansite.bat" and if you installed everthing properly, a copy is located in the of the sim directories
* Double click on the batch file to make it run
* To get it to stop use ctrl+c or ctrl+break or a hammer (The hammer is a joke)

## Yes, it's a text wall, but it is also comprehensive instrctions for two different simulators

* If you can do better, then submit a pull request
