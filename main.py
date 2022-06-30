import time
import timeago

timestamp = time.time() - 30
timestamp_in_the_future = time.time() + 90
print(timeago.format(timestamp, timestamp_in_the_future))
