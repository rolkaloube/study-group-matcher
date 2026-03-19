"""
Generate a csv file containing students, their class choices, and their
appointments. Creates students.csv
"""

import random
import functools

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
]

students = [
    "Alice",
    "Bob",
    "Carol",
    "Dave",
    "Ellie",
    "Fred",
    "Georgia",
    "Henry",
    "Isabella",
    "Jacob",
    "Linda",
    "Mike",
    "Nancy",
    "Oscar",
    "Phoebe",
    "Quentin",
    "Rachel",
    "Sam",
    "Tina",
    "Victor",  # couldn't come up with a name starting with U, lol
]

classes = ["CISC-160", "CISC-301", "MATH-220"]

output = open("students.csv", "w")
output.write('"student","classes",')
output.write(",".join(f'"{d}"' for d in weekdays))
output.write("\n")


Appointment = tuple[int, int]


def clamp_normal(min: int, max: int, mu=0.0, sigma=1.0):
    """
    Clamp the normal distribution to a minimum and maxiumum. Repeated trials
    are used over min() and max() to avoid bunching at the endpoints.
    """
    while True:
        rand = int(random.normalvariate(mu, sigma))
        if min <= rand <= max:
            return rand


# time to start placing appointments: 0-4 over a uniform distribution
start_time = functools.partial(random.randint, 0, 4)

# appointment length: 60-180 minutes from a normal distribution
appointment_length = functools.partial(clamp_normal, 2, 6, 3.25, 2)


def format_appointment(appointment: Appointment):
    start, length = appointment
    hour = 9 + (start // 2)
    minutes = "30" if start % 2 == 1 else "00"
    return f"{hour}:{minutes}+{30*length}"


def generate_day():
    """
    Generate a day's worth of appointments.
    """

    appointments: list[Appointment] = []

    while True:
        now = start_time()
        # the day is split into 18 30-minute blocks, from 9 AM to 6 PM.
        while now < 18:
            # for any given 30-minute block, there is a 40% chance it's taken
            if random.random() < 0.33:
                # ... by something from 30 to 120 minutes long.
                length = appointment_length()
                # clamp the length for stuff at the end of the day. nobody
                # wants to miss dinner.
                if now + length > 18:
                    length = 18 - now
                appointments.append((now, length))
                # advance time...
                now += length
            # plus union-mandated 30 minute break.
            now += 1

        # keep trying until we get at least 2 appointments
        if len(appointments) < 2:
            appointments.clear()
        else:
            return appointments


for student in students:
    output.write(f'"{student}",')

    n_classes = random.randint(1, len(classes))
    interests = set(random.choices(classes, k=n_classes))
    output.write('"')
    output.write(";".join(interests))
    output.write('",')

    # random schedule every day
    for weekday in weekdays:
        appointments = generate_day()

        output.write('"')
        output.write(";".join(map(format_appointment, appointments)))
        output.write('",')

    output.write("\n")

output.close()
