# logging-system
A handmade logging system for general purpose

## usage
```
from main import Logging

logger = Logging() # or other object name, this will write on the 'logfile.log' file, that is the dafault value
logger = Logging('somelog.log') # this will write the 'somelog.log' file

logger.read() # to read entire log
logger.read("DEBUG") # to read the 'DEBUG' log

logger.write("INFO", "some log test") # write the 'INFO' log in the log file

logger.clean() # to clean the entire log file
logger.clean("WARNING") # to clean the 'WARNING' logs on the log file
```
## log types
* DEBUG
* INFO
* WARNING
* DANGER
* ERROR
