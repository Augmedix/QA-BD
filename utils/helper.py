import datetime
import random
import string
import time
import calendar
import re
import platform
import csv
from datetime import timedelta
import pytz
from pytz import timezone

def wait_for_next_minute():
    # Check the current second is between 40 to 59 seconds. If it is then waiting 20 seconds.
    myobj = datetime.datetime.now()
    print(myobj.second)
    if (40 <= myobj.second and myobj.second <= 59):
        print('waiting 20 seconds')
        time.sleep(20)


def generate_password(length=15):
    # define all possible characters
    chars = string.ascii_letters + string.digits + string.punctuation
    # ensure the password includes at least one lowercase letter, one uppercase letter, 
    # one special character, and one digit
    while True:
        password = ''.join(random.choice(chars) for _ in range(length))
        if (any(char.islower() for char in password)
                and any(char.isupper() for char in password)
                and any(char in string.punctuation for char in password)
                and any(char.isdigit() for char in password)):
            break

    return password


def generate_custom_id(length: int) -> str:
    """
        Generates a custom id.
    """
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


def generate_random_alphanumeric_string(string_lenght=10):
    """
    Generates random alphanumeric string for specified length.
    :param string_lenght: length of the expected random string. Default length is 10.
    :return: alphanumeric string of specified length.
    """
    alpha_numeric_string = string.ascii_letters + string.digits
    return ''.join(random.choice(alpha_numeric_string) for _ in range(string_lenght))



def generate_random_string(length=4):
    # Define the character set: lowercase, uppercase letters
    characters = string.ascii_letters  # Includes both lowercase and uppercase letters
    # Generate the random string
    random_string = ''.join(random.choices(characters, k=length))
    return random_string


def get_time_difference(start_time, end_time):
    m2 = start_time
    m2 = datetime.datetime.strptime(m2, '%I:%M %p')
    print(m2)
    m3 = end_time
    m3 = datetime.datetime.strptime(m3, '%I:%M %p')

    print(m3 - m2)
    difference = m3 - m2
    hour_minute_array = str(difference).split(':')

    hour = hour_minute_array[0] + 'h'
    minute = hour_minute_array[1] + 'm'
    return hour, minute


def get_formatted_date_str(_days=0, _date_format='%a, %m/%d'):
    # Define the PST time zone
    pst = pytz.timezone('America/Los_Angeles')

    # Get the current time in PST and adjust by the number of days
    date = datetime.datetime.now(pst) + datetime.timedelta(days=_days)

    # Check for platform compatibility
    if platform.system() == 'Windows':
        # On Windows, handle leading zeros manually
        formatted_date = date.strftime(_date_format)
        return formatted_date.replace('/0', '/').replace(', 0', ', ')
    else:
        # On Unix-based systems (Linux/macOS), use %-m and %-d directly
        return date.strftime(_date_format)


def get_formatted_time_of_lamdatest_device(driver, _date_format='%a, %-m/%-d'):
    # Execute the mobile:deviceInfo Appium command to get the device time
    device_info = driver.execute_script('mobile:deviceInfo')
    
    if 'time' not in device_info:
        raise KeyError('Device time not found in the returned device info.')
    
    device_time = device_info['time']
    print(f'Raw Device Time: {device_time}')
    
    # Convert ISO 8601 time to a datetime object
    try:
        device_time_obj = datetime.datetime.fromisoformat(device_time)
    except ValueError as e:
        raise ValueError(f'Error parsing device time: {e}')

    # Check platform for compatibility with date format
    if platform.system() == 'Windows':
        # On Windows, handle leading zeros manually
        formatted_time = device_time_obj.strftime(_date_format)
        formatted_time = formatted_time.replace('/0', '/').replace(', 0', ', ')
    else:
        # On Unix-based systems (Linux/macOS), use %-m and %-d directly
        formatted_time = device_time_obj.strftime(_date_format)

    print(f'Formatted Device Time: {formatted_time}')
    return formatted_time



def time_to_seconds(time_str):
    # Split the time string into hours, minutes, and seconds
    time_components = reversed(time_str.split(':'))  # seconds, mins, hours if any

    total_time_in_seconds = sum([60 ** index * int(item)
                                 for index, item in enumerate(time_components)])

    return total_time_in_seconds


