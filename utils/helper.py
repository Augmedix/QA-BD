"""
Contains generic helper methods independent of any applications i.e.: generating random string of
specified length, converting datetime to specific Timezone, calculating past/future time relative
to current time etc.
"""
import calendar
import csv
import datetime as date_time
import os
import random
import re
import string
import time
import urllib.parse
from datetime import datetime, timedelta

import pytz
from pytz import timezone


def wait_for_next_minute(min_second=40):
    # Get the current time
    now = datetime.now()

    if min_second <= now.second <= 59:
        seconds_until_next_minute = (59 - now.second) + 2

        # Wait until the next minute starts
        time.sleep(seconds_until_next_minute)

        print(f'waiting an additional {seconds_until_next_minute} seconds until the next minute starts')


def generate_random_alphanumeric_string(string_lenght=10):
    """
    Generates random alphanumeric string for specified length.
    :param string_lenght: length of the expected random string. Default length is 10.
    :return: alphanumeric string of specified length.
    """
    alpha_numeric_string = string.ascii_letters + string.digits
    return ''.join(random.choice(alpha_numeric_string)
                   for _ in range(string_lenght))


def get_current_time_stamp():
    return str(calendar.timegm(time.gmtime()))


def get_date_time_by_zone(
        date_format='%m%d%Y',
        _timezone='US/Pacific',
        time_delta='+0y'):
    """
    Returns current date for specific timezone with provided format
    :param date_format - the format for the return string
    :param _timezone - specific timezone string for which date is to be returned
    :param time_delta - used to calculate future or past date. Provided as +/-time
        unit might be appended as y(year), M(month), d(day), h(hour), m(minute) etc
    """
    utc_date = datetime.now(tz=pytz.utc)
    delta_unit = time_delta[-1]
    delta_value = int(re.sub('[^0-9]', '', time_delta))
    expected_time_delta = get_time_delta(delta_unit, delta_value)
    if time_delta.startswith('+'):
        utc_date += expected_time_delta
    elif time_delta.startswith('-'):
        utc_date -= expected_time_delta

    timezone_specific_date = utc_date.astimezone(timezone(_timezone))
    return timezone_specific_date.strftime(date_format)


def get_time_difference(start_time, end_time):
    """
    Get the time difference beteween end_time & start_time
    :param start_time start time in string format
    :param end_time end time in string format
    """
    _start_time = datetime.strptime(start_time, '%I:%M %p')
    _end_time = datetime.strptime(end_time, '%I:%M %p')

    time_difference = _end_time - _start_time

    hour = f'{divmod(time_difference.seconds, 3600)[0]}h'
    minute = f'{time_difference.min}m'
    return hour, minute


def get_current_date_hour_minute_in_pst():
    pst = pytz.timezone('America/Los_Angeles')
    date = datetime.now(pst)

    _time = date.strftime('%D:%H:%M')
    return _time


def get_time_in_ordinal_format(date_string=None):
    splitted_date = re.split(r'-|\\|/|\.', date_string)
    formatted_date = datetime.strptime('-'.join(splitted_date), '%Y-%m-%d')
    month_name_string = formatted_date.strftime('%b')
    return f'{month_name_string} {get_ordinal_value_of(splitted_date[2])} {splitted_date[0]}'


def get_ordinal_value_of(value=0):
    value = int(value)
    if 4 <= value <= 20 or 24 <= value <= 30:
        suffix = 'th'
    else:
        suffix = ['st', 'nd', 'rd'][value % 10 - 1]

    return f'{value}{suffix}'


def find_minimum_time(time_list):
    """
        This method return minimum time from a list of given times
        time format example: 1:09 AM, 12:55 PM etc.
    """
    times = [datetime.strptime(_time, '%I:%M %p') for _time in time_list]
    return min(times).strftime('%I:%M %p').lstrip('0')


