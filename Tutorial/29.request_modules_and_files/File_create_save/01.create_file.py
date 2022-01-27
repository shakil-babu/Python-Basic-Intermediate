fp = open("text.txt", "w")
fp.write("hi, this is shakil babu a passionate learner.")

# adding text
fp.write("A passionate learner.")
fp.close()


# Overwrite
fl = open("text.txt", "w")
fl.write("This is overwrite ")

print(type(fl))
