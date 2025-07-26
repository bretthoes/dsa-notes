from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # define a sort key using a tuple
        def sortKey(log: str):
            
            # unpack the log; identifier and content
            identifier, content = log.split(' ', 1)

            # if its a digit-log, return a tuple
            # that is equal for all digits and
            # greater than all letter-logs
            if content[0].isdigit():
                return (1,)

            # if its a letter-log, return a tuple
            # that will lexographically sort first
            # by the letter-log content, then by
            # the letter-log identifier
            return (0, content, identifier)

        logs.sort(key=sortKey)
        return logs
