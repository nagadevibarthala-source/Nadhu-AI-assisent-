import unittest

import voice


class VoiceCommandTests(unittest.TestCase):

    def test_youtube_is_handled(self):
        self.assertTrue(
            voice.should_handle("opening youtube")
        )

    def test_wake_word_is_handled(self):
        self.assertTrue(
            voice.should_handle("nadhu opening youtube")
        )

    def test_nandu_is_handled(self):
        self.assertTrue(
            voice.should_handle("nandu opening youtube")
        )

    def test_unknown_command_is_not_handled(self):
        self.assertFalse(
            voice.should_handle("hello there")
        )

    def test_normalize_removes_nadhu(self):
        self.assertEqual(
            voice.normalize_command(
                "nadhu opening youtube"
            ),
            "opening youtube"
        )

    def test_normalize_removes_nandu(self):
        self.assertEqual(
            voice.normalize_command(
                "nandu opening youtube"
            ),
            "opening youtube"
        )


if __name__ == "__main__":
    unittest.main()
