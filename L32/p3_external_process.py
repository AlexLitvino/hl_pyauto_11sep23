"""
    os.system
    os.popen
    subprocess
"""
import os
from time import sleep


# os.system("sleep 2")
# result = os.system("gita --version")
# print()
# print(result)

#os.popen()

from subprocess import run, Popen, PIPE

# #run(['sleep', '3'])
# cmd = "ls -la"
# result = run(cmd.split(), capture_output=True, text=True)
# print(result)
# print(result.returncode)
# print(result.stdout)
# print(result.stderr)
# #print(result.stdout.decode())

# cmd = "python3 input_example.py"
# result = run(cmd.split(), capture_output=True, input=b'5')
# #result = run(cmd.split(), capture_output=True, text=True, input='5')
# print(result.returncode)
# print(result.stdout)

cmd = "bash script.sh"
#process = Popen(cmd.split(), stdout=PIPE)

# with open('output.log', 'w') as f:
#     process = Popen(cmd.split(), stdout=f)
process = Popen(cmd.split())
stdout, stderr = process.communicate(timeout=2)
for i in range(5):
    print("In Main")
    sleep(0.8)


print(stdout)
print(stderr)

print("After process")