"""
Chi Hieu Nguyen - 530382197
This is my test program.

Instructions:
There would be 15 test cases, each testcase will correspond to a function.
Every test case has a brief summary about its type, expected output and expected mark

+ Scroll down, and you will see a bunch of comments, uncomment each one respectively to 
check if each test have passed, if pass, then a message would be printed to notify that
the test have passed.

+ After that, for each question suite, there's an if statement to check if all the
tests in the corresponding suite have passsed.

+ If you want to check the functions separately, remember to comment the big "if" statement
to avoid message duplication

+ P.s: If you wanted to check all at once do python3 test_program.py, just uncomment the 
if statements (if alr commented), and be careful dont uncomment the "labels" on top of each 
suite (line 185, 193, 203)!
"""
import question

# Creating questions:
# Question 1 - short
ques1 = question.Question("short")
ques1.set_description("Which is your ex?")
ques1.set_correct_answer("her")
ques1.set_marks(2)

# Question 2 - single
ques2 = question.Question("single")
ques2.set_description("Which is my favourite subject?")
ques2.set_correct_answer("C")
ques2.set_answer_options([("A. 1064", False), ("B. 1112", False), ("C. 1110", False), ("D. 1601", False)])
ques2.set_marks(1)

# Question 3 - multiple
ques3 = question.Question("multiple")
ques3.set_description("Which is your ex?")
ques3.set_correct_answer("A, C, D")
ques3.set_answer_options([("A. Hanh", False), ("B. VPL", True), ("C. PLinh", False), ("D. Bao Linh", False)])
ques3.set_marks(4)


# TESTCASES


# SHORT SUITE
# short - positive - correct answer - full points (2.0)
def test_1():
    expected = 2.0
    actual = ques1.mark_response("her")
    assert actual == expected, f"Mark does not match as expected.\
    \nExpected: {expected}\
    \nGot: {actual}"
    print("Test 1 passed!")
    return True


# short - negative - incorrect answer - no points (0)
def test_2():
    expected = 0.0
    actual = ques1.mark_response("nah")
    assert actual == expected, f"Mark does not match as expected.\
    \nExpected: {expected}\
    \nGot: {actual}"
    print("Test 2 passed!")
    return True


# short - negative - incorrect answer - no points (0)
def test_3():
    expected = 0.0
    actual = ques1.mark_response("1")
    assert actual == expected, f"Mark does not match as expected\
    \nExpected: {expected}\
    \nGot: {actual}"
    print("Test 3 passed!")
    return True


# SINGLE SUITE
# single - positive - correct answer - full points (1.0)
def test_4():
    expected = 1.0
    actual = ques2.mark_response("C")
    assert actual == expected, f"Mark does not match as expected\
    \nExpected: {expected}\
    \nGot: {actual}"
    print("Test 4 passed!")
    return True


# single - negative - incorrect answer - no points (0)
def test_5():
    expected = 0.0
    actual = ques2.mark_response("A")
    assert actual == expected, f"Mark does not match as expected\
    \nExpected: {expected}\
    \nGot: {actual}"
    print("Test 5 passed!")
    return True


# single - negative - passed in an invalid answer - no points (0)
def test_6():
    expected = 0.0
    actual = ques2.mark_response("hi")
    assert actual == expected, f"Mark does not match as expected\
    \nExpected: {expected}\
    \nGot: {actual}"
    print("Test 6 passed!")
    return True


# single - negative - lowercase - no points (0)
def test_13():
    expected = 0.0
    actual = ques2.mark_response("a")
    assert actual == expected, f"Mark does not match as expected\
    \nExpected: {expected}\
    \nGot: {actual}"
    print("Test 13 passed!")
    return True


# single - negative - empty - no points (0)
def test_14():
    expected = 0.0
    actual = ques2.mark_response("")
    assert actual == expected, f"Mark does not match as expected\
    \nExpected: {expected}\
    \nGot: {actual}"
    print("Test 14 passed!")
    return True


# MULTIPLE SUITE
# multiple - positive - all correct answer - full points (4.0)
def test_7():
    expected = 4.0
    actual = ques3.mark_response("A,C,D")
    assert actual == expected, f"Mark does not match as expected\
    \nExpected: {expected}\
    \nGot: {actual}"
    print("Test 7 passed!")
    return True

# multiple - positive - all correct answer (even the wrong answer)  - full points (4.0)
def test_16():
    expected = 4.0
    actual = ques3.mark_response("A,B,C,D")
    assert actual == expected, f"Mark does not match as expected\
    \nExpected: {expected}\
    \nGot: {actual}"
    print("Test 16 passed!")
    return True

# multiple - positive - one correct answer - partial points (1.33)
def test_8():
    expected = 1.33
    actual = ques3.mark_response("A,B")
    assert actual == expected, f"Mark does not match as expected\
    \nExpected: {expected}\
    \nGot: {actual}"
    print("Test 8 passed!")
    return True


# multiple - positive - some correct answer - partial points (2.67)
def test_9():
    expected = 2.67
    actual = ques3.mark_response("A,C")
    assert actual == expected, f"Mark does not match as expected\
    \nExpected: {expected}\
    \nGot: {actual}"
    print("Test 9 passed!")
    return True


# multiple - negative - incorrect answer - no points (0)
def test_10():
    expected = 0.0
    actual = ques3.mark_response("B")
    assert actual == expected, f"Mark does not match as expected\
    \nExpected: {expected}\
    \nGot: {actual}"
    print("Test 10 passed!")
    return True


# multiple - negative - no points (0)
def test_11():
    expected = 0.0
    actual = ques3.mark_response("12")
    assert actual == expected, f"Mark does not match as expected\
    \nExpected: {expected}\
    \nGot: {actual}"
    print("Test 11 passed!")
    return True


# multiple - negative - lowercase - no points (0)
def test_12():
    expected = 0.0
    actual = ques3.mark_response("a,b")
    assert actual == expected, f"Mark does not match as expected\
    \nExpected: {expected}\
    \nGot: {actual}"
    print("Test 12 passed!")
    return True


# multiple - negative - empty - no points (0)
def test_15():
    expected = 0.0
    actual = ques3.mark_response("")
    assert actual == expected, f"Mark does not match as expected\
    \nExpected: {expected}\
    \nGot: {actual}"
    print("Test 15 passed!")
    return True

# FOR MARKER

# SHORT

# test_1()
# test_2()
# test_3()
if test_1() and test_2() and test_3():
    print("All SHORT question test cases passed")

# SINGLE

# test_4()
# test_5()
# test_6()
# test_13()
# test_14()
if test_4() and test_5() and test_6() and test_13() and test_14():
    print("All SINGLE test cases passed")

# MULTIPLE

# test_7()
# test_8()
# test_9()
# test_10()
# test_11()
# test_12()
# test_15()
# test_16()

if test_7() and test_8() and test_9() and test_10() \
        and test_11() and test_12() and test_15() and test_16():
    print("All MULTIPLE test cases passed")

