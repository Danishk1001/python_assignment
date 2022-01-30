# creating logger class
class Logger:
    def __init__(self):
        self.logs = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.logs:
            self.logs[message] = timestamp
            return True
        elif timestamp >= self.logs[message] + 10:
            self.logs[message] = timestamp
            return True
        else:
            return False


# test case
inputs = [[1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]

# creating a logger object
logger = Logger()

for timestamp, message in inputs:
    print(logger.shouldPrintMessage(timestamp, message))
