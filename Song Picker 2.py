## Song picker! Asks user how they're feeling, what they want, and then chooses
## the perfect song for them

# i'm feeling: [joyful energetic tired weepy anxious frustrated powerful]
# and i want to: [be inspired wallow rock out dance focus]

## Ask user how they're feeling
def howyafeeling():
    user_feeling = input("How are you feeling? \n\t A: Joyful \n\t B: Energetic \n\t C: Tired \n\t D: Weepy \n\t E: Anxious \n\t F: Frustrated \n\t G: Powerful \n Type A, B, C, D, E, F, or G: ")
    good_answers = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g"]
    while user_feeling not in good_answers:
        user_feeling = input("\n~*~*Was that a typo? Try again! How are you feeling? \n\t A: Joyful \n\t B: Energetic \n\t C: Tired \n\t D: Weepy \n\t E: Anxious \n\t F: Frustrated \n\t G: Powerful \n Please type ONLY A, B, C, D, E, F, or G: ")
    return user_feeling
        
## Ask user what they want to do        
def whatchawant():
    user_wants = input("\nThanks for sharing. And what do you want to do? \n\t H: Be inspired \n\t I: Wallow \n\t J: Rock out \n\t K: Dance \n\t L: Focus \n\t M: Rage \n\t N: Harmonize \n Type H, I, J, K, L, M, or N: ")
    good_answers_2 = ["H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n"]
    while user_wants not in good_answers_2:
        user_wants = input("\n~*~*Was that a typo? Try again! What do you want to do? \n\t H: Be inspired \n\t I: Wallow \n\t J: Rock out \n\t K: Dance \n\t L: Focus \n\t M: Rage \n\t N: Harmonize \n Type H, I, J, K, L, M, or N: ")
    return user_wants

## define song lists (each list appears in order of "whatchawant" answers -- be inspired, then wallow, etc)
joy_songs = ["*Show Yourself* by Ayla Nereo","*Home* by Edward Sharpe","*The Sound of Sunshine* by Michael Franti","*Happy* by Pharrell Williams","*Medicine* by Rising Appalachia","*Train Song* by Feist","*One Voice* by The Wailin Jennys"]
energ_songs = ["*Sing to the Mountain* by Elephant Revival","*Breathe It In* by Beautiful Chorus","*The Sound of Sunshine* by Michael Franti","*Happy* by Pharrell Williams","*First Snow* by Emancipator","*Respect* by Aretha Franklin","*Galileo* by the Indigo Girls"]
tired_songs = ["*Show Yourself* by Ayla Nereo","*Hum* by Ayla Nereo","*It Aint Me Babe* by Bob Dylan","*Downtown* by Rising Appalachia","*Case of You* by Joni Mitchell","*Slowly* by Max Sedgley","*One Voice* by The Wailin Jennys"]
weepy_songs = ["*Show Yourself* by Ayla Nereo","*Burn* by Ray LaMontagne","*Jolene* by Rhonda Vincent","*Slowly* by Max Sedgley","*Blue* by Joni Mitchell","*Let Her Go* by Passenger","*Nobody's Fault* by Rising Appalachia"]
anx_songs = ["*Show Yourself* by Ayla Nereo","*Let Her Go* by Passenger","*Shameless* by Ani Difranco","*Mississippi* by Rising Appalachia","*Gajumaru* by Yaima","*Pushing the Needle Too Far* by the Indigo Girls","*I Release Control* by Alexa Sunshine Rose"]
frust_songs = ["*Shameless* by Ani Difranco","*Blood and Fire* by the Indigo Girls","*Shameless* by Ani Difranco","*So What* by P!nk","*Aint No Grave* by Crooked Still","*You Oughta Know* by Alanis Morissette","*Crossing Muddy Waters* by I'm With Her"]
power_songs = ["*Royals* by Lorde","*Strange Fire* by the Indigo Girls","*Hurricane* by Kris Delmhorst","*Ekombe* by Jupiter & Okwess","*Chelsea Morning* by Joni Mitchell","*Not Ready to Make Nice* by the Dixie Chicks","*Show Yourself* by Alya Nereo"]


## Activate whatchawant to ask user what they want, then create references/links between wants/to-dos, and print the result
def want_songs(song_list):
    keep_playing = whatchawant()
    if keep_playing == "H" or keep_playing == "h":
        song_choice = song_list[0]
    elif keep_playing == "I" or keep_playing == "i":
        song_choice = song_list[1]
    elif keep_playing == "J" or keep_playing == "j":
        song_choice = song_list[2]
    elif keep_playing == "K" or keep_playing == "k":
        song_choice = song_list[3]
    elif keep_playing == "L" or keep_playing == "l":
        song_choice = song_list[4]
    elif keep_playing == "M" or keep_playing == "m":
        song_choice = song_list[5]
    elif keep_playing == "N" or keep_playing == "n":
        song_choice = song_list[6]
    return print("You should definitely, absolutely listen to", song_choice, "right now. You're welcome.")


## Main: combines all of the prior functions: asks user how they feel, what they want, and spits out a song.
def song_picker():
    lets_play = howyafeeling()
    if lets_play == "A" or lets_play == "a":
        want_songs(joy_songs)
    elif lets_play == "B" or lets_play == "b":
        want_songs(energ_songs)
    elif lets_play == "C" or lets_play == "c":
        want_songs(tired_songs)
    elif lets_play == "D" or lets_play == "d":
        want_songs(weepy_songs)
    elif lets_play == "E" or lets_play == "e":
        want_songs(anx_songs)
    elif lets_play == "F" or lets_play == "f":
        want_songs(frust_songs)
    elif lets_play == "G" or lets_play == "g":
        want_songs(power_songs)

    
if __name__ == "__main__":
    song_picker()