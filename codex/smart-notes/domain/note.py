from dataclasses import dataclass
from datetime import datetime


@dataclass
class Note:
    id: int
    title: str
    content: str
    created_at: str
    completed: bool

    @staticmethod
    def create(note_id: int, title: str, content: str) -> "Note":
        return Note(
            id=note_id,
            title=title,
            content=content,
            created_at=datetime.now().isoformat(),
            completed=False,
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at,
            "completed": self.completed,
        }
