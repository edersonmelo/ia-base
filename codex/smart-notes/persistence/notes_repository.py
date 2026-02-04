from abc import ABC, abstractmethod


class NotesRepository(ABC):
    @abstractmethod
    def load_notes(self) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    def save_notes(self, notes: list[dict]) -> None:
        raise NotImplementedError
