from Email_Sender import EmailSender
from SMS_Sender import SMSSender

def send(message):
    message.sender_message() # 메소드 다형성


if __name__ == "__main__":
    obj1 = EmailSender()
    obj1.irum = "김초롱"
    obj1.email = "aaa@daum.net"
    send(obj1)
    print()
    obj2 = SMSSender()
    obj2.irum = "김초로롤"
    obj2.tel = "010-1111-1111"
    send(obj2)