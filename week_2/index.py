
def word_count_file(file_path):
    content = open(file_path,"r")
    sentences = content.read().split("\n")
    result = dict()
    for i in sentences:
        words = i.split(" ")
        for i in words:
            try:
                result[f'{i}'] +=1
            except:
                result[f'{i}'] = 1
    return result
print(word_count_file("week_2/P1_data.txt"))