import random


class Question:

    def __init__(self, qtype):
        # checking question type validity
        try:
            if qtype.lower() == "single" or qtype == "multiple" or qtype == "short" or qtype == "end":
                self.qtype = qtype
            else:
                self.qtype = None
        except AttributeError:
            self.qtype = None

        self.description = None
        self.answer_options = []
        self.correct_answer = None
        self.marks = None

    def set_type(self, qtype):
        """
        Update instance question type if:
        + The value is not None or empty
        + The value is a str and match one of the specified question types
        Returns -> bool: True if successfully update the type, else False
        """
        # avoid unwanted spaces
        if qtype:  # check if the value is not None or empty
            question_type = qtype.strip().lower()
        else:
            return False

        # update qtype
        if question_type == "single":
            self.qtype = "single"
        elif question_type == "multiple":
            self.qtype = "multiple"
        elif question_type == "short":
            self.qtype = "short"
        elif question_type == "end":
            self.qtype = "end"
        else:
            return False

        return True

    def set_description(self, desc):
        """
        Update instance variable description if:
        + It is not end type
        + If the parameter is a str and not blank
        Returns -> bool: True if successfully update the description, else False
        """
        # return False if its end type
        if self.qtype == "end":
            return False
        # check if the parameter is a str and not blank
        if isinstance(desc, str) and desc.strip():
            self.description = desc
            return True
        return False

    def set_correct_answer(self, ans):
        """
        Update instance variable correct_answer if:
        + Question type is single, multiple or short
        + The parameter is valid label(s) - example: A.
        Returns -> bool: True if successfully update the answers, else False
        """
        valid_ans = ["A", "B", "C", "D"]

        # single
        if self.qtype == "single":
            m = 0
            # check if answer is valid
            while m < len(valid_ans):
                if ans == valid_ans[m]:
                    self.correct_answer = ans
                    return True
                m += 1
            else:
                return False

        # multiple
        elif self.qtype == "multiple":
            # split up the chars to check valid
            answers = ans.strip().split(",")
            # loop through the chars to compare with valid ans
            i = 0
            while i < len(answers):
                k = 0
                is_valid = False  # set up a flag for checking

                while k < len(valid_ans):
                    answer = answers[i].strip()
                    if answer == valid_ans[k]:
                        is_valid = True  # update the flag if the answer is valid
                        break
                    k += 1

                if not is_valid:  # if there is an invalid option ( not False -> True) then return a False value
                    return False
                i += 1

            self.correct_answer = ans  # after checking append back to attribute

        # short
        elif self.qtype == "short":
            self.correct_answer = ans  # append the answer right away

        # end
        elif self.qtype == "end":
            return False

        return True

    def set_marks(self, num):
        """
        Update instance variable marks if:
        + Question type is valid and not "end"
        + The parameter is int type and greater or equal to 0
        Returns -> bool: True if successfully update the answers, else False
        """
        # return False if its end type
        if self.qtype == "end":
            return False
        # check if num is int type and greater or equal to 0
        if isinstance(num, int) and num >= 0:
            self.marks = num
            return True

        return False

    def set_answer_options(self, opts):
        """
        Update instance variable answer_options if:
        + There are only 4 options
        + All options are tuple type in a list
        + All the types have 2 elements and valid format (description, bool)
        + Options have all flags equal to False when passed in.
        + Option description start with a valid label and follow the correct order (A,B,C,D)

        This method will update the flags based on the correct answer.
        + Check the number of correct answers is correct -> return True, else False
        """

        # if question type is either 1 one these two, assign the value.
        if self.qtype == "short" or self.qtype == "end":
            self.answer_options = opts
            return True

        # if answer is not assigned, return default value
        if self.correct_answer is None:
            return False

        data_is_valid = True  # flag use to avoid appending to the attribute if it isn't valid

        # only 4 elements is allowed in opts
        if len(opts) != 4:
            return False

        # (for data checking purposes)
        valid_ans = ["A", "B", "C", "D"]

        k = 0
        # set all flags to false
        while k < len(opts):
            # default the tuples to False
            if isinstance(opts[k], tuple):  # check if the elements are tuple
                opts[k] = (opts[k][0], False)  # set flags to False initially
            else:
                return False
            k += 1

        # loop through the tuples of opts list
        i = 0
        while i < len(opts):

            tuple_extracted = opts[i]
            # check if there are 2 elements in a tuple
            if len(tuple_extracted) != 2:
                data_is_valid = False
                break

            # extract the tuple elements
            ans_description = tuple_extracted[0]

            # check if the 1st element of the tuple is str
            if not isinstance(ans_description, str):
                data_is_valid = False
                break

            # check if the description starts with A., B. ... and in correct order
            # checking if the ans are separated by a period
            if not (ans_description[:2] == valid_ans[i] + "." and ans_description[2:3] == " "):
                data_is_valid = False
                break

            # update flag for the corresponding types
            answers = self.correct_answer.split(",")

            # single
            if self.qtype == "single":
                if self.correct_answer == valid_ans[i]:
                    opts[i] = (ans_description, True)  # update the tuple if it is the correct answer

            # multiple
            elif self.qtype == "multiple":
                correct = False
                j = 0
                while j < len(answers):
                    if valid_ans[i] == answers[j].lstrip().strip():
                        correct = True
                        break
                    j += 1

                if correct:  # update the tuple if it is the correct answer
                    opts[i] = (ans_description, True)

            # modify the outer control variable loop
            i += 1

        # update the attribute if data pass all the checks
        if data_is_valid:
            self.answer_options = opts
        else:
            return False

        # check if question type is single, then there is exactly 1 correct answer.
        if self.qtype == "single":
            count_flags = 0
            i = 0
            while i < len(opts):
                if opts[i][1]:  # if the flag is True, +1
                    count_flags += 1
                i += 1

            if count_flags == 1:
                return True

        # check if question type is multiple, then there is at least 1 correct answer.
        if self.qtype == "multiple":
            count_flags = 0
            i = 0
            while i < len(opts):
                if opts[i][1]:  # if the flag is True, +1
                    count_flags += 1
                i += 1

            if 4 >= count_flags >= 1:
                return True

        return False  # return false other question types.

    def get_answer_option_descriptions(self):
        """
        Returns formatted string listing each answer description on a new line
        Example:
        A. Answer description
        B. Answer description
        C. Answer description
        D. Answer description
        """
        # if its end type return False
        if self.qtype == "short" or self.qtype == "end":
            return ""

        str_out = ""
        p = 0
        while p < len(self.answer_options):
            answer_des = self.answer_options[p][0]  # extract the description
            if p != len(self.answer_options)-1:
                str_out += (answer_des + "\n")
            else:
                str_out += answer_des
            p += 1

        return str_out

    def mark_response(self, response: str):
        """
        Check if response matches the expected answer
        Parameter:
            response: str, response provided by candidate
        Returns:
            marks: int|float, marks awarded for the response.
        """
        answers = self.correct_answer
        marks_awarded = self.marks
        default_mark = 0.00

        if self.qtype == "end":
            return None
        elif self.qtype == "single":
            if response == answers:
                rounded_single = round(marks_awarded, 2)
                return rounded_single
            else:
                return default_mark
        elif self.qtype == "short":
            if response == answers.lstrip().strip():
                rounded_single = round(marks_awarded, 2)
                return rounded_single
            else:
                return default_mark
        elif self.qtype == "multiple":
            answers_list = answers.split(",")
            response_list = response.split(",")

            b = 0
            correct_count = 0
            while b < len(response_list):
                c = 0
                response_part = response_list[b].lstrip()
                while c < len(answers_list):
                    if response_part == answers_list[c].lstrip():
                        correct_count += 1
                        break
                    c += 1
                b += 1

            if correct_count == 0 or correct_count > 4:
                return default_mark
            else:
                rounded_marks = round((marks_awarded/len(answers_list))*correct_count, 2)
                return rounded_marks

    def preview_question(self, i=0, show=True):
        """
        Returns formatted string showing details of question.
        Parameters:
            i: int, placeholder for question number, DEFAULT = 0
            show: bool, True to show Expected Answers, DEFAULT = TRUE
        """
        str_out = ""

        # end type
        if self.qtype == "end":
            return "-End-"

        # single
        elif self.qtype == "single":
            if show:  # show answer
                if i == 0:
                    str_out += f"Question X - {self.qtype.capitalize()} Answer[{self.marks}]"
                else:
                    str_out += f"Question {i} - {self.qtype.capitalize()} Answer[{self.marks}]"

                str_out += f"\n{self.description}\n"
                str_out += Question.get_answer_option_descriptions(self)
                str_out += f"\nExpected Answer: {self.correct_answer}"

            elif not show:  # dont show
                if i == 0:
                    str_out += f"Question X - {self.qtype.capitalize()} Answer[{self.marks}]"
                else:
                    str_out += f"Question {i} - {self.qtype.capitalize()} Answer[{self.marks}]"
                str_out += f"\n{self.description}\n"
                str_out += Question.get_answer_option_descriptions(self)

        elif self.qtype == "multiple":
            if show:  # show answer
                if i == 0:
                    str_out += f"Question X - {self.qtype.capitalize()} Answers[{self.marks}]"
                else:
                    str_out += f"Question {i} - {self.qtype.capitalize()} Answers[{self.marks}]"

                str_out += f"\n{self.description}\n"
                str_out += Question.get_answer_option_descriptions(self)
                str_out += f"\nExpected Answer: {self.correct_answer}"

            elif not show:  # dont show
                if i == 0:
                    str_out += f"Question X - {self.qtype.capitalize()} Answers[{self.marks}]"
                else:
                    str_out += f"Question {i} - {self.qtype.capitalize()} Answers[{self.marks}]"
                str_out += f"\n{self.description}\n"
                str_out += Question.get_answer_option_descriptions(self)

        elif self.qtype == "short":
            if show:  # show answer
                if i == 0:
                    str_out += f"Question X - {self.qtype.capitalize()} Answer[{self.marks}]"
                else:
                    str_out += f"Question {i} - {self.qtype.capitalize()} Answer[{self.marks}]"
                str_out += f"\n{self.description}"
                str_out += f"\nExpected Answer: {self.correct_answer}"

            elif not show:  # dont show
                if i == 0:
                    str_out += f"Question X - {self.qtype.capitalize()} Answer[{self.marks}]"
                else:
                    str_out += f"Question {i} - {self.qtype.capitalize()} Answer[{self.marks}]"
                str_out += f"\n{self.description}"
                str_out += Question.get_answer_option_descriptions(self)
        return str_out

    def generate_order():
        """
        Returns a list of 4 integers between 0 and 3 inclusive to determine order.
        Sample usage:
            generate_order()
            [3,1,0,2]
        """
        unique_numbers = []
        i = 0
        while True:
            if len(unique_numbers) == 4:
                break

            number = random.randint(0, 3)

            if len(unique_numbers) == 0:
                unique_numbers.append(number)
            else:
                k = 0
                flag = True
                while k < len(unique_numbers):
                    if number == unique_numbers[k]:
                        flag = False
                    k += 1
                if flag:
                    unique_numbers.append(number)
            i += 1
        return unique_numbers

    def shuffle_answers(self):
        """
        Updates answer options with shuffled elements.

        Algorithm:
        + Assign the options to a random list of numbers ranging from 0-3
        + Update the new answers base on the new order
        + Then update the corresponding attributes - correct answers and answer options
        """
        if self.qtype == "end" or self.qtype == "short":
            return

        # note: all the loops are limited to 4 since they are restricted to only 4 elements
        options = self.answer_options
        order = Question.generate_order()

        # update the order
        new_answers_order = []
        k = 0
        while k < 4:
            index = order[k]
            new_answers_order.append(options[index])
            k += 1

        # new list
        shuffled_answers = []

        # change the label of the new answer order
        i = 0
        while i < 4:
            ans_tuple = new_answers_order[i]
            ans_description = ans_tuple[0]
            flag = ans_tuple[1]
            initial_char = ans_description.split()[0]

            if i == 0:
                new_ans_des = ans_description.replace(initial_char, "A.")  # make sure first element starts with A.
                new_ans_tuple = (new_ans_des, flag)
                shuffled_answers.append(new_ans_tuple)
            if i == 1:
                new_ans_des = ans_description.replace(initial_char, "B.")  # make sure first element starts with B.
                new_ans_tuple = (new_ans_des, flag)
                shuffled_answers.append(new_ans_tuple)
            if i == 2:
                new_ans_des = ans_description.replace(initial_char, "C.")  # make sure first element starts with C.
                new_ans_tuple = (new_ans_des, flag)
                shuffled_answers.append(new_ans_tuple)
            if i == 3:
                new_ans_des = ans_description.replace(initial_char, "D.")  # make sure first element starts with D.
                new_ans_tuple = (new_ans_des, flag)
                shuffled_answers.append(new_ans_tuple)
            i += 1

        # new answer list
        new_ans = ""

        # detect new answers
        h = 0
        while h < 4:
            ans_tuple = shuffled_answers[h]
            ans_description = ans_tuple[0]
            initial_char = ans_description.split()[0].strip(".")  # extract the label only
            flag = ans_tuple[1]

            if flag:   # append the new correct answers
                new_ans += (initial_char + ", ")

            h += 1

        formatted_ans = new_ans[:-2]  # get rid of excessive trails
        # update new ans after shuffled
        self.correct_answer = formatted_ans
        self.answer_options = shuffled_answers

    def copy_question(self):
        """
        Create a new question copy base on the original
        Returns: new question
        """
        new_question = Question(self.qtype)

        # set attributes
        new_question.description = self.description
        new_question.answer_options = self.answer_options
        new_question.correct_answer = self.correct_answer
        new_question.marks = self.marks

        return new_question

    def __str__(self):
        return f'''Question {self.__hash__()}:
        
Type: {self.qtype}
Description: {self.description}
Possible Answers: {self.get_answer_option_descriptions()}
Correct answer: {self.correct_answer}
Marks: {self.marks}
'''

