lines = [
    "I am shakil babu",
    "I am torikus sadik",
    "I am fahim morshed"
]

with open("test.txt", "w") as f:
    for line in lines:
        f.write(line+"\n")
