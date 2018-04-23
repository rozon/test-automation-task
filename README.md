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

# Questions

3. In a typical test scenario not all input values can be tested. Are there specific value
ranges to test for each operation and explain why the defined range is important?

Answer: in the selection of variables there is a method called boundary value partitioning, basically
it is to look for the expected values and the edge conditions of each variable.

It is important because we must consider the concurrent data entry and the correct isolation between
each session that is manipulating the values of the variables.