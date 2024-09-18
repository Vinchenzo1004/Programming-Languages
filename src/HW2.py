import random

questions = [
    {
        "Spaghetti or Meat?\na. Spaghetti\nb. Meat\nc. None\nd. Both",
        "scores": {"a": 2, "b": 1, "c": -1, "d": 0}
    },
    {
    "How many eggs tall are you?\na. Ten\nb. About seven\nc. A number that is better than 24 ;)\nd. This is a stupid question",
    "scores": {"a": 0, "b": 2, "c": 1, "d": -1}
    },
    {
    "Who's the best live action Spider-Man?\na. Tom Holland\nb. Tobey Maguire\nc. Andrew Garfield\nd. None, Spider-Man's for nerds",
    "scores": {"a": 0, "b": 1, "c": 2, "d": -1}
    },
    {
    "What's the first ten digits of pi?\na. 3.141592653\nb. 3.141582653\nc. 3.142592653\nd. 3.141592663",
    "scores": {"a": -1, "b": 1, "c": 2, "d": 0}
    },
    {
    "If when you do so, would you and when, but also how and why, possibly who?\na. What are you even saying?\nb. Yes, Today, With a Moonlight Greatsword, Because, No\nc. No.\nd. Maybe, Might Be Tomorrow, Might Be With a Kamehameha, Might Be Out of Spite or Vengenance, You.",
    "scores": {"a": -1, "b": 1, "c": 0, "d": 2}
    }
]

def ask_questions():
    total_score = 0
    selected_questions = random.sample(questions, 3)
    for item in selected_questions:
        print(item["question"])
        response = input("Please pick a letter: ").strip().lower()

        while response not in ['a', 'b', 'c', 'd']:
            print("Not an answer. Please try again.")
            response = input("Please choose an answer: ").strip().lower()

        total_score += item["scores"][response]

    return total_score

def determine_nerdity(total_score):
    if total_score < 0:
        return "Congratulations, you're extremely boring and like to have no fun whatsoever. No one likes you."
    elif total_score == 0:
        return "Meh"
    elif total_score > 0:
        if total_score % 2 == 0:
            return "The nerdiest nerd out there. You're pretty cool."
        else:
            return "Almost the coolest person out there. You're alright."

def main():
    print("Time to determine how nerdy you are!")
    total_score = ask_questions()
    result = determine_nerdity(total_score)
    print(result)

if __name__ == "__main__":
    main()
