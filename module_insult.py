"""
Module that, when called, insults people, in true Tumblr fashion.

Tumblr dictionary and logic shamelessly stolen from https://github.com/Lokaltog/tumblr-argument-generator, thank you!
"""

import random
import string

def _tumblr_insult(args):

    tumblrDictionary = {
        'insult': [
            'burn in hell',
            'check your {privilegedNoun} privilege',
            'die in a fire',
            'die in a ditch',
            'drop dead',
            'fuck off',
            'fuck you',
            'go drown in your own piss',
            'go fuck yourself',
            'go play in traffic',
            'kill yourself',
            'light yourself on fire',
            'make love to yourself in a furnace',
            'please die',
            'rot in hell',
            'screw you',
            'shut the fuck up',
            'shut up',
        ],
        'insultAdverb': [
            'antediluvian',
            'awful',
            'chauvinistic',
            'ciscentric',
            'close-minded',
            'deluded',
            'entitled',
            'fucking',
            'goddamn',
            'heteropatriarchal',
            'ignorant',
            'inconsiderate',
            'intolerant',
            'judgmental',
            'misogynistic',
            'nphobic',
            'oppressive',
            'pathetic',
            'patriarchal',
            'racist',
            'rape-culture-supporting',
            'sexist',
            'worthless',
        ],
        'insultNoun': [
            'MRA',
            'TERF',
            'ableist',
            'ageist',
            'anti-feminist',
            'asshole',
            'assimilationist',
            'basement dweller',
            'bigot',
            'brogrammer',
            'chauvinist',
            'classist',
            'creep',
            'dudebro',
            'essentialist',
            'fascist',
            'feminazi',
            'femscum',
            'hitler',
            'kyriarchist',
            'lowlife',
            'misogynist',
            'mouthbreather',
            'nazi',
            'neckbeard',
            'oppressor',
            'patriarchist',
            'pedophile',
            'piece of shit',
            'radscum',
            'rape-apologist',
            'rapist',
            'redditor',
            'scum',
            'sexist',
            'subhuman',
            'transmisogynist',
            'virgin',
        ],
        'marginalizedNoun': [
            'CAFAB',
            'CAMAB',
            'LGBTQIA+',
            'PoC',
            'QTPOC',
            'WoC',
            'activist',
            'androphilia',
            'appearance',
            'asian',
            'attractive',
            'bi',
            'black',
            'body hair',
            'celestial',
            'chubby',
            'closet',
            'color',
            'cross-dresser',
            'curvy',
            'deathfat',
            'demi',
            'differently abled',
            'disabled',
            'diversity',
            'dysphoria',
            'estrogen-affinity',
            'ethnic',
            'ethnicity',
            'fandom',
            'fat love',
            'fat',
            'fatist',
            'fatty',
            'female',
            'feminist',
            'feminist',
            'freeganist',
            'furry',
            'genderless',
            'gynephilia',
            'headmate',
            'height',
            'hijra',
            'indigenous',
            'intersectionality',
            'intersexual',
            'invisible',
            'kin',
            'latin@',
            'lesbianist',
            'little person',
            'marginalized',
            'minority',
            'multigender',
            'multiple system',
            'native american',
            'non-gender',
            'non-white',
            'obesity',
            'otherkin',
            'privilege',
            'prosthetic',
            'queer',
            'radfem',
            'saami',
            'skinny',
            'smallfat',
            'stretchmark',
            'therian',
            'thin',
            'third-gender',
            'trans*',
            'transman',
            'transnormative',
            'transwoman',
            'trigger',
            'two-spirit',
            'womyn',
            'wymyn',
        ],
        'personalPrefixes': [
            'dandy',
            'demi',
            'gender',
        ],
        'personalPostfixes': [
            'amorous',
            'femme',
            'fluid',
            'queer',
            'fuck',
        ],
        'sexualPrefixes': [
            'a',
            'bi',
            'demi',
            'multi',
            'non',
            'omni',
            'pan',
            'para',
            'poly',
            'trans',
        ],
        'sexualPostfixes': [
            'gender',
            'sexual',
            'romantic',
            'queer',
        ],
        'marginalizedAdverb': [
            'antediluvian',
            'attacking',
            'chauvinistic',
            'close-minded',
            'dehumanizing',
            'denying',
            'discriminating',
            'hypersexualizing',
            'ignoring',
            'intolerant',
            'misogynistic',
            'nphobic',
            'objectifying',
            'oppressive',
            'patriarchal',
            'phobic',
            'racist',
            'rape-culture-supporting',
            'sexist',
            'sexualizing',
            'shaming',
        ],
        'marginalizedIsm': [
            'fatist',
            'feminist',
            'freeganist',
            'lesbianist',
        ],
        'privilegedNoun': [
            'able-body',
            'binary',
            'cis',
            'cisgender',
            'cishet',
            'hetero',
            'male',
            'middle-class',
            'smallfat',
            'thin',
            'uterus-bearing',
            'white',
        ],
        'privilegedAdverb': [
            'normative',
            'elitist',
            'overprivileged',
            'privileged',
        ],
        'privilegedIsm': [
            'ableist',
            'ageist',
            'anti-feminist',
            'chauvinist',
            'classist',
            'kyriarchist',
            'misogynist',
            'nazi',
            'patriarchist',
            'sexist',
            'transmisogynist',
        ]
    }

    rand = random.Random()

    buildstr = ""

    insult = rand.choice(tumblrDictionary['insult'])
    if "{privilegedNoun}" in insult:
        insult = string.replace(insult, "{privilegedNoun}", rand.choice(tumblrDictionary['privilegedNoun']))
    buildstr = buildstr + insult + ', '
    buildstr = buildstr + args.strip() + ', '
    buildstr = buildstr + "you "

    if rand.random() > 0.3:
        buildstr = buildstr + rand.choice(tumblrDictionary['insultAdverb']) + ' '
    if rand.random() > 0.3:
        if rand.random() > 0.5:
            choice = rand.choice(tumblrDictionary['marginalizedIsm'])
        else:
            choice = rand.choice(tumblrDictionary['marginalizedNoun'])
    else:
        if rand.random() > 0.5:
            choice = rand.choice(tumblrDictionary['personalPrefixes']) + rand.choice(tumblrDictionary['personalPostfixes'])
        else:
            choice = rand.choice(tumblrDictionary['sexualPrefixes']) + rand.choice(tumblrDictionary['sexualPostfixes'])
        buildstr = buildstr + choice + '-' + rand.choice(tumblrDictionary['marginalizedAdverb']) + ', '

    buildstr = buildstr + rand.choice(tumblrDictionary['privilegedNoun']) + '-' + rand.choice(tumblrDictionary['privilegedAdverb']) + ' '
    buildstr = buildstr + rand.choice(tumblrDictionary['insultNoun']) + " " + rand.choice(tumblrDictionary['privilegedIsm']) + ' '

    return buildstr.upper()

def _banal_insult(nick, args):
    """Bringing back the old insults."""
    import linecache
    import os

    def file_len(fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
            return i+1

    insults_path = os.getcwd() + "/modules/insults.txt"
    linecount = file_len(insults_path)
    insult_line = linecache.getline(insults_path, random.randint(0, linecount))

    return_line = str(args).strip() + ", " + str(nick) + " would like you to know that " + str(insult_line)

    return return_line


def command_insult(bot, user, channel, args):
    """Insults a person of your choice. Use with a complete and utter disregard for feelings and restraint."""
    
    # Quick and dirty functionality to have the bot randomly choose between insulting methods.
    # I will replace this with a more generic solution when I have more time to devote to it.
    if random.random() > 0.5:
        retstr = _banal_insult(bot.factory.getNick(user), args)
    else:
        retstr = _tumblr_insult(args)

    bot.say(channel, retstr)
    return
