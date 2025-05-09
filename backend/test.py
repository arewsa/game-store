from schemas.token import AccessToken 
import time
import datetime


class test():
    a = datetime.datetime.now()


print(AccessToken(user_id=1).exp)
time.sleep(1)
print(AccessToken(user_id=1).exp)

print(test().a)
print(test().a)