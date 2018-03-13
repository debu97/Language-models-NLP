import math
path1 = 'C:/Users/Jitendra Arora/OneDrive/ACADEMICS 2016-2019/6th sem/Machine Learning/Autocorrect/CMP462_HW02_Data/CMP462 HW02 Data/data/holbrook-tagged-train.txt'
training_file = open(path1, 'r')                           #storing path and mode
corpus = training_file.read()                               #storing full plain text in para
sentence = corpus.split('\n')                            #storing seperate paragraphs in 'corpus'
counts = dict()
count = []
words = dict()
probability = dict()
total_count = 0
ans = []
sna= []

for line in sentence:
    words = line.split()
    for i in range(len(words)):
        if i < len(words)-1:
            ans.append(words[i]+ words[i + 1])
            sna.append(words[i - 1] + words[i]+ words[i + 1])
print(ans)
print(sna)
for i in range(len(sna)):
    if sna[i] in counts:
        counts[sna[i]] += 1
    else:
        counts[sna[i]] = 1
print(counts[sna[1]])
for i in range(len(ans)):
    if ans[i] in counts:
        counts[ans[i]] += 1
    else:
        counts[ans[i]] = 1
print(counts[ans[8]])

def trigram_prob(phrase):
    ans1 = []
    sna1= []
    for line in phrase:
        words = line.split()
        for i in range(len(words)):
            if i < len(words) - 1:
                ans1.append(words[i] + words[i + 1])
                sna1.append(words[i - 1] + words[i] + words[i + 1])
    return ((sna1,ans1))

x = (trigram_prob(('I have four chocolates and two fruits','wife of the man who was caught','the gift you have them for is fake')))
sna2 = x[0]
ans2 = x[1]
print(ans2)


for i in range(len(sna2)):
    if sna2[i] in counts:
        counts[sna2[i]] += 0
    else:
        counts[sna2[i]] = 0

for i in range(len(ans2)):
    if ans2[i] in counts:
        counts[ans2[i]] += 0
    else:
        counts[ans2[i]] = 0


probability_test_data = 1
probability_test_data_log = 0
for i in range(len(sna2)):
    probability[i] = (counts[sna2[i]] + 1)/(counts[ans2[i]] + 1)
    probability_test_data *= probability[i]
    probability_test_data_log += math.log(probability[i])
print(probability_test_data,probability_test_data_log)
