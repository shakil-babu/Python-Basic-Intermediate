# dictionaries declaration
details = {
    "person1" : {
        "name" : "Torikus Sadik Raihan",
        "age" : 23
    },
    "person2" : {
        "name" : "Fahim Morshed",
        "age" : 22
    },
    "person3" : {
        "name" : "Shakil Babu",
        "age" : 21
    }
}


# dictionaries 
personDetails = {
    "det": [
        {
            "name" : "shakil"
        },
        {
            "name" : "torikus"
        },
        {
            "name" : "fahim"
        }
    ]
}


for person in personDetails["det"]:
    print(person["name"])