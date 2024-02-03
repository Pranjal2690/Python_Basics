import time as T

current_time = T.localtime(T.time())
formatted_time = T.strftime("%Y-%m-%d %H:%M:%S", current_time)
print("Current time is", formatted_time)