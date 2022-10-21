from play import Play

scissors = Play("scissors", "✂️")
rock = Play("rock", "⛰️")
paper = Play("paper", "📝")
lizard = Play("lizard", "🦎")
spock = Play("Spock", "🖖")

scissors.wins = [paper, lizard]
rock.wins = [scissors, lizard]
paper.wins = [rock, spock]
lizard.wins = [paper, spock]
spock.wins = [rock, scissors]

dictionary = {"1":rock, "2":paper, "3":scissors, "4":lizard, "5":spock}