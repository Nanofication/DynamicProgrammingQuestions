"""

Move robots from one side to another to line up for award ceromony in order of winners.

"""

class Robot:
    def __init__(self, rank = 0, position = 0):
        self.rank = rank
        self.position = position



""" Try all forms of moving robots across at once and return the max"""
def BruteForceLineUp(robots, highestPosition):
    if len(robots) == 1:
        return 1
    for i in range(0, len(robots) - 1):
        currentBot = robots[i]

        for j in range(i, len(robots) - 1):
            if HasCrossed(currentBot, robots[j + 1]) == False and currentBot.position > highestPosition:
                highestPosition = currentBot.position
                robots.pop(0)
                count = BruteForceLineUp(robots, highestPosition) + 1
                return max(BruteForceLineUp(robots, highestPosition), count)
            else:
                robots.pop(0)
                return BruteForceLineUp(robots, highestPosition)

def HasCrossed(robot1, robot2):
    print robot1.rank
    print robot2.rank
    print "\n"
    if robot1.rank < robot2.rank:
        if robot1.position < robot2.position:
            return False
        else:
            return True
    else:
        if robot1.position < robot2.position:
            return False
        else:
            return True


bot1 = Robot(1,16)
bot2 = Robot(2,8)
bot3 = Robot(3,6)
bot4 = Robot(4,15)

robots = [bot1, bot2, bot3, bot4]

print BruteForceLineUp(robots, 0)