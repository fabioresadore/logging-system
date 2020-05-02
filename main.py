#################################################################
#   LOGGER HANDLER                                              #
#                                                               #
# e.g.                                                          #
# input: logSystem('INFO', 'foi feita uma submissao')           #
# output:                                                       #
#   write a new line in 'django_log.log':                       #
#       '0/0/0000 0:0:0 INFO: foi feita uma submissao'          #
#################################################################

import os
import datetime
import json


class Logging:
    def __init__(self, file='logfile.log'):
        if type(file) is not str:
            raise TypeError(
                "'file' type in the Logging instance needs to be string. Provided: {}".format(type(file)))
        self.file = file
        self.log_dir = ""
        self.log_types = [
            'DEBUG',
            'INFO',
            'WARNING',
            'DANGER',
            'ERROR'
        ]

    def file_handling(self, content='', read=False, write=False):
        if type(content) is not str:
            raise TypeError(
                "'content' type needs to be string. Provided: {}".format(type(content)))
        if type(read) is not bool:
            raise TypeError(
                "'read' type needs to be boolean. Provided: {}".format(type(read)))
        if type(write) is not bool:
            raise TypeError(
                "'write' type needs to be boolean. Provided: {}".format(type(write)))
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

    def clean(self, log_type='', whole=False):
        '''
        Make a clean in log file


        whole: turn this True if you wanna to clean the entire file
        log_type: the log type, see self.log_types to valids type list
        '''

        if type(log_type) is not str:
            raise TypeError(
                "'log_type' type needs to be string. Provided: {}".format(type(log_type)))
        if type(whole) is not bool:
            raise TypeError(
                "'whole' type needs to be boolean. Provided: {}".format(type(log_type)))
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

        if log_type not in self.log_types:
            raise ValueError(
                "'log_type' needs to be a valid log type value. Provided: {}".format(log_type))
        now = datetime.datetime.now()
        log_line = "%s %s: %s\n" % (now.strftime(
            "%d-%m-%Y %H:%M:%S"), log_type, log_text)

        self.file_handling(log_line, write=True)

    def read(self, log_type: str = 'ALL'):
        '''
        Read the log file


        log_type: the log type, see self.log_types to valids type list
        '''

        if type(log_type) is str:
            all_log = self.file_handling(read=True).split("\n")
            if log_type == 'ALL':
                return all_log
            else:
                if log_type not in self.log_types:
                    raise ValueError(
                        "'log_type' needs to be a valid log type value. Provided: {}".format(log_type))
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

    def danger(self, log_text: str):
        if type(log_text) is str:
            self.write("DANGER", log_text)
        else:
            raise TypeError(
                "'log_text' typ needs to be string. Provided: {}".format(type(log_text)))

    def error(self, log_text: str):
        if type(log_text) is str:
            self.write("ERROR", log_text)
        else:
            raise TypeError(
                "'log_text' typ needs to be string. Provided: {}".format(type(log_text)))
