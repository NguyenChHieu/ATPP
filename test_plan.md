# Test Case Designs
State the values to initialize appropriate `Question` objects required for the test case.
Question 1:
    Type: Short
    Description: "Which is your ex?"
    Correct Answer: "her"
    Marks: 2
Question 2:
    Type: Single choice
    Description: "Which is my favourite subject?"
    Correct Answer: "C"
    Answer Options: "A. 1064," "B. 1112," "C. 1110," "D. 1601"
    Marks: 1
Question 3:
    Type: Multiple choice
    Description: "Which is your ex?"
    Correct Answer: "A, C, D"
    Answer Options: "A. Hanh," "B. VPL," "C. PLinh," "D. Bao Linh"
    Marks: 4

Column descriptions:
* Test ID - Test case identification number
* Description - Type of testcase and brief explanation of test case details
* Inputs - Arguments into the method
* Expected Output - Return values of the method
* Status - pass/fail 

Table 1: Summary of test cases for method `mark_response` for question type `short`

| Test ID | Description                                          | Inputs | Expected Output | Status |
|---------|------------------------------------------------------|--------|-----------------|--------|
| 001     | Positive: user enter the correct answer              | "her"  | 2.0             | pass   |
| ------- | ---------------------------------------------------- | ------ | --------------  | -----  |
| 002     | Negative: user enter the incorrect answer            | "nah"  | 0.0             | pass   |
| ------- | ---------------------------------------------------- | ------ | --------------  | -----  |
| 003     | Negative: user enter the incorrect answer            | "1"    | 0.0             | pass   |


Table 2: Summary of test cases for method `mark_response` for question type `single`

| Test ID | Description                                 | Inputs | Expected Output | Status |
|---------|---------------------------------------------|--------|-----------------|--------|
| 004     | Positive: user enter the correct answer     | "C"    | 1.0             |  pass  |
| ------- | ---------------------------------------     | ------ | --------------  |--------|
| 005     | Negative: user enter the incorrect answer   | "A"    | 0.0             |  pass  |
| ------- | ---------------------------------------     | ------ | --------------  | -------|
| 006     | Negative: user enter invalid answer         | "hi"   | 0.0             |  pass  |
| ------- | ---------------------------------------     | ------ | --------------  | -------|
| 013     | Negative: user enter lowercase answer       | "a"    | 0.0             |  pass  |
| ------- | ---------------------------------------     | ------ | --------------  | -------|
| 014     | Negative: user does not enter anything      | ""     | 0.0             |  pass  |

Table 3: Summary of test cases for method `mark_response` for question type `multiple`

| Test ID | Description                                     | Inputs   | Expected Output | Status |
|---------|-------------------------------------------------|----------|-----------------|--------|
| 007     | Positive: user enter ALL correct answers (3/3)  | "A,C,D"  | 4.0             |  pass  |
| ------- | ----------------------------------------------- | -------  | --------------- | ------ |
| 016     | Positive: user enter ALL answers (4/3)          |"A,B,C,D" | 4.0             |  pass  |
|         | even though this is not how real world works    |          |                 |        |
| ------- | ----------------------------------------------- | -------  | --------------- | ------ |
| 008     | Positive: user enter ONE correct answer (1/3)   | "A,B"    | 1.33            |  pass  |
| ------- | ----------------------------------------------- | -------  | --------------- | ------ |
| 009     | Positive: user enter SOME correct answers (2/3) | "A,C"    | 2.67            |  pass  |
| ------- | ----------------------------------------------- | -------  | --------------- | ------ |
| 010     | Negative: user enter the incorrect answer       | "B"      | 0.0             |  pass  |
| ------- | ----------------------------------------------- | -------  | --------------- | ------ |
| 011     | Negative: user enter invalid answer             | "12"     | 0.0             |  pass  |
| ------- | ----------------------------------------------- | -------  | --------------- | ------ |
| 012     | Negative: user enter invalid answer (lowercase) | "a,b"    | 0.0             |  pass  |
| ------- | ----------------------------------------------- | -------  | --------------- | ------ |
| 015     | Negative: user does not enter anything          | ""       | 0.0             |  pass  |

