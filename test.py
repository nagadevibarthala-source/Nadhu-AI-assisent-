import unittest
from unittest.mock import patch

import voice


class VoiceCommandTests(unittest.TestCase):
    def test_opening_youtube_is_handled_without_wake_word(self):
        self.assertTrue(voice.should_handle("opening youtube"))

    def test_nandu_opening_youtube_is_handled(self):
        self.assertTrue(voice.should_handle("nandu opening youtube"))

    def test_nadhuku_opening_youtube_is_handled(self):
        self.assertTrue(voice.should_handle("nadhuku opening youtube"))

    def test_sat_nadhu_open_youtube_is_handled(self):
        self.assertTrue(voice.should_handle("sat nadhu open youtube"))

    def test_unknown_commands_are_not_handled(self):
        self.assertFalse(voice.should_handle("hello there"))

    def test_normalize_command_removes_wake_words(self):
        self.assertEqual(
            voice.normalize_command("nadhu opening youtube"),
            "opening youtube",
        )

    def test_normalize_command_removes_nandu(self):
        self.assertEqual(
            voice.normalize_command("nandu opening youtube"),
            "opening youtube",
        )

    @patch("voice.webbrowser.open")
    @patch("voice.talk", side_effect=RuntimeError("tts failed"))
    def test_handle_command_still_opens_youtube_when_tts_fails(
        self,
        _talk_mock,
        open_mock,
    ):
        self.assertTrue(voice.handle_command("sat nadhu open youtube"))
        open_mock.assert_called_once_with("https://youtube.com")


if __name__ == "__main__":
    unittest.main()