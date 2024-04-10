import json
import datetime
from notes.Note import Note
import os.path
from operator import attrgetter


class NoteCRUD:
    __FILE_NAME = "Notes.json"

    def __init__(self):
        if not os.path.exists(NoteCRUD.__FILE_NAME):
            self.__notes = []
        else:
            self.__notes = self.__loadNotesFromFile()
            self.__sortNotes()

    def __addNote(self, newNote: Note):
        self.__notes.append(newNote)
        self.__writeNotesToFile()

    def __loadNotesFromFile(self):
        with open(NoteCRUD.__FILE_NAME, "r") as notes_file:
            json_string = json.load(notes_file)
            return [Note(**note) for note in json_string]

    def __writeNotesToFile(self):
        json_string = json.dumps([note.__dict__ for note in self.__notes], indent=4)
        with open(NoteCRUD.__FILE_NAME, "w", encoding='utf-8') as notes_file:
            notes_file.write(json_string)

    def __sortNotes(self):
        self.__notes.sort(key=attrgetter("date"), reverse=True)

    def createNewNote(self, title: str, body: str):
        timeStamp = round(datetime.datetime.now().timestamp())
        newNote = Note(timeStamp, title, body, timeStamp)
        self.__addNote(newNote)

    def readAllNotes(self):
        return self.__notes.copy()

    def updateNote(self, index: int, title: str, body: str):
        self.__notes[index].title = title
        self.__notes[index].body = body
        self.__notes[index].date = round(datetime.datetime.now().timestamp())
        self.__writeNotesToFile()
        self.__sortNotes()

    def deleteNote(self, index: int):
        self.__notes.pop(index)
        self.__writeNotesToFile()



