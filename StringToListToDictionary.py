# This is my python code
def mydict(text):
    print([text])
    my_list = text.split()
    my_dist = {}
    i=0
    for letter in my_list:
        for char1 in letter:
            print(char1,i)
            my_dist[i]=char1
            print(my_dist)
            i=i+1
