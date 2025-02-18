from datetime import datetime

date1 = datetime(2024, 2, 1, 12, 0, 0)
date2 = datetime(2024, 2, 10, 15, 30, 0)

difference = (date2 - date1).total_seconds()
print(difference)
