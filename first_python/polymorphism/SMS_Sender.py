from Message_Sender import *

class SMSSender(MessageSender):
    def __init__(self):
        super().__init__()
        self._tel = ""

    def get_tel(self):
        return self._tel

    def set_tel(self, tel):
        self._tel = tel

    tel = property(get_tel, set_tel)

    def sender_message(self):  # MessageSender의 메소드를 상속받아 오버라이딩
        print("이름 : %s" % self._irum)
        print("sms : %s" % self._tel)