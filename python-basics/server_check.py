server = "Server1"
status = "running"
cpu_usage = 90

print ("Checking server", server)

if status == "running":
    print ("Server is running")
else:
    print ("Server need attention")

if cpu_usage > 80:
    print ("High CPU Usage alert")
else:
    print ("CPU under control")