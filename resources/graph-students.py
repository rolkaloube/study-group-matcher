"""
Generate visual graphs of each weekday from students.csv. Creates students-*.pbm

PBM is a text-based image format that can be viewed in a text editor, or in
most image viewers. If you've got imagemagick installed you can convert it to
a png easily: magick students-blah.pbm students-blah.png
"""

import collections
import csv
import io

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
]


Appointment = collections.namedtuple("Appointment", ["start", "length"])


def parse_appointment(a: str):
    start, length = a.split("+")
    h, m = map(int, start.split(":"))
    # 0 - 17 for 30 minute blocks
    start = (2 * (h - 9)) + (1 if m == 30 else 0)
    return Appointment(start, int(length) // 30)


with open("students.csv", "r") as fp:
    students = list(csv.DictReader(fp))

block_width = 4
row_height = block_width
padding = row_height // 2

n_rows = len(students)
px_width = 20 * block_width
px_height = n_rows * row_height + (n_rows + 1) * padding


def pad(output):
    for _ in range(padding):
        output.write("0" * px_width)
        output.write("\n")


def draw_day(weekday: str):
    output = open(f"students-{weekday}.pbm", "w")
    output.write("P1\n")
    output.write(f"{px_width} {px_height}\n")

    for student in students:
        pad(output)
        row = io.StringIO()
        i = -1
        for a in map(parse_appointment, student[weekday].split(";")):
            diff = a.start - i
            if diff > 0:
                row.write("0" * block_width * diff)
            row.write("1" * block_width * a.length)
            i = a.start + a.length

        row.write("0" * (px_width - row.tell()))
        row.write("\n")

        for _ in range(row_height):
            output.write(row.getvalue())

    pad(output)
    output.close()


for day in weekdays:
    draw_day(day)
