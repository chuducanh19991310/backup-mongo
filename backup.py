import os
import time

'''
    mongo backup by python
    developrt: mr-exception
    github: mr-exception
'''


cwd = os.getcwd()

# configs:
interval_m = 0.2
outputs_dir = os.path.join(cwd, "./data-backup")

host = "localhost" # if host is your local machine leave it NA
port = "3021" # if mongo is on default port (37017) leave in NA

username = "root" # if there is no username set, leave it in NA
password = "root" # if there is no password set, leave it in NA

def render_output_locations():
  return os.path.join(outputs_dir, "data"+time.strftime("%d-%m-%Y-%H:%M:%S"))

def run_backup():
  command = "mongodump --forceTableScan "
  if host != 'NA':
    command += " --host " + host
  if port != 'NA':
    command += " --port " + port
  if username != 'NA':
    command += " --username " + username
  if password != 'NA':
    command += " --password " + password
  
  command += " --out " + render_output_locations()
  print (command)
  os.system(command)

print("mongo backup progress started")
print("I will backup your mongo db every {0} minutes".format(interval_m))

while True:
  run_backup()
  time.sleep(interval_m * 60)