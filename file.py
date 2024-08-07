f= open("demo.txt", "r")    # it is use to read file.
data = f.read()
print(data)
f.close

f= open("demo.txt","w")     # it is use to make new file and write in it
data = f.write("heloo")
print(data)
f.close

f= open("demo.txt", "a")    # it is use to write at the end of the file.
data = f.write("\nMy self Ahad abbasi")
print(data)
f.close

f= open("demo.txt","r+")      # it is use to read and write at the start of the file. it over-write the things.
data = f.write("I'm")
print(data)
f.close

with open("demo.txt","r") as f:      #Another syntex ... no need to close
    data = f.read()


#import os     to delet a file
#os.remove("symple.txt")    

#Prectic question.

with open("prectic.txt","w") as f:
    data = f.write("Hi everyone.\nMy self Ahad Abbasi.\n I'm from Pakistan.\n I'm learning python on Apna collage.")
    


with open("prectic.txt","r")as f:
    data = f.read()
new = data.replace("Ahad","Abdul Ahad")     #To replace some words 

with open ("prectic.txt","w") as f:
    data = f.write(new)


#write a function to find Abbasi word exist in it.

def find_word():
    with open ("prectic.txt","r")as f:
        data = f.read()
        if (data.find("Abbasi")!= -1):
            print("founded")
        else:
            print("Not founded") 
find_word()               
