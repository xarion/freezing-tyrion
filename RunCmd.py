import subprocess
import threading

# found this online, modified a bit.
# http://stackoverflow.com/questions/4158502/python-kill-or-terminate-subprocess-when-timeout

class RunCmd(threading.Thread):
    def __init__(self, cmd, timeout):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.timeout = timeout

    def run(self):
        self.p = subprocess.Popen(self.cmd, shell=True, stdout=subprocess.PIPE)
        self.p.wait()

    def Run(self):
        self.start()
        self.join(self.timeout)

        if self.is_alive():
            self.p.kill()
            self.join()
            return "command timed out"
        else:
            return self.p.stdout.read()