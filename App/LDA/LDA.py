import stop_words



def get_Stop_Words():
    en_stop_words    = stop_words.get_stop_words('english')
    malay_stop_words =  stop_words.get_stop_words("indonesian")

    STOP_WORDS = set(en_stop_words)
    STOP_WORDS.update(malay_stop_words)


    with open("./App/LDA/stopwords.txt", "r") as f:
        for l in f.readlines():
            STOP_WORDS.update(l.strip())


    len(STOP_WORDS)