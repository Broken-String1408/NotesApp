import json
import datetime
from notes.Note import Note
import os.path

class NoteCRUD():

    __FILE_NAME = "Notes.json"

    def __init__(self):
        if not os.path.exists(NoteCRUD.__FILE_NAME):
            self.__notes = []
        else :
            self.__notes = self.__loadNotesFromFile()


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

    def __findNoteById(self, id: int):
        for note in self.__notes:
            if note.id == id:
                return note

    def createNewNote(self, title: str, body: str):
        timeStamp = round(datetime.datetime.now().timestamp())
        newNote = Note(timeStamp, title, body, timeStamp)
        self.__addNote(newNote)

    def readAllNotes(self):
        return self.__notes.copy()

    def updateNote(self, id: int, title: str, body: str):
        noteToUpdate = self.__findNoteById(id)
        noteToUpdate.title = title
        noteToUpdate.body = body
        noteToUpdate.date = round(datetime.datetime.now().timestamp())
        self.__writeNotesToFile()

    def deleteNote(self, id: int):
        noteToDelete = self.__findNoteById(id)
        self.__notes.remove(noteToDelete)
        self.__writeNotesToFile()


