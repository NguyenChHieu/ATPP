"""
Functions to set up the exam questions and candidate list for the exam.
"""
import question
import candidate
import io


def extract_questions(fobj: io.TextIOWrapper) -> list:
    """
    Parses obj to extract details of each question found in the file.

    Algorithm:
    1. Validate object is an open file in read mode.
    2. Read the file line by line.
    3. For each line, check if it starts with keywords like
    "Question -", "Possible Answers:", "Expected Answer:", and "Marks:".

    4. Based on the keyword, extract data using string slicing.
       - For "Question -", extract question type.
       - For "Possible Answers:", extract all subsequent lines until
       another keyword is encountered, and store them as answer options.
       - For "Expected Answer:", extract correct answer.
       - For "Marks:", extract marks.
       - Any other line is considered part of the question description.
       (does not count the space between questions, since those have been skipped)

    5. Once all data is extracted, create a Question object then set its attributes.
    6. Append the Question object to the list of questions.
    7. Repeat steps 3-6 until the end of the file is reached.
    8. Add an "end" type question to the list to show the end of exam.

    Parameter:
        obj: open file object in read mode
    Returns:
        result: list of Question objects.
    """
    # check if the parameter is valid and in read mode
    if not isinstance(fobj, io.TextIOWrapper) or fobj.mode != 'r':
        raise ValueError("The parameter passed in is not an open file object in read mode")

    # read first line
    lines = fobj.readline().strip()

    # create a list to store questions
    question_list = []
    # create a dictionary which stores the questions info
    current_data_question = {}


    while lines:
        # keyword "Question -"
        if lines.startswith("Question -"):
            # get question type
            index_to_cut = len("Question -")  # get the length of this string for string slicing
            slice_question_type = lines[index_to_cut:].lower()  # extract the question type, case-insensitive
            current_data_question["type"] = slice_question_type  # assign a key-value pair to the dict

        # keyword answers
        elif lines.startswith("Possible Answers:"):
            # get answer options
            answers = []
            while True:
                next_line = fobj.readline().strip()  # strip here
                if next_line.startswith("Expected Answer:") or next_line.startswith("Marks:") or not next_line:
                    lines = next_line  # update lines here
                    break
                answers.append((next_line, False))

            current_data_question["answers_options"] = answers
            continue

            # keyword correct answer
        elif lines.startswith("Expected Answer:"):
            # get correct answers
            index_to_cut = len("Expected Answer: ")
            slice_correct_answers = lines[index_to_cut:].strip()
            current_data_question["expected_answer"] = slice_correct_answers

        # keyword marks
        elif lines.startswith("Marks:"):
            # get marks
            index_to_cut = len("Marks: ")
            slice_marks = lines[index_to_cut:].strip()
            try:
                current_data_question["marks"] = int(slice_marks)
            except ValueError:
                print("Invalid mark type.")
                exit(1)

        else:
            # if the line does not match the above headers, it is part of the question description
            if lines.strip():  # only non-empty lines are added
                current_data_question.setdefault("description", "")
                current_data_question["description"] += lines

        # read next line foe next question
        lines = fobj.readline()

        # check if we reach the line of new question
        if lines.startswith("Question -") or not lines:
            if current_data_question:
                questions = question.Question("")  # set temporary value
                questions.set_type(current_data_question.get("type", ""))  # get question type
                
                questions.set_description(current_data_question.get("description", "").rstrip())  # get description
                
                # get correct answer
                if questions.qtype == "single" or questions.qtype == "multiple":
                    correct_ans = current_data_question.get("expected_answer", "").upper()  # keep uppercase ("A.")
                    questions.set_correct_answer(correct_ans)
                elif questions.qtype == "short":
                    short_correct_answer = current_data_question.get("expected_answer", "")  # keep original
                    questions.set_correct_answer(short_correct_answer)

                # get answer options
                questions.set_answer_options(current_data_question.get("answers_options", []))
                questions.set_marks(current_data_question.get("marks", 0))  # get marks

                # handle the case if question type is invalid
                if questions.qtype is None:
                    questions.description = None
                    questions.answer_options = []
                    questions.correct_answer = None
                    questions.marks = None

                # append the question to the list
                question_list.append(questions)
                current_data_question = {}  # reset the dictionary

    # end
    end = question.Question("end")
    question_list.append(end)

    return question_list


def sort(to_sort: list, order: int = 0) -> list:
    """
    - Sorts to_sort depending on settings of order.
    Algorithm: bubble sort - compare each pair recursively then swap if it met the criteria.
    Parameters:
        to_sort: list, list to be sorted.
        order: int, 0 - no sort, 1 - ascending, 2 - descending
    Returns
        result: list, sorted results.
    """
    # check if to_sort is a list
    if not isinstance(to_sort, list):
        exit()
    # return new list with original settings
    if not isinstance(order, int) and not 0 <= order <= 2:
        new_list = to_sort
        return new_list

    ls = to_sort
    max_pass = len(ls) - 1  # n-1 passes - worst case ( while n is the number of values in the list)
    passes = 0

    # return same list
    if order == 0:
        return to_sort

    # descending
    elif order == 2:

        while passes < max_pass:
            i = 0
            while i < max_pass:  # recursively compare the pairs
                num = ls[i]
                other_num = ls[i + 1]
                if num < other_num:  # swap if it met the criteria - descend
                    ls[i] = other_num
                    ls[i + 1] = num
                i += 1
            passes += 1
        return to_sort

    elif order == 1:

        while passes < max_pass:
            i = 0
            while i < max_pass:  # recursively compare the pairs
                num = ls[i]
                other_num = ls[i + 1]
                if num > other_num:  # swap if it met the criteria - ascend
                    ls[i] = other_num
                    ls[i + 1] = num
                i += 1
            passes += 1
        return to_sort

    else:
        exit()


def extract_students(fobj: io.TextIOWrapper) -> list:
    """
    Parses obj to extract details of each student found in the file.

    Parameter:
        obj: open file object in read mode
    Returns:
        result: list of Candidate objects sorted in ascending order
    """
    # check if the parameter is valid and in read mode
    if not isinstance(fobj, io.TextIOWrapper) or fobj.mode != 'r':
        return []

    # read the file
    lines = fobj.readlines()
    candidate_list = []
    # instantiate a default list
    current_candidate_info = [0, 0, 0]

    # remove newline chars
    i = 1
    formatted_lines = []
    while i < len(lines):
        formatted_lines.append(lines[i].strip())
        i += 1

    # sort candidates ascending base on sids
    sorted_candidates = sort(formatted_lines, 1)

    k = 0
    while k < len(sorted_candidates):
        line = sorted_candidates[k]

        if line.strip():
            sid, name, extra_time = line.split(",")
            current_candidate_info[0] = sid.strip()
            current_candidate_info[1] = name.strip()
            current_candidate_info[2] = extra_time.strip()

            sid = current_candidate_info[0]
            name = current_candidate_info[1]

            # if the extra time is empty, assign default value "0"
            if current_candidate_info[2].strip():
                new_extra = int(current_candidate_info[2])
            else:
                new_extra = 0

            # create a new candidate object
            candidates = candidate.Candidate("000000001", name, 0)
            candidates.edit_sid(sid)
            candidates.edit_extra_time(new_extra)

            # append the object
            candidate_list.append(candidates)
        k += 1
    return candidate_list

