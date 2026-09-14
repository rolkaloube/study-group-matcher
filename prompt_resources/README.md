# Sample data
[students.csv](./students.csv) contains an example list of students, their course load, and their availability. The first row contains the column names. If you'd like more examples, you can rename the example file and run [gen-students.py](./gen-students.py) to generate a new list.

## CSV structure

- "student"  is the student's name.
- "classes" are the classes the student would be interested in forming a study group for. The class names are separated with semicolons.

The remaining columns represent appointments that student has on any given day. What the student is doing during these appointments is not specified; what's important is that they cannot attend a study group during any of them.

## Appointment format

Each day has a list of appointments separated by semicolons. An appointment is a start time in 24 hour notation and a length in minutes separated by a plus sign. For instance:

- `11:30+90` is an appointment starting at 11:30 AM and lasting 90 minutes until 1:00 PM.
- `14:00+30` is an appointment starting at 2:00 PM and lasting 30 minutes until 2:30 PM.

You can find sample code for parsing appointments from the sample data in [graph-students.py](./graph-students.py). This script generates simple visual representations of the sample data so you can look for potential study group slots that your app might be missing.

The example generator operates in increments of 30 minutes for simplicity's sake. Make sure you can handle appointments starting and ending at odd times so you can handle real data!