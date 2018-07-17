from word import Word
import pglobal


def get_blacklist():
    with open('blacklist.txt') as f:
        return [line.rstrip('\n') for line in f]
    f.close()


def word_pos(string, w_list):
    for index, word in enumerate(w_list):
        if word.stripped_str == Word.strip_word(string):
            return index
    return -1


def store_word(string, blacklist, w_list):
    invalid = False
    for i in blacklist:
        if Word.strip_word(string) == i:
            invalid = True
            break
    if not invalid:
        pos = word_pos(string, w_list)
        if pos >= 0:
            w_list[pos].weight += 1
        else:
            w_list.append(Word(string))


def parse_text():
    blacklist = get_blacklist()
    with open('data.txt', 'r', encoding='utf8') as f:
        # Store sentence
        full_text = f.read().replace('\n', ' ')
        pglobal.sentence_list = [s + '.' for s in full_text.split('.') if s]
        # Store word
        word = full_text.split()
        for w in word:
            store_word(w, blacklist, pglobal.word_list)

    f.close()


def calculate_sentence_score(s, w_list):
    score = 0
    words = s.split()
    for w in words:
        word_obj_pos = word_pos(w, w_list)
        if word_obj_pos >= 0:
            score += w_list[word_obj_pos].weight
    return score


parse_text()
for sentence in pglobal.sentence_list:
    calculate_sentence_score(sentence, pglobal.word_list)
