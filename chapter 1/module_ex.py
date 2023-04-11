#print the operating system plat
# import sys
# sys.platform

#print version of python
# import sys
# print (sys.version)

#name of folder on which the code is running
# import os
# os.getcwd()

#you can access your system's environment variable as a whole (using environ attribute or by using getenv function)
# import os
# os.environ
# os.getenv('HOME') #it can access a specifically named attribute (from the data contained in "environ") using "getenv"

# import datetime
# print(datetime.date.today().day) #output on 07-04-2023 as 7
# print(datetime.date.today().month) #output on 07-04-2023 as 4
# print(datetime.date.today().year) #output on 07-04-2023 as 2023

#for user friendly version of today's date (07-04-2023)
# import datetime
# print(datetime.date.isoformat(datetime.date.today())) #output 2023-04-07

#to display time
# import time
# print(time.strftime("%H:%M")) # H is for hour and M is for minutes

#for day of the week and AM or PM
# import time
# print(time.strftime("%A %p")) # output is Friday PM

#converting to and from HTML encoded text
# import html
# print(html.escape("This HTML fragment contains a <script> script </script> tag.")) #output is This HTML fragment contains a &lt;script&gt; script &lt;/script&gt; tag.
# print(html.unescape("I &hearts; Python's &lt; standard library &gt;.")) #output is I ♥ Python's < standard library >.