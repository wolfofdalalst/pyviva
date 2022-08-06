from re import template
import unittest

from pyviva import framework, database, templates


class TestFrameWork(unittest.TestCase):
    def setUp(self):
        self.uuid = framework._uuid()
        self.test_question_set = framework.QuestionSet(
            self.uuid, -1, "What's 9+10?", [19, 21, 20, None], 2
        )

    def test_return_csv_data(self):
        self.assertIsInstance(framework._return_csv_data(), list)

    def test_append_questions(self):
        # tearDown function will remove the newly created entry
        self.assertTrue(framework.append_question(self.test_question_set))

    def test_random_question(self):
        self.assertIsInstance(framework.random_question(diff=-1), templates.QuestionSet)

    def test_remove_question(self):
        self.assertTrue(framework.remove_question(self.uuid))

    def tearDown(self):
        framework.remove_question(self.uuid)


class TestDataBase(unittest.TestCase):
    def setUp(self):
        self.uuid = framework._uuid()
        self.test_question_set = templates.QuestionSet(
            self.uuid, -1, "What's 9+10?", [19, 21, 20, None], 2
        )

    def test_init_db(self):
        self.assertTrue(database.init_db())

    def test_insert_db(self):
        self.assertTrue(database.insert_db(self.test_question_set))

    def test_random_question_db(self):
        self.assertIsInstance(
            database.random_question_db(diff=-1), templates.QuestionSet
        )

    def test_remove_question_db(self):
        self.assertTrue(database.remove_question_db(self.uuid))

    def tearDown(self):
        database.remove_question_db(self.uuid)


if __name__ == "__main__":
    unittest.main()
