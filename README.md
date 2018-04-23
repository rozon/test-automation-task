# test-automation-task

Command Line Instructions:
---
```bash

# install pip requirements:
$ pip install -r requirements.txt

# install allure reports
$ brew untap qameta/allure
$ brew update
$ brew install allure

# run tests locally:
$ pytest smoke/test_api.py -v --alluredir=test-report

# run allure reports
$ allure serve test-report/
```

You can use one of the following ways to read tests reports

* Read pytest test result on the command line:

![Command Line](https://github.com/rozon/test-automation-task/raw/master/.github/readme_img_01.png)

![Command Line](https://github.com/rozon/test-automation-task/raw/master/.github/readme_img_02.png)

* Read test results on allure test report:

![Allure Report](https://github.com/rozon/test-automation-task/raw/master/.github/readme_img_03.png)

![Allure Report](https://github.com/rozon/test-automation-task/raw/master/.github/readme_img_04.png)