from notes.NoteCRUD import NoteCRUD
from notes.Note import Note
from operator import attrgetter

class NotesApp():

    def __init__(self):
        self.__crud = NoteCRUD()
        self.__notes : list[Note] = []


    def run(self):
        isToRun = True
        while isToRun:
            self.__notes = self.__crud.readAllNotes()
            self.__sortNotesByDate()
            if not self.__notes:
                print()
                print("Пока нет записей")
                print()
                isToRun = self.__runNewOperation("1 - добавить запись", range(1,2))
            else:
                self.__displayNotes()
                isToRun = self.__runNewOperation("1 - добавить запись | 2 - ред.запись | 3 - удалить запись", range(1, 4))


    def __runNewOperation(self, prompt: str, numOfCommands: range):
        command = input(prompt + " | x - выход\n")
        if command.isdigit():
            command = int(command)
            if command in numOfCommands:
                match command:
                    case 1:
                        self.__addNewNote()
                    case 2:
                        self.__updateNote()
                    case 3:
                        self.__deleteNote()
            else:
                print("Неверная комманда!")
        else:
            match command:
                case "x":
                    print("До свидания!")
                    return False
                case _:
                    print("Некорректный ввод")
        return True
    def __addNewNote(self):
        title = input("Введите заголовок записи\n")
        body = input("Введите текст записи\n")
        self.__crud.createNewNote(title, body)

    def __deleteNote(self):
        index = self.__getNoteIndexFromUserInput(" для удаления\n")
        if index is not None:
            noteToDeleteId = self.__notes[index].id
            self.__crud.deleteNote(noteToDeleteId)

    def __updateNote(self):
        index = self.__getNoteIndexFromUserInput(" для редактирования\n")
        if index is not None:
            print(self.__notes[index])
            title = input("Введите новый заголовок записи\n")
            body = input("Введите новый текст записи\n")
            noteToUpdateId = self.__notes[index].id
            self.__crud.updateNote(noteToUpdateId, title, body)

    def __getNoteIndexFromUserInput(self, prompt: str):
        try:
            index = int(input("Введите номер записи" + prompt)) - 1
            if 0 <= index < len(self.__notes):
                return index
            else:
                print("Несуществующий номер записи\n")
        except ValueError:
            print("Некорректный ввод\n")


    def __displayNotes(self):
        for i, note in enumerate(self.__notes):
            print(f"{i + 1} : {note}")

    def __sortNotesByDate(self):
        self.__notes.sort(key= attrgetter("date"), reverse=True)


NotesApp().run()