import time
from datetime import datetime


exersize_time = datetime.now()

dt_string = exersize_time.strftime("%d/%m/%Y %H:%M:%S")

print(exersize_time)
print(type(exersize_time))

print(dt_string)
print(type(dt_string))