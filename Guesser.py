questions = [
    'Is your character real?',
    'Is your character male?',
    'Is your character yellow?',
    'Is your character a human?',
    'Does your character have red hair?',
    'Does your character live in the future?',
    'Is your character fond of donuts?']

characters = {
    'Homer Simpson':
        {'Is your character real?':
            {0: 12, 1: 1},
         'Is your character male?':
            {0: 1, 1: 12},
         'Is your character yellow?':
            {0: 1, 1: 15},
         'Is your character a human?':
            {0: 5, 1: 15},
         'Does your character have red hair?':
            {0: 12, 1: 1},
         'Does your character live in the future?':
            {0: 13, 1: 1},
         'Is your character fond of donuts?':
            {0: 1, 1: 13},
         'Does your character have a bad haircut?':
            {0: 1, 1: 4}
         },
    'Philip J. Fry':
        {'Is your character real?':
            {0: 12, 1: 2},
         'Is your character male?':
            {0: 1, 1: 15},
         'Is your character yellow?':
            {0: 12, 1: 3},
         'Is your character a human?':
            {0: 1, 1: 10},
         'Does your character have red hair?':
            {0: 3, 1: 10},
         'Does your character live in the future?':
            {0: 3, 1: 12},
         'Is your character fond of donuts?':
            {0: 7, 1: 1},
         'Does your character have a bad haircut?':
            {0: 5, 1: 2}
         },
    'Spongebob':
        {'Is your character real?':
            {0: 12, 1: 1},
         'Is your character male?':
            {0: 5, 1: 10},
         'Is your character yellow?':
            {0: 1, 1: 15},
         'Is your character a human?':
            {0: 15, 1: 1},
         'Does your character have red hair?':
            {0: 15, 1: 1},
         'Does your character live in the future?':
            {0: 5, 1: 2},
         'Is your character fond of donuts?':
            {0: 12, 1: 2},
         'Does your character have a bad haircut?':
            {0: 5, 1: 2}
         },
      'Donald Trump':
        {'Is your character real?':
            {0: 0, 1: 10},
         'Is your character male?':
            {0: 0, 1: 10},
         'Is your character yellow?':
            {0: 5, 1: 3},
         'Is your character a human?':
            {0: 0, 1: 10},
         'Does your character have red hair?':
            {0: 5, 1: 1},
         'Does your character live in the future?':
            {0: 9, 1: 0},
         'Is your character fond of donuts?':
            {0: 5, 1: 6},
         'Does your character have a bad haircut?':
            {0: 1, 1: 10}
         }
}

# calculates the weighted average for the given answer
def calculate_weighted_average(character, answer, question):
    weighted_avg = characters[character][question][1] / (characters[character][question][0] + characters[character][question][1])

    if int(answer) == 1:
        return weighted_avg
    elif int(answer) == 0:
        return 1 - weighted_avg


def get_answer_probability(question, user_answer, character_to_ignore):
    yes_count = 0
    no_count = 0

    for character, answer in characters.items():
        if character != character_to_ignore:
            yes_count += characters[character][question][1]
            no_count += characters[character][question][0]

    if user_answer == 1:
        return yes_count / (yes_count + no_count)
    elif user_answer == 0:
        return no_count / (yes_count + no_count)


def calculate_character_probability(character, user_answers):
    p_character = 1 / len(characters)

    numerator = p_character

    for question, answer in user_answers.items():
        numerator *= calculate_weighted_average(character, answer, question)

    denominator = numerator
    denominator_add = 1 - p_character

    for question, answer in user_answers.items():
        denominator_add *= get_answer_probability(question, answer, character)
    
    denominator += denominator_add

    return numerator / denominator


print(calculate_character_probability('Donald Trump', 
        {'Is your character real?': 1,
         'Is your character male?': 1,
         'Is your character yellow?': 1,
         'Is your character a human?': 1,
         'Does your character have red hair?': 0,
         'Does your character live in the future?': 0,
         'Is your character fond of donuts?': 1
         }))