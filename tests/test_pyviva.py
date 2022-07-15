import unittest

from pyviva import framework


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
        self.assertIsInstance(framework.random_question(diff=-1), framework.QuestionSet)

    def test_remove_question(self):
        self.assertTrue(framework.remove_question(self.uuid))

    def tearDown(self):
        framework.remove_question(self.uuid)


if __name__ == "__main__":
    unittest.main()
