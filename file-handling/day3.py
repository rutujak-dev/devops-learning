with open("log.txt","r") as file:
    error_count = 0
    info_count = 0
    warning_count = 0
    debug_count = 0

    for line in file:
        line = line.strip()

        if "ERROR" in line:
            error_count += 1
        elif "INFO" in line:
            info_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "DEBUG" in line:
            debug_count += 1

print ("Log summary:")
print ("Error count:", error_count)
print ("Info count:", info_count)
print ("Warning count:", warning_count)
print ("Debug count:", debug_count)