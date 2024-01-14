"""
Interface of the exam
"""
import sys
import program_two


def main(args):
    candidate_list = program_two.main(args)

    candidate = None
    input_sid = None

    sid_attempts = 0
    retry_attempts = 1
    sid_flag = False  # if the sid is found and valid

    while not sid_flag:
        log_error(sid_attempts, 3, "Contact exam administrator.")
        input_sid = input("Enter your student identification number (SID) to start exam: ")

        # CHECK VALID SID
        try:
            if not(type(input_sid) == str and int(input_sid) > 0
                    and len(input_sid) == 9 and input_sid.isdigit()):
                print("Invalid SID.")
                sid_attempts += 1
                continue
        # if input is not all numbers
        except ValueError:
            print("Invalid SID.")
            sid_attempts += 1
            continue

        # CHECK ID IN LIST
        # FOUND
        index = 0
        while index < len(candidate_list):
            if candidate_list[index].sid == input_sid:
                candidate = candidate_list[index]
                sid_flag = True
                break
            index += 1

        # NOT FOUND
        if not sid_flag:
            print("Candidate number not found for exam.")
            while True:
                input_try_again = input("Do you want to try again [Y|N]? ").upper().strip()
                if input_try_again == "N":
                    exit()
                elif input_try_again == "Y":
                    sid_attempts += 1
                    log_error(sid_attempts, 3, "Contact exam administrator.")
                    # else: keep increment
                    break
                else:
                    print("Response must be [Y|N].")
                    retry_attempts += 1

    # if sid valid and found, proceeds
    name_attempts = 0

    print("Verifying candidate details...")

    # check if name is matched
    while True:
        name = input("Enter your full name as given during registration of exam: ").strip()
        # name can be case in-sensitive
        if candidate.set_confirm_details(input_sid, name):
            print("Start exam....\n")
            candidate.do_exam(False)
            break
        else:
            name_attempts += 1
            log_error(name_attempts,  3, "Contact exam administrator to verify documents.")
            print("Name does not match records.")
            


def log_error(attempts: int, limit: int, log: str):
    if attempts == limit:
        print(log)
        exit()


if __name__ == "__main__":
    main(sys.argv)

