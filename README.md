* The project is called IoT Smart Attendance System.
* Use-fullness:
* Can be used to automatically track employees sign in and sign out.
* Can be used in colleges, universities to track student sign in and sign outs.
* Homes to unlock the doors automatically when the owner turns up etc.
* ##################################### *
* Software:
* Python 3.5
* raspberry linux bash
* Python IDLE
* Python libraries.
* Py Camera installation.
* ##################################### *
* Hardware:
* latest raspberry pi (raspberry pi 3 or new )
* USB or bluetooth mouse
* USB keyboard
* External monitor
* Py Camera
* ##################################### *
* File details:
* capture.py, predict.py, train.py - python files for the model.
* raspberry_configuration_file - Configuration file for raspberry system.
* dataset.zip, trainer.zip - zipped folders.
* haarcascade_frontalface_default.xml - harcascade file for facial recognition.

* ##################################### *
* How to reproduce the project?
* Install all the software required for a raspberry cam to work. (at the moment the installation files are not provided.)
* Make sure the Py Cam is working before proceeding.
* Download all the files and folders and extract the folders.
* Install all the packages required for the python (preferably create a new environment)
* Using the raspberry bash open the python 3.5 environment.
* First call the capture.py from the python terminal.
* This will capture the images of the person in front of the Py cam.
* Use train.py to train the model on the captured images.
* Use predict.py to predict the person in front of the camera.
* ##################################### *
* Planned new functionalities for phase 2: 
* Add the timestamps and data to a database
* Provide analytics on the data.
* Add installation files.
