import csv

english_words = ['meme', 'cookie', 'app', 'app', 'dumpling',
    'emoticon', 'fashionista', 'selfie', 'smiley',
    'nickname', 'quiz', 'vibe', 'incel', 'software',
    'smartphone', 'remake', 'gigabyte', 'countdown',
    'firewall', 'fidget spinner', 'youtuber', 'outfit',
    'laptop', 'tablet', 'tablet', 'chat', 'viagra', 'smog',
    'livestream', 'look', 'captcha', 'hackathon']

japanese_words = ['torii', 'yukata', 'anime', 'anime', 'izakaya',
    'gyoza', 'kombucha', 'ikigai', 'akita', 'akita', 'keiretsu',
    'emoji', 'sudoku', 'tofu', 'haiku', 'haiku', 'netsuke',
    'hikikomori', 'onsen', 'tanuki', 'sake', 'mochi', 'geisha']

words = english_words + japanese_words
answers = {}
gender_to_int = {'un': 0, 'una': 1}
ett_count = {w:0 for w in words}

# read csv and create dictionary with responses
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    column_start = 9
    columns = len(words)

    for row in csv_reader:
        if line_count > 0:
            answers[line_count] = {words[i-column_start]:gender_to_int[row[i]] for i in range(column_start, column_start+columns) if row[i] in ['un', 'una']}
        line_count += 1

for a in answers.values():
    for b in a.keys():
        ett_count[b] += a[b]
ett_count = dict(sorted(ett_count.items(), key=lambda item: -item[1]))

sorted_answers = {}

for a in answers.keys():
    sorted_answers[a] = [answers[a][w] for w in ett_count.keys()]

sorted_answers = dict(sorted(sorted_answers.items(), key=lambda item: -item[1].count(gender_to_int['una'])))
