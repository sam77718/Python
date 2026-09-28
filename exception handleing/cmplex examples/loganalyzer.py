# def analyze_logs(logs):
#     ...

# You are given a list of log entries:

# logs = [
#     "2026-09-01 INFO User login",
#     "2026-09-01 ERROR Database connection failed",
#     "2026-09-01 WARNING High memory usage",
#     "2026-09-02 INFO User logout",
#     "2026-09-02 ERROR File not found",
#     "2026-09-02 ERROR Database connection failed",
#     "2026-09-03 INFO User login",
#     "2026-09-03 WARNING Disk space low"
# ]

# Your function must:

# Count how many INFO, WARNING, and ERROR logs exist.
# Find the most common error message.
# Count errors for each date.
# Find the date with the highest number of errors.
# Return a dictionary in this format:
# {
#     "log_counts": {
#         "INFO": 3,
#         "WARNING": 2,
#         "ERROR": 3
#     },
#     "most_common_error": "Database connection failed",
#     "errors_by_date": {
#         "2026-09-01": 1,
#         "2026-09-02": 2
#     },
#     "worst_date": "2026-09-02"
# }


logs = [
    "2026-09-01 INFO User login",
    "2026-09-01 ERROR Database connection failed",
    "2026-09-01 WARNING High memory usage",
    "2026-09-02 INFO User logout",
    "2026-09-02 ERROR File not found",
    "2026-09-02 ERROR Database connection failed",
    "2026-09-03 INFO User login",
    "2026-09-03 WARNING Disk space low"
]


def analyze_logs(logs):

    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    # Count log levels
    for log in logs:
        parts = log.split()
        level = parts[1]

        if level in counts:
            counts[level] += 1

    # Count error messages
    error_counts = {}

    for log in logs:
        parts = log.split()

        if parts[1] == "ERROR":
            message = " ".join(parts[2:])

            error_counts[message] = error_counts.get(message, 0) + 1

    # Find most common error
    most_common_error = max(
        error_counts,
        key=error_counts.get
    )

    # Count errors for each date.
    errors_by_date = {}
    for log in logs:
        parts = log.split()
        if parts[1] == "ERROR":
            date = parts[0]
            errors_by_date[date] = errors_by_date.get(date, 0) + 1

    # Find the date with the highest number of errors.
    worst_date = max(errors_by_date, key=errors_by_date.get)
    for date, count in errors_by_date.items():
        if count == errors_by_date[worst_date]:
            worst_date = date
            break
        

    # Return all results
    result = {
    "log_counts": counts,
    "most_common_error": most_common_error,
    "errors_by_date": errors_by_date,
    "worst_date": worst_date
}



    return result


result = analyze_logs(logs)

print(result)