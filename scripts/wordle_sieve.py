
def freq_count(word,letter):
    count = 0
    for l in word:
        if l == letter:
            count+=1
    return count

def sieve(current_dict,my_input,outcome):
    possible_dict = current_dict.copy()
    freq_dict = {}
    for i in range(5):
        if outcome[i] == "y" or outcome[i] == "g":
            if my_input[i] not in freq_dict:
                freq_dict[my_input[i]] = 1
            else: 
                freq_dict[my_input[i]] += 1
    freq_dict_ub = {}
    for letter in freq_dict.keys():
        freq_dict_ub[letter] = 5
    for i in range(5):
        if outcome[i] == "_":
            if my_input[i] not in freq_dict:
                freq_dict[my_input[i]] = 0
                freq_dict_ub[my_input[i]] = 0
            else:
                freq_dict_ub[my_input[i]] = freq_dict[my_input[i]]
        
    for letter,freq_l in freq_dict.items():
        freq_u = freq_dict_ub[letter]
        new_dict = {}
        for word in possible_dict.keys():
            if freq_l <= freq_count(word,letter) and freq_count(word,letter) <= freq_u:
                new_dict[word] = True
        possible_dict = new_dict.copy()

    for i in range(5):
        if outcome[i] == "g":
            new_dict = {}
            for word in possible_dict.keys():
                if word[i] == my_input[i]: 
                        new_dict[word] = True
            possible_dict = new_dict.copy()

    for i in range(5):
        if outcome[i] == "y":
            new_dict = {}
            for word in possible_dict.keys():
                if word[i] != my_input[i]: 
                        new_dict[word] = True
            possible_dict = new_dict.copy()

    return possible_dict

def freq_sieve(current_dict,freq_dict):
    possible_dict = current_dict.copy()
    for letter,freq in freq_dict.items():
        new_dict = {}
        for word in possible_dict.keys():
            if freq == freq_count(word,letter):
                new_dict[word] = True
        possible_dict = new_dict.copy()
    return possible_dict

def main():
    allowed_words = open('../data/allowed_words.txt', 'r')
    count = 0
    main_dict = {}
    while True:
        new_word = allowed_words.readline()
        if not new_word:
            break
        main_dict[new_word[0:5]] = True 
        count+=1
    print(f"{count} words stored in dictionary")
    allowed_words.close()

    wordle_dict = main_dict.copy()
    for i in range(6):
        my_input = input("Enter the word : ")
        outcome = input("Enter the outcome : ")
        wordle_dict = sieve(wordle_dict,my_input,outcome)
        if len(wordle_dict) == 1:
            print(f"\nYooo your answer is {list(wordle_dict)[0]}")
            break
        if len(wordle_dict) == 0:
            print("\nyou screwed up somehwere with your inputs!!!")
            break
        print(list(wordle_dict.keys()))
        print(f"{len(wordle_dict)} words left to choose from")
        
        # Developer add-ons
        # explore = input("Do you want to explore? (y/n) : ")
        # if explore == "y":
        #     letters = input("Enter letters you need : ")
        #     freq_dict = {}
        #     for letter in letters:
        #         freq_dict[letter] = freq_count(letters,letter)
        #     explore_dict = freq_sieve(main_dict,freq_dict)        
        #     print(list(explore_dict.keys()))
        #     print(f"{len(explore_dict)} words found")
        
if __name__ == "__main__":
    main()