def add_minutes(time_in_12h, minutes_to_add):
    """
        this method add specific minutes to any 12-hour format time, such as
        add 5 minutes to 2:05 PM = 2:10 PM.
        time format example: 1:09 AM, 12:55 PM etc.
    """
    time_obj = datetime.strptime(time_in_12h, '%I:%M %p')
    time_obj += timedelta(minutes=minutes_to_add)
    return time_obj.strftime('%I:%M %p').lstrip('0')


def add_hours_to_date(given_date_time, hours_to_add):
    """
        Add specific hours to any given date time.
        date format example: 2023-03-09 07:05 AM
    """
    date = datetime.strptime(given_date_time, '%Y-%m-%d %I:%M %p')
    new_date = date + timedelta(hours=hours_to_add)
    return datetime.strftime(new_date, '%Y-%m-%d %I:%M %p')


def add_days_to_date(date_str, days_to_add):
    """
        Add specific number of days to a given date string
        date format example: 2023-03-05 ('YYYY-MM-DD')
    """
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    new_date_obj = date_obj + timedelta(days=days_to_add)
    return new_date_obj.strftime('%Y-%m-%d')


def increase_day_from_today(days_to_increase=1):
    """
        Add specific number of days to current date.
        date format example: 2023-03-07 ('YYYY-MM-DD')
    """
    current_date = date_time.date.today()
    increased_day = timedelta(days=days_to_increase)
    future_date = current_date + increased_day
    return str(future_date)


def capitalize_only_first_character(text):
    """
    Capitalizes only the first character of the provided text
    :param text: str: The text to capitalize the first character of
    :return: str: The text with only the first character capitalized
    """
    # Slice the text to obtain the first character and capitalize it
    first_letter = text[0].upper()

    # Slice the text to obtain the rest of the characters
    rest_of_text = text[1:]

    # Concatenate the capitalized first character with the rest of the text
    formatted_text = first_letter + rest_of_text

    return formatted_text


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


def encode_value_for_url(value):
    """
    In URLs, spaces are not allowed. To include a space or any other special character in a URL,
    it needs to be encoded using percent-encoding. This function will replace any character
    that is not safe to include in a URL with its corresponding percent-encoded value
    Use urllib.parse.quote to encode the value.
    """
    encoded_value = urllib.parse.quote(value)
    return encoded_value


def get_data_from_csv(csv_file_path):
    with open(csv_file_path) as csv_file:
        yield from csv.reader(csv_file)


def get_random_file_name(folder_path, file_type):
    """
    Args:
        folder_path: From where the random file will be taken
        file_type: .mp3, .mp4 etc.
    Returns:
        file name with extension
    """
    files = [file for file in os.listdir(folder_path) if file.endswith(file_type)]
    random_file = random.choice(files)
    return random_file


def generate_sublist(input_list, sublist_length):
    if sublist_length > len(input_list):
        print("Sublist length exceeds the length of the input list.")
        return None
    sublist = random.sample(input_list, sublist_length)
    return sublist


def generate_sublist_with_same_order(original_list, sublist_length):
    """
        This method encapsulates the process of generating a random sample
        while preserving the order of the original list
        :param original_list - from which generate a random sample
        :param sublist_length - size of the random sample list
    """
    if sublist_length > len(original_list):
        print("Sublist length exceeds the length of the main list.")
        return None
    shuffled_list = original_list.copy()
    random.shuffle(shuffled_list)
    random_sample = shuffled_list[:sublist_length]
    random_sample.sort(key=original_list.index)
    return random_sample


def order_list_item(main_list, sublist):
    """
        This method essentially takes two lists as input and returns a new list
        with the elements from the second list arranged in the order specified by the first list
        :param main_list - The reference list based on which the order of elements in sublist will be
        :param sublist - The list whose order needs to be modified according to the order of
    """
    # Create a dictionary to store the index of each element in the first list
    index_dict = {element: index for index, element in enumerate(main_list)}
    # Use the index information to sort the second list
    ordered_list = sorted(sublist, key=lambda x: index_dict[x])
    return ordered_list

def normalize_time(time_str):
    return time_str.lstrip('0')