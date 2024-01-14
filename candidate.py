import os
import question


class Candidate:
    def __init__(self, sid, name, time):
        self.sid = sid
        self.name = name
        self.extra_time = time
        self.exam = None
        self.confirm_details = False
        self.results = []

    def get_duration(self) -> int:
        """
        Returns total duration of exam.
        """
        test_time = self.exam.duration
        extra = self.extra_time

        # check if extra time is valid
        if isinstance(extra, int) and extra >= 0:
            total = test_time + extra
            return total
        else:
            print("Invalid extra time.")
            exit()

    def edit_sid(self, sid):
        """
        Update attribute sid
        """
        # check if sid is a str and > 0
        if type(sid) == str:
            try:
                if int(sid) > 0:
                    if len(sid) == 9:
                        if sid.isdigit():
                            self.sid = sid
            except ValueError:
                print("Invalid sid type.")
                exit(1)

    def edit_extra_time(self, t):
        """
        Update attribute extra_time
        """

        # check if extra time is valid
        if isinstance(t, int) and t >= 0:
            self.extra_time = t
        else:
            exit()

    def set_confirm_details(self, sid, name) -> bool:
        """
        Update attribute confirm_details
        """
        # check str
        if not isinstance(sid, str) or not isinstance(name, str):
            return False

        # check if sid and name match.
        saved_name = self.name
        if name.strip().lower() == saved_name.lower() and sid.strip() == self.sid:
            self.confirm_details = True
            return True
        else:
            return False

    def log_attempt(self, data):
        """
        Save data into candidate's file in Submissions.
        """
        submission_file = self.set_file_path()
        with open(submission_file, "w") as s_file:
            s_file.write(data)

    def set_file_path(self):
        # attributes
        path_to_test = self.exam.path_to_dir
        own_sid = self.sid
        full_path = os.path.join(path_to_test, "submissions")

        # if we don't have the folder, then create it
        if not os.path.exists(full_path):
            os.makedirs(full_path)

        submission_file = os.path.join(full_path, f"{own_sid}.txt")
        return submission_file

    def set_results(self, ls: list):
        """
        Update attribute results if the confirm_details are True
        """
        flag = self.confirm_details
        exam_questions = self.exam.questions

        # check if parameter is a list
        if not isinstance(ls, list):
            exit()

        # if the candidate has pass the verification check
        if flag:
            # check if the number of marks correspond to the number of questions
            if len(ls) == (len(exam_questions) - 1):  # exclude the end question
                self.results = ls

    def do_exam(self, preview=True):
        """
        Display exam and get candidate response from terminal during the exam.
        """
        # basic candidate info
        print(f"Candidate: {self.name}({self.sid})")
        t = self.get_duration()
        print(f"Exam duration: {t} minutes")
        print("You have " + str(t) + " minutes to complete the exam.")

        # exam name
        print(self.exam.get_name())

        # if the exam is not assigned
        if self.exam is None:
            print(f"Exam preview: \nNone\n")

        else:
            questions_list = self.exam.questions
            o = 0
            i = 1
            default_mark = 0.00
            logging_question = ""

            while o < len(questions_list):
                question_x = questions_list[o]
                if preview:
                    if question_x.qtype == "end":
                        question_str = question_x.preview_question(i, show=False)
                        print(question_str)
                        break

                    question_str = question_x.preview_question(i, show=False)
                    print(question_str)

                    print(f"Response for Question {i}: ")
                    print()

                elif not preview:
                    if question_x.qtype == "end":
                        question_str = question_x.preview_question(i, show=False)
                        print(question_str)
                        logging_question += question_str
                        break

                    question_str = question_x.preview_question(i, show=False)
                    print(question_str)

                    # answer
                    answer_candidate = input(f"Response for Question {i}: ")
                    print()

                    if self.check_valid_input(answer_candidate, question_x):
                        mark = question_x.mark_response(answer_candidate)
                    else:
                        mark = default_mark

                    # logging question
                    logging_question += question_str
                    logging_question += f"\nResponse for Question {i}: {answer_candidate}"
                    logging_question += f"\nYou have scored {mark:.2f} marks.\n\n"
                o += 1
                i += 1
            self.log_attempt(logging_question)

    def check_valid_ans(self, answer):
        valid_ans = ["A", "B", "C", "D"]
        is_valid = False

        # check if the answer contains multiple options
        u = 0
        o = 0
        comma = False

        while u < len(answer):
            if answer[u] == ",":
                comma = True
                break
            u += 1
        # have comma = multiple
        if comma:
            answers_split = answer.split(",")
            if not 0 <= len(answers_split) <= 4:
                return False

            while o < len(answers_split):
                is_valid = False  # Reset is_valid for each new choice
                ans = answers_split[o].lstrip()
                d = 0
                while d < len(valid_ans):
                    if ans == valid_ans[d]:
                        is_valid = True
                        break  # exit loop
                    d += 1
                if not is_valid:
                    return False  # exit early if invalid answer found
                o += 1
            return True
        # no? = single
        else:
            d = 0
            while d < len(valid_ans):
                if answer == valid_ans[d]:
                    is_valid = True
                    break
                d += 1
            return is_valid

    def check_valid_input(self, answer: str, question_object: question.Question):
        question_type = question_object.qtype

        if question_type == "single":
            if self.check_valid_ans(answer):
                check = answer.split(",")
                return len(check) == 1
            else:
                return False
        elif question_type == "multiple":
            if self.check_valid_ans(answer):
                return True
            else:
                return False
        elif question_type == "short":
            return True

    def __str__(self):
        pass

