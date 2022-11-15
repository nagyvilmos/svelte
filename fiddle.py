import random

class Standing:
    def __init__(self, team) -> None:
        self.team = team
        self.played = 0
        self.won = 0
        self.drawn = 0
        self.lost = 0
        self.scored = 0
        self.against = 0
        self.games = []

    def __str__(self):
        return f"({self.team}\t,P {self.played}\t,W {self.won}\t,D {self.drawn}\t,L {self.lost}\t,Pts {3*self.won+self.drawn}\t,G/D {self.scored-self.against})"

    def compare(self, other):
        return self.get_points()-other.get_points() or \
            self.get_goal_difference() - other.get_goal_differnce() or \
            self.scored - other.scored or \
            other.played - self.played

    def get_score(self, game):
        opponent = [t for t in game.keys() if t != self.team][0]
        scored = game.get(self.team, 0)
        against = game.get(opponent, 0)
        return (scored, against)

    def get_distribution(self):
        w = 0.333
        l = 0.333
        d = 0.333

        for g in self.games:
            (f,a) = self.get_score(g)
            if f>a:
                w+=1
            elif f<a:
                l+=1
            else:
                d+=1
            w/=2
            l/=2
            d/=2
        return (w,l,d)

    def get_points(self):
        return self.won*3+self.drawn

    def get_goal_difference(self):
        return self.scored-self.against

    def add_game(self, game):
        self.games.append(game)
        (scored, against) = self.get_score(game)

        self.played += 1
        self.scored += scored
        self.against += against

        if scored > against:
            self.won += 1
        elif scored < against:
            self.lost += 1
        else:
            self.drawn += 1

    def sym_game(self, other):
        sd = self.get_distribution()
        od = other.get_distribution()

        w = sd[0] + od[1] + .1
        l = sd[1] + od[0] + .1
        d = sd[2] + od[2] + .1
        result = random.random() *(w+l+d)
        game = {}
        if result < w:
            game[self.team] = 1
            game[other.team] = 0
        elif result < w+l:
            game[self.team] = 0
            game[other.team] = 1
        else:
            game[self.team] = 0
            game[other.team] = 0
        return game

    def add_sym(self, other):
        game = self.sym_game(other)
        self.add_game(game)
        other.add_game(game)

    def run_sym(self, other, times):
        win = 0
        lose = 0
        for i in range(times):
            game = self.sym_game(other)
            if game[self.team] > game[other.team]:
                win += 1
            elif game[self.team] < game[other.team]:
                lose += 1
        print(f"{self.team}\t{other.team}\t{100.0*win/times}\t{100.0*lose/times}")


results = [
    {"Crystal Palace": 0, "Arsenal": 2},
    {"Fulham": 2, "Liverpool": 2},
    {"AFC Bournemouth": 2, "Aston Villa": 0},
    {"Leeds United": 2, "Wolverhampton Wanderers": 1},
    {"Newcastle United":    2, "Nottingham Forest": 0},
    {"Tottenham Hotspur":    4, "Southampton": 1},
    {"Everton":    0, "Chelsea": 1},
    {"Leicester City":    2, "Brentford": 2},
    {"Manchester United":    1, "Brighton & Hove Albion": 2},
    {"West Ham United": 0, "Manchester City": 2},
    {"Aston Villa": 2, "Everton": 1},
    {"Arsenal": 4, "Leicester City": 2},
    {"Brighton & Hove Albion": 0, "Newcastle United": 0},
    {"Manchester City": 4, "AFC Bournemouth": 0},
    {"Southampton": 2, "Leeds United": 2},
    {"Wolverhampton Wanderers": 0, "Fulham": 0},
    {"Brentford": 4, "Manchester United": 0},
    {"Nottingham Forest": 1, "West Ham United": 0},
    {"Chelsea": 2, "Tottenham Hotspur": 2},
    {"Liverpool": 1, "Crystal Palace": 1},
    {"Tottenham Hotspur": 1, "Wolverhampton Wanderers": 0},
    {"Crystal Palace": 3, "Aston Villa": 1},
    {"Everton": 1, "Nottingham Forest": 1},
    {"Fulham": 3, "Brentford": 2},
    {"Leicester City": 1, "Southampton": 2},
    {"AFC Bournemouth": 0, "Arsenal": 3},
    {"Leeds United": 3, "Chelsea": 0},
    {"West Ham United": 0, "Brighton & Hove Albion": 2},
    {"Newcastle United": 3, "Manchester City": 3},
    {"Manchester United": 2, "Liverpool": 1},
    {"Southampton":0, "Manchester United":1},
    {"Brentford":1, "Everton":1},
    {"Brighton & Hove Albion":1, "Leeds United":0},
    {"Chelsea":2, "Leicester City":1},
    {"Liverpool":9, "AFC Bournemouth":0},
    {"Manchester City":4, "Crystal Palace":2},
    {"Arsenal":2, "Fulham":1},
    {'Aston Villa':0, "West Ham United":1},
    {"Wolverhampton Wanderers":1, "Newcastle United":1},
    {'Nottingham Forest':0, "Tottenham Hotspur":2},
]

