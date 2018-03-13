import math
path1 = 'C:/Users/Jitendra Arora/OneDrive/ACADEMICS 2016-2019/6th sem/Machine Learning/Autocorrect/CMP462_HW02_Data/CMP462 HW02 Data/data/holbrook-tagged-train.txt'
training_file = open(path1, 'r')                           #storing path and mode
corpus = training_file.read()                               #storing full plain text in para
sentence = corpus.split('\n')                            #storing seperate paragraphs in 'corpus'
# print(len(corpus))
counts = dict()
words = dict()
probability = dict()
total_count = 0
for line in sentence:
    words = line.split()
    # print(words)
    for word in words:
        if word in counts:
            counts[word] += 1
            total_count += 1
        else:
            counts[word] = 1
            total_count += 1
# print(total_count)
# print(probability['night'],probability['in'],probability['one'],probability['bed'])

probability_test_data = 1
probability_test_data_log = 0
test_data = "One night in bed"
test_words = test_data.split()

for word in test_words:
    probability[word] = (counts[word] +1 )/( total_count+1)
    probability_test_data *= probability[word]
    probability_test_data_log += math.log(probability[word])
print(probability_test_data,probability_test_data_log)