def winner(names):
    votes = dict()
    max_vote = 0
    for name in names:
        if name not in votes:
            # Register the candidate
            votes[name] = 0
        # Add 1 to candidate's vote
        votes[name] += 1
        max_vote = max(max_vote, votes[name])
    potential_winners = [name for name in votes if votes[name] == max_vote]
    potential_winners.sort()
    print(potential_winners[0])
    return potential_winners[0]


s = "john,johnny,jackie,johnny,john,jackie,jamie,jamie,john,johnny,jamie,johnny,john"
names = s.split(",")
winner(names)