to_play = [
    ['Fulham', "Brighton & Hove Albion"],
    ['Crystal Palace', 'Brentford'],
    ['Southampton', 'Chelsea'],
    ["Leeds United", 'Everton'],
    ["AFC Bournemouth", "Wolverhampton Wanderers"],
    ['Arsenal', 'Aston Villa'],
    ["Manchester City", 'Nottingham Forest'],
    ["West Ham United", "Tottenham Hotspur"],
    ['Liverpool', "Newcastle United"],
    ["Leicester City", "Manchester United"],
    ['Everton', 'Liverpool'],
    ['Brentford', "Leeds United"],
    ["Newcastle United", 'Crystal Palace'],
    ['Nottingham Forest', "AFC Bournemouth"],
    ["Tottenham Hotspur", 'Fulham'],
    ["Wolverhampton Wanderers", 'Southampton'],
    ['Aston Villa', "Manchester City"],
    ["Brighton & Hove Albion", "Leicester City"],
    ['Chelsea', "West Ham United"],
    ["Manchester United", 'Arsenal'],
    ['Fulham', 'Chelsea'],
    ["AFC Bournemouth", "Brighton & Hove Albion"],
    ["Leicester City", 'Aston Villa'],
    ['Liverpool', "Wolverhampton Wanderers"],
    ['Southampton', 'Brentford'],
    ["Manchester City", "Tottenham Hotspur"],
    ['Arsenal', 'Everton'],
    ["West Ham United", "Newcastle United"],
    ['Crystal Palace', "Manchester United"],
    ["Leeds United", 'Nottingham Forest'],
    ['Aston Villa', 'Southampton'],
    ['Nottingham Forest', 'Fulham'],
    ["Wolverhampton Wanderers", "Manchester City"],
    ["Brighton & Hove Albion", 'Crystal Palace'],
    ['Everton', "West Ham United"],
    ["Newcastle United", "AFC Bournemouth"],
    ["Tottenham Hotspur", "Leicester City"],
    ['Brentford', 'Arsenal'],
    ["Manchester United", "Leeds United"],
    ['Chelsea', 'Liverpool'],
    ['Arsenal', "Tottenham Hotspur"],
    ["AFC Bournemouth", 'Brentford'],
    ['Crystal Palace', 'Chelsea'],
    ['Fulham', "Newcastle United"],
    ['Liverpool', "Brighton & Hove Albion"],
    ['Southampton', 'Everton'],
    ["West Ham United", "Wolverhampton Wanderers"],
    ["Manchester City", "Manchester United"],
    ["Leeds United", 'Aston Villa'],
    ["Leicester City", 'Nottingham Forest'],
    ["AFC Bournemouth", "Leicester City"],
    ['Chelsea', "Wolverhampton Wanderers"],
    ["Manchester City", 'Southampton'],
    ["Newcastle United", 'Brentford'],
    ["West Ham United", 'Fulham'],
    ["Brighton & Hove Albion", "Tottenham Hotspur"],
    ['Crystal Palace', "Leeds United"],
    ['Arsenal', 'Liverpool'],
    ['Everton', "Manchester United"],
    ['Nottingham Forest', 'Aston Villa'],
    ['Brentford', "Brighton & Hove Albion"],
    ["Leicester City", 'Crystal Palace'],
    ['Fulham', "AFC Bournemouth"],
    ['Southampton', "West Ham United"],
    ["Wolverhampton Wanderers", 'Nottingham Forest'],
    ["Tottenham Hotspur", 'Everton'],
    ['Aston Villa', 'Chelsea'],
    ["Leeds United", 'Arsenal'],
    ["Manchester United", "Newcastle United"],
    ['Liverpool', "Manchester City"],
    ["Brighton & Hove Albion", 'Nottingham Forest'],
    ['Crystal Palace', "Wolverhampton Wanderers"],
    ["AFC Bournemouth", 'Southampton'],
    ["Newcastle United", 'Everton'],
    ['Liverpool', "West Ham United"],
    ["Manchester United", "Tottenham Hotspur"],
    ['Brentford', 'Chelsea'],
    ['Fulham', 'Aston Villa'],
    ["Leicester City", "Leeds United"],
    ['Arsenal', "Manchester City"],
    ['Nottingham Forest', 'Liverpool'],
    ['Everton', 'Crystal Palace'],
    ["Tottenham Hotspur", "Newcastle United"],
    ['Aston Villa', 'Brentford'],
    ["Leeds United", 'Fulham'],
    ["Manchester City", "Brighton & Hove Albion"],
    ['Southampton', 'Arsenal'],
    ["Wolverhampton Wanderers", "Leicester City"],
    ['Chelsea', "Manchester United"],
    ["West Ham United", "AFC Bournemouth"],
    ["Leicester City", "Manchester City"],
    ["AFC Bournemouth", "Tottenham Hotspur"],
    ['Brentford', "Wolverhampton Wanderers"],
    ["Brighton & Hove Albion", 'Chelsea'],
    ['Crystal Palace', 'Southampton'],
    ["Newcastle United", 'Aston Villa'],
    ['Fulham', 'Everton'],
    ['Arsenal', 'Nottingham Forest'],
    ['Liverpool', "Leeds United"],
    ["Manchester United", "West Ham United"],
    ['Aston Villa', "Manchester United"],
    ['Chelsea', 'Arsenal'],
    ['Everton', "Leicester City"],
    ["Leeds United", "AFC Bournemouth"],
    ["Manchester City", 'Fulham'],
    ['Nottingham Forest', 'Brentford'],
    ['Southampton', "Newcastle United"],
    ["Tottenham Hotspur", 'Liverpool'],
    ["West Ham United", 'Crystal Palace'],
    ["Wolverhampton Wanderers", "Brighton & Hove Albion"],
    ["AFC Bournemouth", 'Everton'],
    ["Brighton & Hove Albion", 'Aston Villa'],
    ['Fulham', "Manchester United"],
    ['Liverpool', 'Southampton'],
    ["Manchester City", 'Brentford'],
    ["Newcastle United", 'Chelsea'],
    ['Nottingham Forest', 'Crystal Palace'],
    ["Tottenham Hotspur", "Leeds United"],
    ["West Ham United", "Leicester City"],
    ["Wolverhampton Wanderers", 'Arsenal'],
    ['Arsenal', "West Ham United"],
    ['Aston Villa', 'Liverpool'],
    ['Brentford', "Tottenham Hotspur"],
    ['Chelsea', "AFC Bournemouth"],
    ['Crystal Palace', 'Fulham'],
    ['Everton', "Wolverhampton Wanderers"],
    ["Leeds United", "Manchester City"],
    ["Leicester City", "Newcastle United"],
    ["Manchester United", 'Nottingham Forest'],
    ['Southampton', "Brighton & Hove Albion"],
    ["AFC Bournemouth", 'Crystal Palace'],
    ["Brighton & Hove Albion", 'Arsenal'],
    ['Fulham', 'Southampton'],
    ['Liverpool', "Leicester City"],
    ["Manchester City", 'Everton'],
    ["Newcastle United", "Leeds United"],
    ['Nottingham Forest', 'Chelsea'],
    ["Tottenham Hotspur", 'Aston Villa'],
    ["West Ham United", 'Brentford'],
    ["Wolverhampton Wanderers", "Manchester United"],
    ['Arsenal', "Newcastle United"],
    ['Aston Villa', "Wolverhampton Wanderers"],
    ['Brentford', 'Liverpool'],
    ['Chelsea', "Manchester City"],
    ['Crystal Palace', "Tottenham Hotspur"],
    ['Everton', "Brighton & Hove Albion"],
    ["Leeds United", "West Ham United"],
    ["Leicester City", 'Fulham'],
    ["Manchester United", "AFC Bournemouth"],
    ['Southampton', 'Nottingham Forest'],
    ['Aston Villa', "Leeds United"],
    ['Brentford', "AFC Bournemouth"],
    ["Brighton & Hove Albion", 'Liverpool'],
    ['Chelsea', 'Crystal Palace'],
    ['Everton', 'Southampton'],
    ["Manchester United", "Manchester City"],
    ["Newcastle United", 'Fulham'],
    ['Nottingham Forest', "Leicester City"],
    ["Tottenham Hotspur", 'Arsenal'],
    ["Wolverhampton Wanderers", "West Ham United"],
    ["AFC Bournemouth", 'Nottingham Forest'],
    ['Arsenal', "Manchester United"],
    ['Crystal Palace', "Newcastle United"],
    ['Fulham', "Tottenham Hotspur"],
    ["Leeds United", 'Brentford'],
    ["Leicester City", "Brighton & Hove Albion"],
    ['Liverpool', 'Chelsea'],
    ["Manchester City", "Wolverhampton Wanderers"],
    ['Southampton', 'Aston Villa'],
    ["West Ham United", 'Everton'],
    ['Aston Villa', "Leicester City"],
    ['Brentford', 'Southampton'],
    ["Brighton & Hove Albion", "AFC Bournemouth"],
    ['Chelsea', 'Fulham'],
    ['Everton', 'Arsenal'],
    ["Manchester United", 'Crystal Palace'],
    ["Newcastle United", "West Ham United"],
    ['Nottingham Forest', "Leeds United"],
    ["Tottenham Hotspur", "Manchester City"],
    ["Wolverhampton Wanderers", 'Liverpool'],
    ["AFC Bournemouth", "Newcastle United"],
    ['Arsenal', 'Brentford'],
    ['Crystal Palace', "Brighton & Hove Albion"],
    ['Fulham', 'Nottingham Forest'],
    ["Leeds United", "Manchester United"],
    ["Leicester City", "Tottenham Hotspur"],
    ['Liverpool', 'Everton'],
    ["Manchester City", 'Aston Villa'],
    ['Southampton', "Wolverhampton Wanderers"],
    ["West Ham United", 'Chelsea'],
    ['Aston Villa', 'Arsenal'],
    ['Brentford', 'Crystal Palace'],
    ["Brighton & Hove Albion", 'Fulham'],
    ['Chelsea', 'Southampton'],
    ['Everton', "Leeds United"],
    ["Manchester United", "Leicester City"],
    ["Newcastle United", 'Liverpool'],
    ['Nottingham Forest', "Manchester City"],
    ["Tottenham Hotspur", "West Ham United"],
    ["Wolverhampton Wanderers", "AFC Bournemouth"],
    ["AFC Bournemouth", "Manchester City"],
    ['Crystal Palace', 'Liverpool'],
    ['Everton', 'Aston Villa'],
    ['Fulham', "Wolverhampton Wanderers"],
    ["Leeds United", 'Southampton'],
    ["Leicester City", 'Arsenal'],
    ["Manchester United", 'Brentford'],
    ["Newcastle United", "Brighton & Hove Albion"],
    ["Tottenham Hotspur", 'Chelsea'],
    ["West Ham United", 'Nottingham Forest'],
    ['Arsenal', "AFC Bournemouth"],
    ['Aston Villa', 'Crystal Palace'],
    ['Brentford', 'Fulham'],
    ["Brighton & Hove Albion", "West Ham United"],
    ['Chelsea', "Leeds United"],
    ['Liverpool', "Manchester United"],
    ["Manchester City", "Newcastle United"],
    ['Nottingham Forest', 'Everton'],
    ['Southampton', "Leicester City"],
    ["Wolverhampton Wanderers", "Tottenham Hotspur"],
    ["AFC Bournemouth", 'Liverpool'],
    ['Crystal Palace', "Manchester City"],
    ['Everton', 'Brentford'],
    ['Fulham', 'Arsenal'],
    ["Leeds United", "Brighton & Hove Albion"],
    ["Leicester City", 'Chelsea'],
    ["Manchester United", 'Southampton'],
    ["Newcastle United", "Wolverhampton Wanderers"],
    ["Tottenham Hotspur", 'Nottingham Forest'],
    ["West Ham United", 'Aston Villa'],
    ['Arsenal', 'Crystal Palace'],
    ['Aston Villa', "AFC Bournemouth"],
    ['Brentford', "Leicester City"],
    ["Brighton & Hove Albion", "Manchester United"],
    ['Chelsea', 'Everton'],
    ['Liverpool', 'Fulham'],
    ["Manchester City", "West Ham United"],
    ['Nottingham Forest', "Newcastle United"],
    ['Southampton', "Tottenham Hotspur"],
    ["Wolverhampton Wanderers", "Leeds United"],
    ["AFC Bournemouth", 'Fulham'],
    ['Arsenal', "Leeds United"],
    ["Brighton & Hove Albion", 'Brentford'],
    ['Chelsea', 'Aston Villa'],
    ['Crystal Palace', "Leicester City"],
    ['Everton', "Tottenham Hotspur"],
    ["Manchester City", 'Liverpool'],
    ["Newcastle United", "Manchester United"],
    ['Nottingham Forest', "Wolverhampton Wanderers"],
    ["West Ham United", 'Southampton'],
    ['Aston Villa', 'Nottingham Forest'],
    ['Brentford', "Newcastle United"],
    ['Fulham', "West Ham United"],
    ["Leeds United", 'Crystal Palace'],
    ["Leicester City", "AFC Bournemouth"],
    ['Liverpool', 'Arsenal'],
    ["Manchester United", 'Everton'],
    ['Southampton', "Manchester City"],
    ["Tottenham Hotspur", "Brighton & Hove Albion"],
    ["Wolverhampton Wanderers", 'Chelsea'],
    ['Aston Villa', "Newcastle United"],
    ['Chelsea', "Brighton & Hove Albion"],
    ['Everton', 'Fulham'],
    ["Leeds United", 'Liverpool'],
    ["Manchester City", "Leicester City"],
    ['Nottingham Forest', "Manchester United"],
    ['Southampton', 'Crystal Palace'],
    ["Tottenham Hotspur", "AFC Bournemouth"],
    ["West Ham United", 'Arsenal'],
    ["Wolverhampton Wanderers", 'Brentford'],
    ["AFC Bournemouth", "West Ham United"],
    ['Arsenal', 'Southampton'],
    ['Brentford', 'Aston Villa'],
    ["Brighton & Hove Albion", "Manchester City"],
    ['Crystal Palace', 'Everton'],
    ['Fulham', "Leeds United"],
    ["Leicester City", "Wolverhampton Wanderers"],
    ['Liverpool', 'Nottingham Forest'],
    ["Manchester United", 'Chelsea'],
    ["Newcastle United", "Tottenham Hotspur"],
    ['Everton', "Newcastle United"],
    ["Leeds United", "Leicester City"],
    ['Nottingham Forest', "Brighton & Hove Albion"],
    ["Tottenham Hotspur", "Manchester United"],
    ["West Ham United", 'Liverpool'],
    ["Wolverhampton Wanderers", 'Crystal Palace'],
    ['Aston Villa', 'Fulham'],
    ['Chelsea', 'Brentford'],
    ['Southampton', "AFC Bournemouth"],
    ["Manchester City", 'Arsenal'],
    ["AFC Bournemouth", "Leeds United"],
    ['Arsenal', 'Chelsea'],
    ['Brentford', 'Nottingham Forest'],
    ["Brighton & Hove Albion", "Wolverhampton Wanderers"],
    ['Crystal Palace', "West Ham United"],
    ['Fulham', "Manchester City"],
    ["Leicester City", 'Everton'],
    ['Liverpool', "Tottenham Hotspur"],
    ["Manchester United", 'Aston Villa'],
    ["Newcastle United", 'Southampton'],
    ["AFC Bournemouth", 'Chelsea'],
    ["Brighton & Hove Albion", 'Everton'],
    ['Fulham', "Leicester City"],
    ['Liverpool', 'Brentford'],
    ["Manchester City", "Leeds United"],
    ["Newcastle United", 'Arsenal'],
    ['Nottingham Forest', 'Southampton'],
    ["Tottenham Hotspur", 'Crystal Palace'],
    ["West Ham United", "Manchester United"],
    ["Wolverhampton Wanderers", 'Aston Villa'],
    ['Arsenal', "Brighton & Hove Albion"],
    ['Aston Villa', "Tottenham Hotspur"],
    ['Brentford', "West Ham United"],
    ['Chelsea', 'Nottingham Forest'],
    ['Crystal Palace', "AFC Bournemouth"],
    ['Everton', "Manchester City"],
    ["Leeds United", "Newcastle United"],
    ["Leicester City", 'Liverpool'],
    ["Manchester United", "Wolverhampton Wanderers"],
    ['Southampton', 'Fulham'],
    ["AFC Bournemouth", "Manchester United"],
    ["Brighton & Hove Albion", 'Southampton'],
    ['Fulham', 'Crystal Palace'],
    ['Liverpool', 'Aston Villa'],
    ["Manchester City", 'Chelsea'],
    ["Newcastle United", "Leicester City"],
    ['Nottingham Forest', 'Arsenal'],
    ["Tottenham Hotspur", 'Brentford'],
    ["West Ham United", "Leeds United"],
    ["Wolverhampton Wanderers", 'Everton'],
    ['Arsenal', "Wolverhampton Wanderers"],
    ['Aston Villa', "Brighton & Hove Albion"],
    ['Brentford', "Manchester City"],
    ['Chelsea', "Newcastle United"],
    ['Crystal Palace', 'Nottingham Forest'],
    ['Everton', "AFC Bournemouth"],
    ["Leeds United", "Tottenham Hotspur"],
    ["Leicester City", "West Ham United"],
    ["Manchester United", 'Fulham'],
    ['Southampton', 'Liverpool']
]


def load_games():
    table = {}
    for game in results:
        keys = game.keys()
        for team in keys:
            standing = table.get(team, None)
            if standing is None:
                standing = Standing(team)
                table[team] = standing
            standing.add_game(game)
    return table


def sym_games(table, syms=None):
    for game in to_play:
        if syms == None:
            table[game[0]].add_sym(table[game[1]])
        else:
            table[game[0]].run_sym(table[game[1]], syms)

def print_table(table):
    for t in sorted(table, key=lambda t: table[t].get_points(), reverse=True):
        print(table[t])

if __name__ == "__main__":
    random.seed(54371)
    table = load_games()
    print_table(table)
    print("---")
    sym_games(table)
    print_table(table)

    random.seed(54371)
    syms = 1000
    positions = {}
    for x in range(syms):
        table = load_games()
        sym_games(table)
        i = 0
        for t in sorted(table, key=lambda t: table[t].get_points(), reverse=True):
            if positions.get(t) is None:
                positions[t] = [0 for x in range(20)]
            positions[t][i] += 1
            i += 1
    for p in positions:
        sum = 0
        pos=positions[p]
        for i in range(20):
            sum+=pos[i]*(i)
        print(f"{p}\t{pos}\t{sum/syms}")
