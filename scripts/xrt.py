import os
import time
import psutil


# Get pid by name
def get_pid(name):
    cmd = 'tasklist /FI "IMAGENAME eq %s" /NH' % name
    output = os.popen(cmd).read().strip()
    if output:
        try:
            return int(output.split()[1])
        except ValueError:
            print("Process not found")
            exit()
    else:
        print("Process not found")
        exit()


# define countdown and name
countdown = 5
pidName = 'pidName.exe'

# get pid
pid = get_pid(pidName)

# suspend the process
process = psutil.Process(pid)
process.suspend()
print(f"The process PID {pid} is suspended.")

# countdown
print(f"Resuming the process in {5} seconds")

while countdown > 0:
    print(f"{countdown}")
    time.sleep(1)
    countdown -= 1

# resume process
print("Resuming process")
process.resume()

print(f"The process with  PID {pid} is resumed.")
