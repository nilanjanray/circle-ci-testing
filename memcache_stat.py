import sys
import subprocess
import telnetlib
import pprint
arguments = sys.argv[1:]


def ping_to_memcache(arguments):
  if (':' in arguments[0]):
    command = arguments[0].split(':')
    statscommand = "stats" + " " + command[0] + " " + command[1] + " " + command[2]
  
  else:
    statscommand = "stats" + " " + sys.argv[1]

  try:
    tn = telnetlib.Telnet(sys.argv[2], sys.argv[3], timeout = 120)
    tn.write(statscommand + "\n")
    tn.write("exit\n")
    
    #print(tn.set_debuglevel(10000))
    memory = buffer(tn.read_until('END', 120))
    print(memory)
    
  except:
    print('Unable to connect with server')
  finally:
    tn.close()

if (__name__ == '__main__'):
  ping_to_memcache(arguments)

