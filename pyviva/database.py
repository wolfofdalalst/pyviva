import re
import sqlite3
from pathlib import Path

from pyviva.templates import QuestionSet

PATH = Path(__file__).parent / "resources/quiz.sqlite3"
con = sqlite3.connect(PATH)
cursor = con.cursor()


def init_db():
    try:
        with con:
            con.execute(
                """
            CREATE TABLE Quiz (
                uid INTEGER,
                diff INTEGER,
                question TEXT,
                option1 TEXT,
                option2  TEXT,
                option3 TEXT,
                option4 TEXT,
                answer INTEGER
            )"""
            )
    except sqlite3.OperationalError:
        pass

    return 1


def insert_db(question_set: QuestionSet):
    with con:
        con.execute(
            """
        INSERT INTO Quiz
        VALUES (?,?,?,?,?,?,?,?)
        """,
            (
                question_set.uid,
                question_set.diff,
                question_set.question,
                *question_set.options,
                question_set.answer,
            ),
        )
        return 1


def random_question_db(diff=0) -> QuestionSet:
    from random import choice

    with con:
        cursor.execute("SELECT * FROM Quiz WHERE diff=?", (diff,))
        iterable = choice(cursor.fetchall())
        return QuestionSet(*_parse_args(iterable))


def remove_question_db(uid: int):
    with con:
        con.execute("DELETE FROM Quiz WHERE uid=?", (uid,))
        return 1


def display_db():
    return con.execute("SELECT * FROM Quiz").fetchall()


def _parse_args(iterable):
    # parses the database result to Question set paramater
    return iterable[0], iterable[1], iterable[2], iterable[3:7], iterable[7]
