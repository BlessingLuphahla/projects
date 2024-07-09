from pathlib import Path
import re
import datetime
from collections import Counter


def fix(iterable: list):
    iterable = [[_, datetime.time.fromisoformat(time)] for _, time in iterable]
    return iterable


# TODO setting up time conditioning
def time_condition(time: datetime.time, minimum_time=0, maximum_time=24):
    if minimum_time <= time.hour <= maximum_time:
        return True

    return False


def complicated_string():
    return ' ' * 3 + '`' * 3 + ' ' * 3 + '|' * 1 + ' ' * 6


__ultimate_date_match__ = r"""  '(\d{,4}.+:\d{2}\s)'   """

__date_sample__ = """    2024/03/10, 21:27  """  # TODO put date sample here


def main():  # TODO change pattern matching
    date_match = re.compile(r'\d{4}/\d{2}/\d{2},\s\d{2}:\d{2}', flags=re.IGNORECASE | re.MULTILINE)

    location = Path(r'')  # TODO LOCATION
    dates_and_time = []
    with open(location, encoding='charmap') as file:
        reader = file.readlines()
        for line in reader:
            dates_and_time.append(date_match.findall(line))

    dates_and_time = [''.join(date).replace('/', '-').split(', ') for date in dates_and_time if
                      date]  # [date,time]
    dates_and_time = fix(dates_and_time)

    number_of_times = 0
    list_of_matched_times = set()
    list_of_dates = []
    time_location = location.parent / 'TIME STAMPS.txt'
    with open(time_location, 'w') as file:
        for i in range(24 + 1):
            for date, time in dates_and_time:
                if time_condition(time, minimum_time=i, maximum_time=i):
                    list_of_matched_times.add((i, str(complicated_string()), str(time)))
                    number_of_times += 1

        for date, _ in dates_and_time:
            list_of_dates.append(date)

        date_counter = Counter(list_of_dates)
        date_counter = sorted(list(date_counter.items()), key=lambda x: x[1], reverse=True)

        list_of_matched_times = sorted(list(list_of_matched_times), key=lambda x: x[0])
        list_of_time_approximations = []
        for num, *_ in list_of_matched_times:
            list_of_time_approximations.append(num)

        time_counter = Counter(list_of_time_approximations)
        time_counter = sorted(list(time_counter.items()), key=lambda x: x[1], reverse=True)

        # format string

        format_string: str = '{0:^40}| {1:^40}'

        print(file=file)
        print('statistics'.upper().center(90, '_'), file=file)
        print(file=file)
        print('_' * 90, file=file)
        print(format_string.format('time'.upper(), 'count'.upper()), file=file)
        print('_' * 90, file=file)

        for time, count in time_counter:
            time = str(time)
            if len(time) < 2:
                time = '0' + time
            print(format_string.format(time + ':00+', count), file=file)
            print('_' * 90, file=file)

        print(format_string.format('date'.upper(), 'number of messages'.upper()), file=file)
        print('_' * 90, file=file)
        for date, count in date_counter:
            print(format_string.format(str(date), count), file=file)
            print('_' * 90, file=file)

        print(file=file)
        print('complete breakdown'.upper().center(90, '_'), file=file)
        print(file=file)

        for time_number, comp_str, actual_time in list_of_matched_times:
            time_number = str(time_number)
            if len(time_number) < 2:
                time_number = '0' + time_number
            print(str(complicated_string()) + ' ', time_number + ':00:00+', comp_str, actual_time,
                  sep=' ', file=file)

    print('everything is finished'.upper())


if __name__ == '__main__':
    main()
