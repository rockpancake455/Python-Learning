class Letter:
    Title: str
    Message: str
    Sender: str

    def __init__(self, title:str, message:str, sender:str):
        self.Title = title
        self.Message = message
        self.Sender = sender
        
    def GetHeader(self):
        return f"{self.Title} from {self.Sender}"

    def GetMessage(self):
        return f"{self.Title}\n\n{self.Message}\n\nFrom: {self.Sender}"

MailBox: list[Letter] = [] 