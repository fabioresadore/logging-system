# logging-system
- A simple and functional Python logging system for general purpose
- No extra packages needed!

## usage
```
from main import Logging

logger = Logging() # or other object name, this will write on the 'logfile.log' file, that is the dafault value
logger = Logging('somelog.log') # this will write the 'somelog.log' file

logger.get_all() # to read entire log
logger.get_debug() # to read the 'DEBUG' log
AS THE SAME FOR
logger.get_info()
logger.get_waning()
logger.get_critical()
logger.get_error()


logger.write("INFO", "some log text") # write the 'INFO' log in the log file
YOU CAN ALSO DO:
logger.debug("some log text")
logger.info("some log text")
logger.warning("some log text")
logger.danger("some log text")
logger.error("some log text")

logger.clean(whole=True) # to clean the entire log file
logger.clean("WARNING") # to clean the 'WARNING' logs on the log file
```

## pattern of the log file content
```
02-05-2020 10:17:30 INFO: some log text
02-05-2020 10:17:30 INFO: some log text
02-05-2020 10:17:30 DEBUG: some log text
02-05-2020 10:17:30 DEBUG: some log text
02-05-2020 10:17:30 DEBUG: some log text
```

## log types
* DEBUG
* INFO
* WARNING
* CRITICAL
* ERROR
