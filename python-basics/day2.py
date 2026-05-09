logs = ["error", "error", "error", "error"]

error_count=0

for log in logs:
    if log=="info":
        error_count += 1

print("Total error:", error_count)

