import channel
import subprocess

p = subprocess.Popen(['python', 'child.py'], \
                    stdin=subprocess.PIPE, \
                    stdout=subprocess.PIPE)
ch = channel.Channel(p.stdin, p.stdout)

