# Gemini Testing Assignment- Automate the Institutional Client Registration form in Gemini’s sandbox environment.

The project will help to run UI test cases using pytest Framework and generate the reports using allure report.

## Features

- Run UI test cases using python-pytest.
- Generate Allure report, which gives a good GUI representation of test execution output.


## Software Installation
Below instructions will help you download and install required software on Windows machine to run the project -

1) Python
    - Download and install the Python 3.x as per the instructions mentioned on- https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html
    - Go to Control Panel ->System Variable and set path for Python and Python ->Scripts folder.
    - Open Command prompt and run python --version to verify the installation. 

2) Allure
    - Open link - https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/
    - And download the latest version .zip file
    - Unzip and copy the folder to desired directory
    - Go to Control Panel ->System Variable and set path for allure bin folder.
    
    This link will help to understand more about the Allure installation - https://docs.qameta.io/allure/.

## Set up the project to run

#### Download Project
- Download the project from the repository

#### Activate the Virtual Envrionment
- Go to command prompt and navigate to the project folder using command - cd {project_folder_path}
- Run .\venv\Scripts\activate

#### Install python libraries
On the command prompt after activating the venv, run the below commands - 
- pip install selenium
- pip install pytest
- pip install allure-pytest

#### Verification of the libraries
- Run command - pip list, all the newly installed libraries should be listed.

## Execute the Project
- After python libraries verification on the command prompt run **pytest --alluredir reports/**
- This should run all the tests, giving the total number of Steps Passed, Failed, skipped etc. information in the terminal window.

## View the report
- On the terminal run **allure serve reports**

Allure Report should be populated in your browser.
