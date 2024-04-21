#__________________| SCRIPT INFO |__________________#
# SCRIPT MAKED BY U7P4L 1N
# SC : FB AUTO COMMENT SENDING SCRIPT
# GITHUB : U7P4L-IN
# TEAM : ANONYMOUS CYBER
#_______________| IMPORT MODULES |________________#
import os
os.system("pip install fbtoolsbox")
from FBTools import Start

def Login():
    email = input('Input Your Email : ')#input your email
    password = input('Input Your Password : ')#input your password
    FB = Start(email=email, password=password)
    if FB.IsValid:
        BotComment(FB)
    else:
        exit(' Typing Invalid')

def BotComment(FB):
    post = input('Input ID Post : ')#input id post
    comt = input('Write Comment : ')#input comment
    loop = int(input('How Many : '))#input how many
    for i in range(loop):
        Comment = FB.CommentToPost(post=post, text=comt)
        print(Comment)

if __name__ == '__main__':
   Login()
#_______________| FINISHED |________________#

U7P4L 1N
ANONYMOUS CYBER ™ 
ANONYMOUS CYBER | OFFICIAL