# Pytest_Test_suite_sequence
Pytest plugin to execute testsuite in a user defined sequnece using a json file.


Strictly follow the steps given below. 

1. Make sure that the json file is placed inside the exact location mentioned after the parser "--suite_cfg" 

    example : --suite_cfg ./test_suite_sequence.json

2. Make sure that the parser keyword "--suite_name" is followed by the test_suite name, mentioned in the json file.

    example : --suite functionality

3. Sample pytest Cmd:

        pytest ./test --suite_cfg ./test_suite_sequence.json --suite_name throughput

    where,
    "./test" - test folder in the current execution folder
    "throughput" - suite name mentioned in the json file.

4. Sample json file.

    please reffer the sample.json file
    
# Pytest_Precondition

Pytest plugin to execute precondition cases before suite execution

Strictly follow the steps given below. 

1. Make sure that the Precondition Test cases are placed along with the other test cases

2. Make sure that the parser keyword "--precond" is followed by an array of Precondition Testcase
   without any additional spaces.

    example : --precond [CNXA_1234,CNXA_5678] 

3. Sample pytest Cmd:

        pytest ./test --precond [CNXA_1234,CNXA_5678]

    where,
    "./test" - test folder in the current execution folder

4. All the precondition testcases must be marked with the following marker, after importing pytest.

   " @pytest.mark.precond "

5. This plugin also works along with the pytest suite plugin.
