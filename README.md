fansiteSubmission
=================

This uses Python to connect Tyrant Optimize to the Fansite; it simulates submitted decks and returns the results 

## Installation (Windows)

* Download and install Python 2.7.X (not version 3.X) from http://www.python.org/download/
* Download the latest version of Tyrant Optimize from http://www.hunterthinks.com/to/
* Download the fansiteSubmission source code. Look for the "Download Zip" button.
* Put the source code in folder named "fansiteSubmission-master"
* The fansiteSubmission-master folder must be in the tyrant_optimize folder

## Running for the first time

* Open a command prompt (Start -> Cmd)
* cd into the tyrant_optimize folder
* Call "fansiteSubmission-master\fansiteSims.py"
* It will create a file, fansite_config.txt, in the tyrant_optimize folder
* Open fansite_config.txt, and add your simulator token from the Fansite
* Run fansiteSubmission-master\fansiteSims.py again and it will connect to the Fansite 
* If you do not have the latest XML files, the submission tool will prompt you to update the XML files

## Using fansiteSubmission
* From the tyrant_optimize folder, run fansiteSubmission-master\fansiteSims.py
* The program will download 50 decks, simulate them, return the results, and STOP
* To continuously run fansiteSubmission, type fansiteSubmission-master\fansiteSims.py --runForever
* To stop the fansiteSubmission program, press Ctrl+C
