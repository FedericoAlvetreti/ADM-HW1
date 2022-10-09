def mutate_string(string, position, character):
    string=list(string)
    string[int(position)]=character
    string="".join(string)
    return(string)

