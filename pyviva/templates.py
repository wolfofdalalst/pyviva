class QuestionSet:
    def __init__(self, *args):
        """Structure for maintaining question set. Calling the object will return the question set list
        >>> question_set = QuestionSet(*example_args)
        >>> question_set()
        < class 'list'>

        Args:
            uid (int): unique id
            diff (int): difficulty of the question, -1 for testing
            question (str): question literal
            options (list): list with 4 options
            answers (int): integer with correct answer number
        """
        self.args = args
        [self.uid, self.diff, self.question, self.options, self.answer] = self.args

    def __call__(self) -> list:
        # >>> question_set()
        return self.args

    def __repr__(self) -> str:
        # >>> print(question_set)
        return str(self.__call__())