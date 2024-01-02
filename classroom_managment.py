classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]

def index_student(name):
    i=0
    for s in classroom:
        if s['name']==name:
            return i
        i+=1


def add_student(name, email=None):
    """Add a new student to the classroom
    with the following keys:
    'name': the given name
    'email': if email is given use it otherwise use <name>@example.com
             in lowercase, you can use the `s.lower()` method
    'grade': initialize with empty list
    """
    if email==None:
        # email=f"{name.lower()}@example.com"
        classroom.append({'name':name,'email':f"{name.lower()}@example.com",'grades':[]})
    else:
         classroom.append({'name':name,'email':email,'grades':[]})


def delete_student(name):
    """Delete a student from the classroom"""
    i=index_student(name)
    classroom.remove(classroom[i])


def set_email(name, email):
    """Sets the email of the student"""
    i=index_student(name)
    classroom[i]['email']=email
    




def add_grade(name, profession, grade):
    """Adds a new grade to the student grades"""
    i=index_student(name)
    classroom[i]['grades'].append((profession,grade))


def avg_grade(name, profession):
    """Returns the average of grades of the student
    in the specified profession
    """
    i=index_student(name)
    sum=0
    count=0
    for item in classroom[i]['grades']:
        if item[0]==profession:
            count+=1
            sum+=item[1]
    return sum/count


def get_professions(name):
    """Returns a list of unique professions that student has grades in"""
    i=index_student(name)
    l=[]
    for g in classroom[i]['grades']:
        if l.count(g[0])==0:
            l.append(g[0])
    return l



# add_student('Joe')
# add_student('Yoram','yor@walla.com')
# delete_student('Charlie')
# set_email('Bob','bob@gmail.com')
# add_grade('Bob','physics',80)
# for student in classroom:
#     for k,v in student.items():
#         print (f"{k}:{v}")
#     print()
# print(avg_grade('Alice','math'))
# l=get_professions('Charlie')
# for i in l:
#     print(i)