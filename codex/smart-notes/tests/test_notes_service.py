import unittest
from unittest.mock import Mock

from services.notes_service import NotesService


class TestNotesService(unittest.TestCase):
    def setUp(self):
        self.repo = Mock()
        self.service = NotesService(self.repo)

    def test_create_note_appends_and_persists(self):
        self.repo.load_notes.return_value = []

        note = self.service.create_note("title", "content")

        self.repo.load_notes.assert_called_once_with()
        self.repo.save_notes.assert_called_once()
        saved_notes = self.repo.save_notes.call_args[0][0]
        self.assertEqual(len(saved_notes), 1)
        self.assertEqual(saved_notes[0]["id"], 1)
        self.assertEqual(saved_notes[0]["title"], "title")
        self.assertEqual(saved_notes[0]["content"], "content")
        self.assertFalse(saved_notes[0]["completed"])
        self.assertEqual(note, saved_notes[0])

    def test_list_notes_returns_repository_data(self):
        self.repo.load_notes.return_value = [{"id": 1, "title": "t", "content": "c", "created_at": "x", "completed": False}]

        notes = self.service.list_notes()

        self.repo.load_notes.assert_called_once_with()
        self.assertEqual(notes, self.repo.load_notes.return_value)

    def test_complete_note_marks_completed_and_persists(self):
        notes = [
            {"id": 1, "title": "t1", "content": "c1", "created_at": "x", "completed": False},
            {"id": 2, "title": "t2", "content": "c2", "created_at": "y", "completed": False},
        ]
        self.repo.load_notes.return_value = notes

        updated = self.service.complete_note(2)

        self.repo.load_notes.assert_called_once_with()
        self.repo.save_notes.assert_called_once_with(notes)
        self.assertTrue(updated["completed"])
        self.assertEqual(updated["id"], 2)

    def test_complete_note_returns_none_when_missing(self):
        self.repo.load_notes.return_value = [
            {"id": 1, "title": "t1", "content": "c1", "created_at": "x", "completed": False},
        ]

        updated = self.service.complete_note(99)

        self.repo.load_notes.assert_called_once_with()
        self.repo.save_notes.assert_not_called()
        self.assertIsNone(updated)

    def test_delete_note_filters_and_persists(self):
        self.repo.load_notes.return_value = [
            {"id": 1, "title": "t1", "content": "c1", "created_at": "x", "completed": False},
            {"id": 2, "title": "t2", "content": "c2", "created_at": "y", "completed": False},
        ]

        self.service.delete_note(1)

        self.repo.load_notes.assert_called_once_with()
        self.repo.save_notes.assert_called_once_with(
            [{"id": 2, "title": "t2", "content": "c2", "created_at": "y", "completed": False}]
        )


if __name__ == "__main__":
    unittest.main()
