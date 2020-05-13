#################################################################
#   LOGGING SYSTEM                                              #
#                                                               #
# e.g.                                                          #
# input: Logging(logfile.log).debug('some log')                 #
# output:                                                       #
#   write a new line in 'logfile.log':                          #
#       '00/00/0000 00:00:00 DEBUG: somelog'                    #
#################################################################

import os
import datetime


class Logging:
    def __init__(self, file: str = 'logfile.log'):
        assert type(file) is str, "'file' argument type in the Logging instance needs to be string. Provided: {}".format(
            type(file))

        self.file = file
        self.log_dir = ""
        self.log_types = [
            'DEBUG',
            'INFO',
            'WARNING',
            'CRITICAL',
            'ERROR'
        ]

    def file_handling(self, content: str = '', read: bool = False, write: bool = False):

        assert type(content) is str, "'content' type needs to be string. Provided: {}".format(
            type(content))
        assert type(read) is bool, "'read' type needs to be boolean. Provided: {}".format(
            type(read))
        assert type(write) is bool, "'write' type needs to be boolean. Provided: {}".format(
            type(write))

        if read == False and write == False:
            raise ValueError(
                "At least one of 'read' or 'write' arguments must be True")
        elif read and write:
            raise ValueError("Only 'read' and 'write' argument can be True")
        if write and content == '':
            raise ValueError(
                "'content' argument needs to have some value. Provided: {}".format(content))

        log_file = self.log_dir + self.file
        file_content = ''
        if os.path.isfile(log_file):
            open_type = "r" if read else "a"
        else:
            open_type = "w"
        with open(log_file, open_type) as file:
            if open_type == 'w':
                file.write(content)
                return content
            else:
                if read:
                    return file.read()
                elif write:
                    file.write(content)

            file.close()

    def clean(self, log_type: str = '', whole: bool = False):
        '''
        Make a clean in log file


        whole: turn this True if you wanna to clean the entire file
        log_type: the log type, see self.log_types to valids type list
        '''

        assert type(log_type) is str, "'log_type' type needs to be string. Provided: {}".format(
            type(log_type))
        assert type(whole) is bool, "'whole' type needs to be boolean. Provided: {}".format(
            type(log_type))

        log_file = self.log_dir + self.file
        if whole and log_type == '':
            with open(log_file, "w") as file:
                file.write('')
                file.close()
        elif whole and log_file != '':
            raise ValueError(
                "when 'whole' is True, the 'log_type' needs to be empty. Provided: {}".format(log_type))
        elif whole == False and log_type in self.log_types:
            new_lines = ''
            with open(log_file, "r") as file:
                lines = file.readlines()
                if len(lines) > 0:
                    for x in range(len(lines)):
                        if log_type in lines[x]:
                            lines[x] = ''
                    new_lines = ''.join(lines)
                file.close()
            with open(log_file, "w") as file:
                file.write(new_lines)
                file.close()
        else:
            raise ValueError(
                "'log_type' needs to be a valid log type value. Provided: {}".format(log_type))

    def write(self, log_type: str, log_text: str):
        '''
        Writes a log in the log file


        log_type: the log type, see self.log_types to valids type list
        log_text: the log text
        '''

        assert log_type in self.log_types, "'log_type' needs to be a valid log type value. Provided: {}".format(
            log_type)

        now = datetime.datetime.now()
        log_line = "%s %s: %s\n" % (now.strftime(
            "%d-%m-%Y %H:%M:%S"), log_type, log_text)

        self.file_handling(log_line, write=True)

    def read(self, log_type: str = 'ALL') -> list:
        '''
        Read the log file


        log_type: the log type, see self.log_types to valids type list
        '''

        if type(log_type) is str:
            all_log = self.file_handling(read=True).split("\n")
            if log_type == 'ALL':
                return all_log
            else:
                assert log_type in self.log_types, "'log_type' needs to be a valid log type value. Provided: {}".format(
                    log_type)

                typed_log = []
                for logline in all_log:
                    if log_type in logline:
                        typed_log.append(logline)
                return typed_log
        else:
            raise TypeError(
                "'log_type' typ needs to be string. Provided: {}".format(type(log_type)))

    def debug(self, log_text: str):
        if type(log_text) is str:
            self.write("DEBUG", log_text)
        else:
            raise TypeError(
                "'log_text' typ needs to be string. Provided: {}".format(type(log_text)))

    def info(self, log_text: str):
        if type(log_text) is str:
            self.write("INFO", log_text)
        else:
            raise TypeError(
                "'log_text' typ needs to be string. Provided: {}".format(type(log_text)))

    def warning(self, log_text: str):
        if type(log_text) is str:
            self.write("WARNING", log_text)
        else:
            raise TypeError(
                "'log_text' typ needs to be string. Provided: {}".format(type(log_text)))

    def critical(self, log_text: str):
        if type(log_text) is str:
            self.write("CRITICAL", log_text)
        else:
            raise TypeError(
                "'log_text' typ needs to be string. Provided: {}".format(type(log_text)))

    def error(self, log_text: str):
        if type(log_text) is str:
            self.write("ERROR", log_text)
        else:
            raise TypeError(
                "'log_text' typ needs to be string. Provided: {}".format(type(log_text)))

    def get_all(self) -> list:
        return self.read()

    def get_debug(self) -> list:
        return self.read(log_type='DEBUG')

    def get_info(self) -> list:
        return self.read(log_type='INFO')

    def get_warning(self) -> list:
        return self.read(log_type='WARNING')

    def get_critical(self) -> list:
        return self.read(log_type='CRITICAL')

    def get_error(self) -> list:
        return self.read(log_type='ERROR')
