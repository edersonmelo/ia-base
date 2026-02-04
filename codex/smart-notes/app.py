import sys

from persistence.json_notes_repository import JsonNotesRepository
from services.notes_service import NotesService

STORAGE_FILE = "storage.json"


def print_notes(notes):
    for note in notes:
        status = "✓" if note["completed"] else " "
        print(f"[{status}] {note['id']} - {note['title']}")


def main():
    service = NotesService(JsonNotesRepository(STORAGE_FILE))

    if len(sys.argv) < 2:
        print("Uso:")
        print("  add <title> <content>")
        print("  list")
        print("  complete <id>")
        print("  delete <id>")
        return

    command = sys.argv[1]

    if command == "add":
        title = sys.argv[2]
        content = sys.argv[3]
        note = service.create_note(title, content)
        print("Nota criada:", note)

    elif command == "list":
        notes = service.list_notes()
        print_notes(notes)

    elif command == "complete":
        note_id = int(sys.argv[2])
        note = service.complete_note(note_id)
        if note:
            print("Nota concluída:", note)
        else:
            print("Nota não encontrada")

    elif command == "delete":
        note_id = int(sys.argv[2])
        service.delete_note(note_id)
        print("Nota removida")

    else:
        print("Comando inválido")


if __name__ == "__main__":
    main()
