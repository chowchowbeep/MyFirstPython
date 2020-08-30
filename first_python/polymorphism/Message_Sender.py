class MessageSender:
    def __init__(self):
        self._irum = "이기자"

    def get_irum(self):
        return self._irum

    def set_irum(self, irum):
        self._irum = irum

    irum = property(get_irum, set_irum)

    def sender_message(self): # 오버라이딩될 예정
        pass