#counts all the characters in the book/text
def counts(texto):
    return len(texto.split())

# adds all the characters in a dictionary as keys, counts the occurence of every character
def characters(texto):
    bukvi = list(texto.lower())
    recnik = {}
    for i in bukvi:
        if i in recnik:
            recnik[i] += 1
        else:
            recnik[i] = 1
    return recnik

# returns a list of sorted dictionaries of the book/text by descending order, only alphanumeric characters
def sorted_list(recnik):
    listata = []
    
    filtered_recnik = {k: v for k, v in recnik.items() if k.isalpha()}
    
    listata = sorted(filtered_recnik.items(), key=lambda x: x[1], reverse=True)
        
    for k, v in listata:
        print(f"{k}: {v}")

    
    return listata