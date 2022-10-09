
def wrap(string, max_width):
    for i in range(0,len(string)//(max_width)):
        j=i*max_width
        print(string[j:j+max_width])
    return(string[j+max_width:])

