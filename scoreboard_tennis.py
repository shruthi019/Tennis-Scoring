points = {0: 0, 1: 15, 2: 30, 3: 40, 4: 'Adv'}


def sets_won(player1, GamesWon, SetsWon):
    player2 = 'B' if player1 == 'A' else 'A'
    if (GamesWon[player1] == 6 and GamesWon[player2] <= 4) or \
            (GamesWon[player1] > 6 and GamesWon[player1] - GamesWon[player2] == 2):
        SetsWon[player1] += 1
        GamesWon[player1] = GamesWon[player2] = 0
    return GamesWon, SetsWon


def games_won(player1, GamesWon, SetsWon):
    GamesWon[player1] += 1
    GamesWon, SetsWon = sets_won(player1, GamesWon, SetsWon)
    return GamesWon, SetsWon


def deuce(s, i, scores, GamesWon, SetsWon):
    player1 = s[i]
    player2 = 'A' if player1 == 'B' else 'B'
    if scores[player1] != 4 and scores[player2] != 4:
        scores[player1] = 4
    elif scores[player1] == 4:
        scores[player1] = scores[player2] = 0
        GamesWon, SetsWon = games_won(player1, GamesWon, SetsWon)
    elif scores[player2] == 4:
        scores[player1] = scores[player2] = 3
    return scores, GamesWon, SetsWon


def score(s: str):
    scores = {'A': 0, 'B': 0}
    GamesWon = {'A': 0, 'B': 0}
    SetsWon = {'A': 0, 'B': 0}
    i = 0
    while i < len(s):

        while (scores['A'] == scores['B'] and scores['A'] == 3) or (scores['A'] == 4 and scores['B'] == 3) \
                or (scores['B'] == 4 and scores['A'] == 3):
            if i >= len(s):
                return (points[scores['A']], points[scores['B']]), GamesWon, SetsWon
            scores, GamesWon, SetsWon = deuce(s, i, scores, GamesWon, SetsWon)
            i += 1

        if i < len(s):
            if scores[s[i]] != 3:
                scores[s[i]] += 1
            elif scores[s[i]] == 3:
                scores['A'] = scores['B'] = 0
                GamesWon, SetsWon = games_won(s[i], GamesWon, SetsWon)
            i += 1

    return (points[scores['A']], points[scores['B']]), GamesWon, SetsWon


s = input()
print('player: A B')
scoreboard = score(s)
print('sets:', ' '.join(str(i) for i in list(scoreboard[2].values())))
print('games:', ' '.join(str(i) for i in list(scoreboard[1].values())))
print('score:', ' '.join(str(i) for i in scoreboard[0]))
