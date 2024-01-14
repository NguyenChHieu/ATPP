"""
Interface of the exam
"""

import setup
import program_one
import exam
import sys


def assign_exam(exam_obj):
    """
    Assign exam to every student in the candidate list.
    Loop through each student, access their exams and loop through each question
    to shuffle (if the flag is True) or just append the exam to the student.

    Args:
        exam_obj: an Exam object

    Returns:

    """
    if not isinstance(exam_obj, exam.Exam):
        return None

    path_to_csv = exam_obj.path_to_dir + "/students.csv"

    with open(path_to_csv, "r") as cand_file:
        candidates_list = setup.extract_students(cand_file)

        # check if the list is empty
        if not candidates_list:
            print("No candidates found in the file")
            return None

        print("Assigning exam to candidates...")

        # assign exam to each student
        m = 0
        while m < len(candidates_list):
            candidate = candidates_list[m]

            new_exam = exam_obj.copy_exam()

            # check shuffle status
            if new_exam.shuffle:

                q = 0
                shuffled_questions = []
                number_of_questions = len(new_exam.questions)

                # for each question, shuffle its answers
                while q < number_of_questions:
                    question = new_exam.questions[q]

                    # the "end" question
                    if q == number_of_questions-1:
                        shuffled_questions.append(question)
                        break
                    elif 0 <= q < number_of_questions-1:
                        question.shuffle_answers()
                        shuffled_questions.append(question)

                    q += 1

                # append the shuffled questions
                new_exam.questions = shuffled_questions

            candidate.exam = new_exam

            m += 1

    print(f"Complete. Exam allocated to {len(candidates_list)} candidates.")
    return candidates_list


def main(args):
    exam_obj = program_one.main(args)
    candidates_list = assign_exam(exam_obj)
    if candidates_list is None:
        print("No file data")
        exit(1)

    while True:
        user_preview = input("Enter SID to preview student's exam (-q to quit): ").strip()
        if user_preview == "-q":
            return candidates_list
        elif user_preview == "-a":
            h = 0
            while h < len(candidates_list):
                candidate = candidates_list[h]
                candidate.do_exam()
                print()
                h += 1
        else:
            # check if user input is a valid sid
            try:
                if int(user_preview) > 0 and len(user_preview) == 9 \
                        and user_preview.isdigit():

                    f = 0
                    candidate_found = False  # flag to check if the candidate was found

                    while f < len(candidates_list):
                        candidate = candidates_list[f]
                        # if candidate found then print the preview
                        if user_preview == candidate.sid:
                            candidate_found = True
                            candidate.do_exam()
                            print()
                            break
                        f += 1

                    # if candidate not found then print the error
                    if not candidate_found:
                        print("SID not found in list of candidates.")
                        print()

                # sid invalid error message
                else:
                    print("SID is invalid.")
                    print()
            # not all numbers
            except ValueError:
                print("SID is invalid.")
                print()


if __name__ == "__main__":
    main(sys.argv)

