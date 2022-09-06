from pushbullet import Pushbullet 

API_KEY = 'o.7AGZM4ffVX18FtfGK8Xyuczjhnp0MDNX'

def PushNote(title, body,API_KEY):
    pb = Pushbullet(API_KEY)
    message = pb.push_note(title, body)


def PushLink(title, body, Link,API_KEY):
    pb = Pushbullet(API_KEY)
    message = pb.push_link(title, Link, body)
