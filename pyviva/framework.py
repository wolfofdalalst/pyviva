import csv
from pathlib import Path

from pyviva.templates import QuestionSet


PATH = Path(__file__).parent / "resources/quiz.csv"


def _uuid() -> int:
    # returns 32-bit random unique id
    from uuid import uuid1

    return uuid1().time_low


# read operations


def _return_csv_data() -> list:
    # returns the csv data in the form of a list, including the headers
    # example output:
    # [
    #   ["3618642576","-1","What's 9+10?","[19, 21, 20, None]","2"],
    #   ...
    # ]
    result = list()
    with open(PATH, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        result.extend(csv_reader)

    return result


def random_question(diff=0) -> QuestionSet:
    # returns a random QuestionSet object
    from random import choice

    csv_data = _return_csv_data()
    question_pool = list()
    for col in csv_data:
        try:
            if int(QuestionSet(*col).diff) == diff:
                question_pool.append(col)
        except ValueError:
            pass
    return QuestionSet(*choice(question_pool))


# write operations


def append_question(question_set: QuestionSet) -> int:
    # appends the question set to the csv file
    with open(PATH, "a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(question_set())
        return 1


def remove_question(uid: int) -> int:
    # removes question from the csv file based on uid
    csv_data = _return_csv_data()
    for col in csv_data:
        try:
            if int(QuestionSet(*col).uid) == uid:
                csv_data.remove(col)
        except ValueError:
            pass
    with open(PATH, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(csv_data)
        return 1
