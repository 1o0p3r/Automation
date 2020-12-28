[WebDriver Setup - Linux]
Download geckodriver
Move geckodriver.exe to /usr/local/bin directory

[WebDriver Setup - Windows]
TO DO

[Python Setup - Pipenv]
To install pipenv(Skip if already have) : pip install pipenv
Get dependencies : Install pip install --dev

[Dependencies]
pytest
pytest-html
selenium


[Execution of TestCases]
pytest -s -v testCases/{test_case_filename}.py

[Execution of TestCases with Report]
pytest -s -v --html=Reports/{file_name}.html testCases/{test_case_filename}.py

Note: Remove flag -s if intend to capture logs including ones that do not have error

