from Message_Sender import *
#Message_Sender 모듈 내의 모든 내용을 임포트함

class EmailSender(MessageSender):
    def __init__(self):
        super().__init__()
        self._email = ""

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    email = property(get_email, set_email)

    def sender_message(self): # MessageSender의 메소드를 상속받아 오버라이딩
        print("이름 : %s" % self._irum)
        print("이메일 : %s" % self._email)