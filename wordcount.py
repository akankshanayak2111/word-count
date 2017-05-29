# put your code here.


def word_count(file_name):
    file_content = open(file_name)
    word_count_dict = {}
    for line in file_content:
        line = line.rstrip()
        line_list = line.split(" ")
        for word in line_list:
            word_count_dict[word] = word_count_dict.get(word, 0) + 1
    #return word_count_dict
    for word, count in word_count_dict.iteritems():
        print word, count


# def word_count_bigfile(file_name):
#     file_content = open(file_name)
#     word_count = {}
#     for line in file_content:
#         line = line.rstrip()
#         line_list = line.split(" ")
#         for word in line_list:
#             if word in word_count:
#                 word_count[word] += 1
#             else:
#                 word_count[word] = 1
#     return word_count


word_count("twain.txt")



# print word_count("twain.txt")
# print word_count_bigfile("twain.txt")