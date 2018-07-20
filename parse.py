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
    return None


def store_word(string, blacklist, w_list):
    if Word.strip_word(string) in blacklist:
        return
    pos = word_pos(string, w_list)
    if pos is not None:
        w_list[pos].weight += 1
    else:
        w_list.append(Word(string))


def strip_sentence(s_list):
    # Remove whitespaces
    for index, s in enumerate(s_list):
        s_list[index] = s.strip()
    # Remove extra full stop for final sentence
    s_list[-1] = s_list[-1][:-1]
    return s_list


def parse_text():
    blacklist = get_blacklist()
    with open('data.txt', 'r') as f:
        # Store sentence
        full_text = f.read().replace('\n', ' ')
        pglobal.sentence_list = strip_sentence([s + '.' for s in full_text.split('. ') if s])
        # Store word
        word = full_text.split()
        for w in word:
            store_word(w, blacklist, pglobal.word_list)

    f.close()


def calculate_sentence_score(s, w_list):
    score = 0
    words = s.split()
    for w in words:
        if w in w_list:
            word_weight = w_list[word_pos(w, w_list)].weight
            if word_weight > 1:
                score += word_weight
    return score


def choose_sentences(s_list, num):
    summary_score = [-1] * num
    summary = [''] * num
    for sentence in s_list:
        for index, s in enumerate(summary_score):
            sentence_score = calculate_sentence_score(sentence, pglobal.word_list)
            if sentence_score > s:
                # Not the last sentence in summary
                if index < num - 1:
                    summary_score[index + 1] = s
                    summary[index + 1] = summary[index]
                summary_score[index] = sentence_score
                summary[index] = sentence
                break

    return summary

