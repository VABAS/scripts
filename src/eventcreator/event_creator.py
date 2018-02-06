#!/usr/bin/python3
import sys
import datetime

def event_creator (file_name, name, time, duration):
    vevent_class = "CONFIDENTIAL"
    now = datetime.datetime.now()
    f = open(file_name, "r")
    filu = f.read().splitlines()
    f.close()
    out_f = open(file_name + ".ics", "w")
    out_f.write("BEGIN:VCALENDAR\r\nVERSION:2.0\r\nPRODID:Event Creator\r\n")
    for line in filu:
        times = line.split(" ")
        date = times[0].split(".")
        # Assuming current year if not provided.
        if len(date[2]) == 0:
            date[2] = str(now.year)
        date = date[2] + ("0" * (2 - len(date[1]))) + date[1] + ("0" * (2 - len(date[0]))) + date[0]
        now_stamp = "{:04d}{:02d}{:02d}T{:02d}{:02d}00".format(now.year, now.month, now.day, now.hour, now.minute)
        vevent = "BEGIN:VEVENT\r\n" \
               + "UID:" + date + time + duration + "\r\n" \
               + "DTSTAMP:" + now_stamp + "\r\n" \
               + "DTSTART:" + date + "T" + time + "00\r\n" \
               + "DURATION:PT" + duration + "H0M0S\r\n" \
               + "SUMMARY:" + name + "\r\n" \
               + "STATUS:CONFIRMED\r\n" \
               + "CLASS:" + vevent_class + "\r\n" \
               + "END:VEVENT\r\n";
        out_f.write(vevent)

    out_f.write("END:VCALENDAR\r\n")
    out_f.close()

if __name__ == "__main__":
    if len(sys.argv) <= 4:
        print("Not enough arguments!")
        print("Usage: " + sys.argv[0] + " file event-name event-start-time event-duration")
        print(" - File contains dates separated with new-line formatted dd.mm.yyyyi or dd.mm.")
        print(" - Event start-time is formatted hhmm")
        print(" - Event-duration is in full hours")
        sys.exit()
    event_creator(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

