from question import Question


class Exam:
    def __init__(self, duration, path, shuffle):
        self.duration = duration
        self.path_to_dir = path
        self.shuffle = shuffle
        self.exam_status = False
        self.questions = []
        self.set_name(path)

    def set_name(self, path):
        """
        Sets the name of the exam with new format if:
        + The parameter is a string
        """
        # extract the last part of the path as the name
        if not isinstance(path, str):
            exit()

        name = path.split("/")[-1]

        # replace all the whitespace to _
        exam_name = name.replace(" ", "_")

        self.name = exam_name

    def get_name(self):
        """
        Returns formatted string of exam name with new format.
        """
        name = self.name
        upper_name = name.upper()

        # convert _ to " "
        converted_name = upper_name.replace("_", " ")

        return converted_name

    def set_exam_status(self):
        """
        Set exam_status to True only if exam has questions.
        """
        if len(self.questions) > 0:
            self.exam_status = True
    
    def set_duration(self, t):
        """
        Update duration of exam.
        Parameter:
            t: int, new duration of exam.
        """
        if isinstance(t, int) and t > 0:
            self.duration = t

    def set_questions(self, ls):
        """
        Verifies all questions in the exam are complete.
        + For single, multiple questions, check if:
            + Not missing description and correct answers
            + Have enough answer options.
        + For short:
            + Not missing description and correct answers
            + Don't have answer options
        + Also check if there's an "end" type question at the end

        Parameter:
            ls: list, list of Question objects
        Returns:
            status: bool, True if set successfully.
        """

        if not isinstance(ls, list):
            return False

        # check attributes of every question in the list
        i = 0
        while i < len(ls):

            question = ls[i]

            # check if the elements are Question types
            if not isinstance(question, Question):
                return False

            # extracting the questions and its attributes
            question_type = question.qtype
            description = question.description
            correct_answer = question.correct_answer
            options = question.answer_options
            marks = question.marks

            # check if last element were "end"
            if i == len(ls) - 1:
                if question_type != "end":
                    print("End marker missing or invalid")
                    return False
                # check end type attributes are default
                # des: None, correct_ans: None, options list is empty, marks is None
                if description is not None or correct_answer is not None or len(options) != 0 or marks is not None:
                    print("End marker missing or invalid")
                    return False

            # check question type:
            # single
            if question_type == "single" or question_type == "multiple":
                # if there were no des
                if description is None:
                    print("Description or correct answer missing")
                    return False
                # if correct ans were not set
                if correct_answer is None:
                    print("Description or correct answer missing")
                    return False
                # check options if they are empty
                if not len(options) == 4:
                    print("Answer options incorrect quantity")
                    return False

            if question_type == "short":
                # if there were no des
                if description is None:
                    print("Description or correct answer missing")
                    return False
                # if correct ans were not set
                if correct_answer is None:
                    print("Description or correct answer missing")
                    return False
                # if there are options
                if len(options) > 0:
                    print("Answer options should not exist")
                    return False
            i += 1

        self.questions = ls
        return True
    
    def preview_exam(self) -> str:
        """
        Returns a formatted string.
        """
        # initiate the string
        str_out = ""

        questions_list = self.questions

        # display
        # name of exam
        str_out += Exam.get_name(self)

        i = 1
        while i <= len(questions_list):

            # extract each question and its attributes
            question = questions_list[i-1]  # 0-indexed list
            description = question.description
            types = question.qtype
            correct_ans = question.correct_answer
            options = question.answer_options
            marks = question.marks

            if types == "end":
                str_out += "\n-End-"
                break

            # print question number, type and answer
            # "Answer"
            if types == "single" or types == "short":
                str_out += f"\nQuestion {i} - {types.capitalize()} Answer[{marks}]\n"
            # "Answers"
            elif types == "multiple":
                str_out += f"\nQuestion {i} - {types.capitalize()} Answers[{marks}]\n"

            # print question description
            str_out += description

            # for single and multiple
            if types == "single" or types == "multiple":
                k = 0
                while k < 4:  # there are only 4 options
                    if k == 0:
                        str_out += f"\n{options[k][0]}"
                    else:
                        str_out += f"\n{options[k][0]}"
                    k += 1

            # print correct answers
            str_out += f"\nExpected Answer: {correct_ans}"
            # print an extra line
            str_out += "\n"

            i += 1

        return str_out + "\n\n"

    def copy_exam(self):
        """
        Create a new exam object using the values of these instances' values.
        """
        new_exam = Exam(self.duration, self.path_to_dir, self.shuffle)

        # set attributes
        new_exam.name = self.name
        new_exam.exam_status = self.exam_status

        # make a new list of questions to reassign to the attribute
        new_questions = []
        i = 0
        while i < len(self.questions):
            original_question = self.questions[i]
            # call the copy method for this question
            new_question = original_question.copy_question()

            # insert this into new list of questions
            new_questions.append(new_question)
            i += 1

        new_exam.questions = new_questions

        # return the new exam
        return new_exam

    def __str__(self):
        pass

