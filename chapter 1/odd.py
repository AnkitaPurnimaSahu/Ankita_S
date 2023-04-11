from datetime import datetime
import time
odds = [1,3,5,7,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,51,53,55,57,59]
right_this_minute = datetime.today().minute
for i in range(5):
    time.sleep(5)
    if right_this_minute in odds:
        print("This minute seems a little odd.")
        print(right_this_minute)
    else:
        print("Not an odd minute.")
        print(right_this_minute)