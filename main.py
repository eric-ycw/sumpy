import parse
import pglobal

sentence_num = int(input("Enter the length of the summary (in sentences) : "))

parse.parse_text()
summary = parse.choose_sentences(pglobal.sentence_list, sentence_num)

print('\nSummary :')
for sentence in summary:
    print(sentence)

print('\nKeywords :')
for word in pglobal.word_list:
    if word.weight > 2:
        print(word.stripped_str, word.weight)