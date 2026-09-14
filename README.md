## **Prompt**
Match and place students into study groups based on course and availability overlap.

## **Problem**
If you're having trouble with a course, it's nice to be able to meet up with your fellow students and compare notes. However, scheduling can feel like trying to solve the halting problem! Thankfully, it's possible to just churn through every possible meeting time and pick the best one. But who wants to do that? That's what we've got computers for. 

## **MVP**
A study group matching tool that allows students to enter their name and select a course for which they want to form a study group. Based on course enrollment data and participant availability, the system automatically generates optimal study groups by maximizing overlapping availability among students. Users can also specify the desired maximum size of the group to tailor the matching process.

Key MVP Components:
* User inputs: course selection and desired group size
* Data inputs: student course enrollments and availability
* Output: optimized study groups and schedules

## **Beyond MVP**
* Take input from a Google calendar (or other groupware product) instead of preformatted CSV
* Prefer keeping consistent groups of students together
* Allow students to "block" other students (refuse to participate in their groups)
* Develop an API or CLI that takes dynamic inputs and returns results for different services. Examples:
  * API endpoint: `GET /study-group?course=CISC-210&size=4`
  * CLI command: `study-group --course CISC-210 --size 4`

## **Available Resources**
* Example students and their freetime: [students.csv](prompt_resources/students.csv)
* Code used to generate the above: [gen-students.py](prompt_resources/gen-students.py)
* Generate simple visual representations of appointments: [graph-students.py](prompt_resources/graph-students.py)
graph-students.py contains code to parse students.csv. Take a look at that and you might save yourself some time!
