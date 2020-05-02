# logging-system
A handmade logging system for general purpose

## usage
```
from main import Logging

logger = Logging() # or other object name, this will write on the 'logfile.log' file, that is the dafault value
logger = Logging('somelog.log') # this will write the 'somelog.log' file

logger.read() # to read entire log
logger.read("DEBUG") # to read the 'DEBUG' log

logger.write("INFO", "some log text") # write the 'INFO' log in the log file
YOU CAN ALSO DO:
logger.debug("some log text")
logger.info("some log text")
logger.warning("some log text")
logger.danger("some log text")
logger.error("some log text")

logger.clean() # to clean the entire log file
logger.clean("WARNING") # to clean the 'WARNING' logs on the log file
```

## pattern of the log file content
```
02-05-2020 10:17:30 INFO: algum log
02-05-2020 10:17:30 INFO: algum log
02-05-2020 10:17:30 DEBUG: algum log
02-05-2020 10:17:30 DEBUG: algum log
02-05-2020 10:17:30 DEBUG: algum log
```

## log types
* DEBUG
* INFO
* WARNING
* DANGER
* ERROR
