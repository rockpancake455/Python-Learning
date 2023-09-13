import Questing

class Letter:

    Title: str
    Message: str
    Sender: str
    LinkedQuest: Questing.Quest

    def __init__(self, title:str, message:str, sender:str, linkedQuest: Questing.Quest):
        self.Title = title
        self.Message = message
        self.Sender = sender
        self.LinkedQuest = linkedQuest

    def GetHeader(self):
        return f"{self.Title} from {self.Sender}"

    def GetMessage(self):
        return f"{self.Title}\n\n{self.Message}\n\nFrom: {self.Sender}"
        

MailBox: list[Letter] = [] 