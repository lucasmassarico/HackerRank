from datetime import datetime


# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
def time_Conversion(hour):
    format_data_12 = "%I:%M:%S%p"
    date = datetime.strptime(hour, format_data_12)
    format_data_24 = "%H:%M:%S"
    return datetime.strftime(date, format_data_24)


if __name__ == '__main__':
    s = input()
    result = time_Conversion(s)
    print(result)
