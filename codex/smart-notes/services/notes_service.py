from domain.note import Note
from persistence.notes_repository import NotesRepository


class NotesService:
    def __init__(self, repository: NotesRepository) -> None:
        self._repository = repository

    def create_note(self, title: str, content: str) -> dict:
        notes = self._repository.load_notes()
        note = Note.create(len(notes) + 1, title, content)
        notes.append(note.to_dict())
        self._repository.save_notes(notes)
        return note.to_dict()

    def list_notes(self) -> list[dict]:
        return self._repository.load_notes()

    def complete_note(self, note_id: int) -> dict | None:
        notes = self._repository.load_notes()

        for note in notes:
            if note["id"] == note_id:
                note["completed"] = True
                self._repository.save_notes(notes)
                return note

        return None

    def delete_note(self, note_id: int) -> None:
        notes = self._repository.load_notes()
        new_notes = [note for note in notes if note["id"] != note_id]
        self._repository.save_notes(new_notes)
