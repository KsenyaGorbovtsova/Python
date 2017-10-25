ivan={
    "name": "ivan",
    "age":34,
    "children":[{
        "name":"vasja",
        "age":12,
    },{
        "name":"petja",
        "age":10,
    }

    ],
}

darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    }, {
        "name": "pavel",
        "age": 15,
    }

    ],
}
emps=[ivan, darja]
for i in range(len(emps)):
    for j in range(len(emps[i]['children'])):
        if (emps[i]['children'][j]['age'])>=18:
             print emps[i]
             break