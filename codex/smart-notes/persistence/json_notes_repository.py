import json
import os

from persistence.notes_repository import NotesRepository


class JsonNotesRepository(NotesRepository):
    def __init__(self, storage_file: str) -> None:
        self._storage_file = storage_file

    def load_notes(self) -> list[dict]:
        if not os.path.exists(self._storage_file):
            return []

        with open(self._storage_file, "r") as file:
            return json.load(file)

    def save_notes(self, notes: list[dict]) -> None:
        with open(self._storage_file, "w") as file:
            json.dump(notes, file, indent=2)
