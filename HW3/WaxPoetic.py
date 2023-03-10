import random


Nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
Verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
Adjectives = ["furry", "balding", "incredulous", "fragrant","exuberant", "glistening"]
Prepositions = ["against", "after", "into", "beneath", "upon","for" , "in", "like", "over", "within"]
Adverbs = ["curiously", "extravagantly", "tantalizingly","furiously", "sensuously"]



def creat_poem(nouns,verbs,adjec,prepos,adverb):
    vowels = ['a','e','o','i','u',]
    poem = []
    adj1 = random.choice(adjec)
    noun1 = random.choice(nouns)

    if adj1[0] in vowels:
        poem.append("An")
    else:
        poem.append("A")

    poem.append(adj1)
    poem.append(noun1)
    poem.append("\n")
    poem.append(poem[0])
    poem.append(adj1)
    poem.append(noun1)
    poem.append(random.choice(verbs))
    poem.append(random.choice(prepos))
    poem.append("the")
    poem.append(random.choice(adjec))
    noun2 = random.choice(nouns)
    poem.append(noun2)
    poem.append("\n")
    poem.append(random.choice(adverb))
    poem.append(", the")
    poem.append(noun1)
    poem.append(random.choice(verbs))
    poem.append("\n")
    poem.append("the")
    poem.append(noun2)
    poem.append(random.choice(verbs))
    poem.append(random.choice(prepos))
    poem.append('a')
    poem.append(random.choice(adjec))
    poem.append(random.choice(nouns))

    return poem


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele + " "

    # return string
    return str1

poem = creat_poem(Nouns,Verbs,Adjectives,Prepositions,Adverbs)

result = listToString(poem)
print(result)


# {A/An} {adj1} {noun1}
# {A/An} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
# {adverb1}, the {noun1} {verb2}
# the {noun2} {verb3} {prep2} a {adj3} {noun3}