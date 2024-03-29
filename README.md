# Appium Python Example

## Articles written about this project

## Project Setup

* Clone the project
* Navigate to the project directory

* Install pytest-html-reporter by running the following command:

```
pip install pytest-html-reporter
```

* Install Selenium by running the following command:

```
pip install selenium
```

* Install requirements (dependencies) by running the following command:

```
pip install -r requirements.txt 
```

* you still will need to install Appium, UiAutomator2, environment variables 

## Running Tests with report

```
python -m pytest tests_wifi_functionality/ --html-report=./reports
```

When no browser was selected then chromium will be used.

* Run tests:

```
pytest
```

## Viewing Test Results

* View results locally by navigate to the project folder under the main folder of the project run the command:
```
allure serve
```


## View Help And Custom CLI Options

```
pytest --help
```