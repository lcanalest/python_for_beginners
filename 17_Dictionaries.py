# Dictionaries (2:07:19)
## También llamado "key value pairs"

month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

result = month_conversions["Mar"]
print(result)

result = month_conversions.get("Feb", "Not a valid key")
print(result)

result = month_conversions.get("Lux", "Not a valid key")
print(result)