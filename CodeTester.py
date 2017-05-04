
from controller.LoopController import LoopController

# ** OPTIONS **

# Running time in minutes for each query running over database, 
# after this time it will be skipped if it has not finished yet
QUERY_TIME_LIMIT = 20 # minutes


# Running time in seconds for each query running over database, 
# after this time it will be skipped if it has not finished yet
limit = QUERY_TIME_LIMIT * 60 #seconds


if __name__ == "__main__":

	lC = LoopController(limit)
	lC.mainLoop()