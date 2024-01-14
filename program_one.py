"""
Interface of the exam
"""
import os.path
import exam
import setup
import sys


def parse_cmd_args(args: list):
    """
    Parameters:
        args: list, command line arguments
    Returns:
        result: None|tuple, details of the exam
    """
    # get total length without 1st element as script name
    arg_actual_length = len(args) - 1

    # check arguments
    if arg_actual_length < 2:
        print("Check command line arguments")
        return None

    # extract information
    directory = args[1]

    # check valid type of duration
    try:
        exam_duration = int(args[2])
    except ValueError:
        print("Duration must be an integer")
        return None

    # check for the shuffle flag
    shuffle_flag = False
    # check if there are enough args and in read mode
    if arg_actual_length >= 3 and args[3] == "-r":
        shuffle_flag = True

    return directory, exam_duration, shuffle_flag  # return a tuple


def setup_exam(obj):
    """
    Update exam object with question contents extracted from file.
    Parameter:
        obj: Exam object
    Returns:
        (obj, status): tuple containing updated Exam object and status
        where status: bool, True if exam is set up successfully. Otherwise, False.
    """

    # try to open the file in the Exam object and extract questions
    if not isinstance(obj, exam.Exam):
        print("Error setting up exam")
        return obj, False

    try:
        path = obj.path_to_dir + "/questions.txt"  # create the absolute path

        # read the file and extract the questions
        with open(path, 'r') as exam_obj:
            questions = setup.extract_questions(exam_obj)

            # Set the questions in the Exam object
            obj.set_questions(questions)

            # set exam status
            obj.set_exam_status()
            status = obj.exam_status

            return obj, status

    # catch any exception and return False
    except Exception as e:
        print(f"Error setting up exam: {e}")  # Optionally log the error for debugging
        return obj, False


def main(args):
    """
    Implement all stages of exam process.
    """
    # parse the args
    result = parse_cmd_args(args)
    if not result:
        exit()

    # extract the values
    directory, duration, shuffle_flag = result

    # check if "questions.txt" and "students.csv" are exist
    if not os.path.exists(os.path.join(directory, "questions.txt")) or \
            not os.path.exists(os.path.join(directory, "students.csv")):
        print("Missing files")
        exit()

    # display
    print("Setting up exam...")

    # create the exam object
    exam_obj = exam.Exam(duration, directory, shuffle_flag)

    # set up
    exam_obj, status = setup_exam(exam_obj)

    if not status:  # if status = False
        print("Error setting up exam")
        exit()

    # display
    print("Exam is ready...")
    try:
        # prompt the user if they enter invalid input
        while True:
            user_preview = input("Do you want to preview the exam [Y|N]? ").strip().lower()
            if user_preview == "y":
                print(exam_obj.preview_exam(), end="")  # avoid excessive lines
            elif user_preview == "n":
                break
            else:
                print("Invalid command.")
    except AttributeError:
        exit()
    return exam_obj

if __name__ == "__main__":
    '''
    DO NOT REMOVE
    '''
    main(sys.argv)

