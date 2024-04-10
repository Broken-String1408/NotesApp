import datetime


class Note:
    def __init__(self, id: int, title: str, body: str, date: int):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def __repr__(self):
        return self.title + "\n" + self.body + "\n" + "Дата изменения: " + str(
            datetime.datetime.fromtimestamp(self.date).strftime('%d-%m-%Y %H:%M:%S'))
