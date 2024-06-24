#1
# def getting_max_over_kernel(arr,k):
#     start_indexes = list(range(0,len(arr)-k+1))
#     end_indexes =list(range(k,len(arr)+1))
#     result = []
#     for i in range(len(start_indexes)):
#         start_index = start_indexes[i]
#         end_index = end_indexes[i]
#         result.append(max(arr[start_index:end_index]))
#     return result
# print(getting_max_over_kernel([3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1],3))
#2
# def word_count(text):
#     result = dict()
#     for i in text:
#         result[f'{i}'] = 0
#     for i in text:
#         result[f"{i}"] = result[f"{i}"] + 1
#     return result
# print(word_count("Happiness"))
#3
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