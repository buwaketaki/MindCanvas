import string

selected_chr = ''

def anag_freq_alpha_selector(anaglinks, ignore_list):

    global selected_chr
    
    def freq_alpha_out(Input, mode = 0):

        count_dict = {alpha: 0 for alpha in string.ascii_uppercase}
        
        for anaglink in Input:
            for wrd in anaglink:
                for alpha in wrd:
                    count_dict[alpha.upper()] += 1

        result = sorted(count_dict.items(), reverse = bool(mode), key = lambda tup : tup[1])

        if(mode == 0):
            temp = list()
            for tup in result:
                if (tup[1] != 0):
                    temp.append(tup)
            result = temp

        return [tup[0] for tup in result]

    Ans_alpha = freq_alpha_out(anaglinks)
    nonAns_alpha = freq_alpha_out(ignore_list, 1)

    selected = ('', 51)
    for i in range(len(Ans_alpha)):
        score = i + nonAns_alpha.index(Ans_alpha[i])
        if(score < selected[1]):
            selected = (Ans_alpha[i], score)

    selected_chr = selected[0]

    print(selected_chr)

    return selected[0]

def run(anaglinks):

    global selected_chr
    
    for i in range(len(anaglinks)):
        if(selected_chr not in anaglinks[i][0].upper() and selected_chr != ''): 
            anaglinks[i].append(-1)

    
