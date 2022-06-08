"""A command line function to normalize a CSV file according to given specs."""
from typing import List
import click
import dateutil.parser
import pytz

@click.command()
@click.argument('input', type=click.Path(exists=True))
@click.argument('output', type=click.File('w'))
def normalizer(input, output):
    with open(input, encoding='utf-8') as file:
        first_line: bool = True
        pacific_time = pytz.timezone('US/Pacific')
        eastern_time = pytz.timezone('US/Eastern')
        for line in file:
            # unicode check and replacement - Python appears to be doing this automatically
            # copy the schema line
            if first_line:
                output.write(line)
                first_line = False
            else:
                # parse the line
                entries: List = []
                if '"' in line:
                    # if the address and/or notes is in quotes
                    mid_entries: List = line.split('"')
                    for entry in mid_entries:
                        if entry[-1] == ',' or entry[0] == ',':
                            entries = entries + entry.strip(',').split(',')
                        else:
                            entries.append('"'+ str(entry) + '"')
                else:
                    entries = line.split(',')
                # timestamp conversion
                date_parsed = dateutil.parser.parse(entries[0])
                date_zoned = pacific_time.localize(date_parsed)
                output.write(date_zoned.astimezone(eastern_time).isoformat() + ',')
                # address
                output.write(entries[1] + ',')
                # zip
                for index in range(len(str(entries[2])), 5):
                    output.write("0")
                output.write(str(entries[2]) + ',')
                # fullname
                output.write(entries[3].upper() + ',')
                # foo, bar, and total
                duration_time = 0.0
                for time in (entries[4], entries[5]):
                    try:
                        split_time = time.split(':')
                        sec = int(split_time[0])*3600 + int(split_time[1])*60 + float(split_time[2])
                    except:
                        sec = 0.0
                    output.write(str(sec) + ',')
                    duration_time = duration_time + sec
                output.write(str(duration_time) + ',')
                # notes (may be empty)
                if entries[7]:
                    output.write(str(entries[7]))
                    # this is weird, but it seems if an entry ends in quotes it doesn't newline
                    if entries[7][-1] == '"':
                        output.write('\n')

if __name__ == '__main__':
    normalizer()

# unicode check and replcament > I can't seem to replicate this? curious
# maybe python does it automatically?
# data validation -- buffer? then write?
# - date
# - times counts 
# too many decimals on total duration

# take in the text input
# parse on a linebreak
# parse on , except in "" (???? how!)
# timestamp PST -> EST, -> RFC3339
# address -> address w/ unicode validation
# zip -> 5 digits, leading 0s
# fullname -> to uppercase (unicode included)
# fooduration HH:MM:SS.MS -> SS
# barduration HH:MM:SS.MS -> SS
# totalduration garbage -> foo+bar
# notes -> notes w/ unicode replacement
# output new thing