# Pytest_Test_suite_sequence
Pytest plugin to mention testsuite sequnece along with the name of the test case

Strictly follow the steps given below. 


1. Make sure that the json file is placed inside the exact location mentioned after the parser "--suite_cfg" 

    example : --suite_cfg ./test_suite_sequence.json

2. Make sure that the parser key word is "--suite_name" followed by the test suite name, mentioned in the json file only

    example : --suite functionality


3. Sample pytest Cmd:

        pytest ./test -p no:randomly --suite_cfg ./test_suite_sequence.json --suite_name throughput

    where,
    "./test" - test folder in the current execution folder
    "throughput" - suite name mentioned in the json file.
    "-p no:randomly" - pytest-randomly cmd

4. sample json file.

    {

    throughput":{"CNXA_test3":2,"CNXA_test2":1,"CNXA_test":3}

    }