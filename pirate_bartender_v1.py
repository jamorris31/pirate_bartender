import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
  }

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
  }

def askQuestion():
  answers = {}
  for key in questions.keys():
    my_input = raw_input(questions[key])
    if my_input == "yes" or my_input == "y":
      answers[key] = True
    else:
      answers[key] = False
  return answers


def makeDrink(theAnswers):
  theDrink = []
  for key in theAnswers:
    if theAnswers[key] == True:
      theDrink.append(random.choice(ingredients[key]))
import random

def askquestion():
    questions = {
        "strong": "Do ye like yer drinks strong? ",
        "salty": "Do ye like it with a salty tang? ",
        "bitter": "Are ye a lubber who likes it bitter? ",
        "sweet": "Would ye like a bit of sweetness with yer poison? ",
        "fruity": "Are ye one for a fruity finish? "
    }

    answers = {}

    for key in questions.keys():
        my_input = raw_input(questions[key]).lower()
        if my_input == "yes" or my_input == "y":
            answers[key] = True
        else:
            answers[key] = False
    return answers

def makedrink(theAnswers):

    ingredients = {
        "strong": ["glug of rum", "slug of whisky", "splash of gin"],
        "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
        "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
        "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
        "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
    }

    theDrink = []
    for key in theAnswers:
        if theAnswers[key] == True:
            theDrink.append(random.choice(ingredients[key]))
    return theDrink


def pickcooldrinkname():
    drinknames = {
        "adjective": ["Slimy", "Black", "Crusty", "Golden", "Haunted"],
        "noun": ["Jack Sparrow", "Petey", "Treasure", "Ship", "Skeleton"]
    }

    random.seed();
    adj = random.choice(drinknames["adjective"])
    noun = random.choice(drinknames["noun"])
    coolname = "{} {}".format(adj,noun)
    return coolname

def main():
    keepdrinking = True
    while keepdrinking:
        preferences = askquestion()
        drink = makedrink(preferences)
        coolname = pickcooldrinkname()

        print "One drink coming up"
        print "{}".format(coolname)

        for ingredient in drink:
            print "A {}".format(ingredient)
        print "Want another one, matey? "
        keepdrinking = raw_input().lower() in ["yes", "y"]

if __name__ == '__main__':
  main()
                   