def seconds_to_mm_ss(seconds):
    if seconds < 0:
        raise ValueError("Duration cannot be negative")
    minutes = int(seconds // 60)
    remaining_seconds = int(seconds % 60)
    return f"{minutes}:{remaining_seconds:02}"


def get_current_time_stamp():
    return str(calendar.timegm(time.gmtime()))


def get_date_time_by_zone(
        date_format='%m%d%Y',
        _timezone='US/Pacific',
        time_delta='+0y'):
    """
    Returns current date for specific timezone with provided format.
    :param date_format - the format for the return string.
    :param _timezone - specific timezone string for which date is to be returned.
    :param time_delta - used to calculate future or past date. Provided as +/-time
        unit might be appended as y(year), M(month), d(day), h(hour), m(minute) etc
    """
    utc_date = datetime.datetime.now(tz=pytz.utc)
    delta_unit = time_delta[-1]
    delta_value = int(re.sub('[^0-9]', '', time_delta))
    expected_time_delta = get_time_delta(delta_unit, delta_value)
    if time_delta.startswith('+'):
        utc_date += expected_time_delta
    elif time_delta.startswith('-'):
        utc_date -= expected_time_delta

    timezone_specific_date = utc_date.astimezone(timezone(_timezone))
    return timezone_specific_date.strftime(date_format)


def get_time_delta(delta_unit, delta_value):
    match delta_unit:
        case 'y':
            delta_value = delta_value * 365
            return timedelta(days=delta_value)
        case 'M':
            delta_value = delta_value * 12
            return timedelta(days=delta_value)
        case 'd':
            return timedelta(days=delta_value)
        case 'h':
            return timedelta(hours=delta_value)
        case 'm':
            return timedelta(minutes=delta_value)
    return None


def get_data_from_csv(csv_file_path):
    with open(csv_file_path) as csv_file:
        yield from csv.reader(csv_file)


def find_minimum_time(time_list):
    """
        This method return minimum time from a list of given times
        time format example: 1:09 AM, 12:55 PM etc.
    """
    times = [datetime.datetime.strptime(_time, '%I:%M %p') for _time in time_list]
    return min(times).strftime('%I:%M %p').lstrip('0')


def get_iso_formatted_datetime_str(_days=0):
    # ISO DateTime Format yyyy-MM-dd'T'HH:mm:ss.SSSZ, e.g. "2000-10-31T01:30:00.000-05:00".
    date = datetime.datetime.now() + datetime.timedelta(days=_days)
    date = date.astimezone(datetime.timezone.utc)
    date = date.isoformat(timespec='milliseconds')
    return date.replace('+00:00', 'Z')


def get_current_pst_time():
    # Set the time zone to PST
    tz = pytz.timezone('US/Pacific')
    # Get the current time in PST
    current_time = datetime.datetime.now(tz)
    # Format the time in the 12-hour clock format with AM/PM
    formatted_time = current_time.strftime("%I:%M %p")
    return formatted_time


def get_time_minus_12_hours():
    # Get the current time
    current_time = datetime.datetime.now()

    # Subtract 12 hours from the current time
    time_minus_12_hours = current_time - timedelta(hours=12)

    # Format the time in the desired format (without leading zero in hour)
    formatted_time = time_minus_12_hours.strftime("%I%M%p").lstrip("0").replace("AM", "AM").replace("PM", "PM")

    return formatted_time

def calculate_age(dob: str) -> int:
    """
    Calculate the age in years based on the date of birth and the current date.

    :param dob: Date of Birth in 'YYYY-MM-DD' format
    :return: Age in years
    """
    # Define the date format
    date_format = "%Y-%m-%d"
    
    # Parse the date of birth from string format
    dob_date = datetime.datetime.strptime(dob, date_format)
    
    # Get the current date
    today = datetime.datetime.now()
    
    # Calculate the age
    age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
    
    return age

    # Example usage
    # dob = '2000-01-01'
    # age = calculate_age(dob)
    # print(f"Age: {age} years")


# def get_utc_time_from_current_time_to_11_hours_ahead():
#
