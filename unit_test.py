import unittest

# importing functions from anagram.py
from anagrams.anagrams import reverse_word
from anagrams.anagrams import reverse_sentence


class TestTypicalBehavior(unittest.TestCase):

    def test_reversing_word(self):

        expecting_result_of_word = [("0He1ll42o!", '0ol1le42H!'),
                                    ("P4!y>t0h<o4n", "n4!o>h0t<y4P")
                                    ]
        for word, reversed_word in expecting_result_of_word:
            with self.subTest(msg="Checking input: word, output: reversed_word"):
                self.assertEqual(reverse_word(word), reversed_word)

    def test_reversing_sentence(self):
        expecting_result_of_sentence = [("Th*i1s i!s m-y t1es%t", "si*h1T s!i y-m t1se%t"),
                                        ("It1 7i9s f!ir*st te)9s(t!", "tI1 7s9i t!sr*if ts)9e(t!"),
                                        ("", "")
                                        ]
        for sentence, reversed_sentence in expecting_result_of_sentence:
            with self.subTest(msg="Checking input: sentence, output: reversed_sentence"):
                self.assertEqual(reverse_sentence(sentence), reversed_sentence)


class TestAtypicalBehavior(unittest.TestCase):

    def test_atypical_behavior(self):
        # [int, float, list, tuple, dict, set, bool]
        list_wrong_input = [432123, 93.12, ["K9as6g >OskdS"], ("sad", "1sad", "asdf"),
                            {"First": "12", "Second": "834"}, {"d", "d", "e"}, True
                            ]
        for sentence in list_wrong_input:
            with self.subTest(msg="Checking when sentence not string",
                              input_sentence=sentence, type_sentence=type(sentence)):
                self.assertRaises(AttributeError, reverse_sentence, sentence)


# This is test
if __name__ == "__main__":
    unittest.main()
