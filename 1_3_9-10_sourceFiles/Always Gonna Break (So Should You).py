####
# Each team's file must define four tokens:
#     team_name: 15
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = '' # Only 10 chars displayed.
strategy_name = 'The KEY to success'
strategy_description = "The way in which this system works is that the system checks the first 10 responses of a person to determine if the person has the key. If they do, then the system will collude with them the other 89 times. The final move will be a betray to act as a minor addition, so that every successful key will increase my score by 100. If at any point the key doesnt work or the person betrays, a failsafe is initiated, and the code reverts to a predetermined algorithm which determines the other user's algorithm with a sample size of ten moves."
    
def move(my_history, their_history, my_score, their_score):
    th = their_history
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    currentTrialLength = len(th)
    dicStepper = 0
    desicion = ''
    previousTrialDesicion = th()
    theirDictionary = {}
    publicKey = {"key0":"c", "key1":"c", "key2":"b", "key3":"b","key4":"c","key5":"b","key6":"c","key7":"b","key8":"b","key9":"c"}
    privateKey = {"key0":"b", "key1":"b", "key2":"c", "key3":"c","key4":"b","key5":"c","key6":"b","key7":"c","key8":"c","key9":"b"}
    keyActivated = False
    keyReject = False
    while dicStepper < len(th):
        theirDictionary['trial{0}'.format(dicStepper)] = th[dicStepper]
        dicStepper = dicStepper + 1
    while currentTrial > 10 and keyReject == False:
        if currentTrial == 0:
            desicion = privateKey['key{0}'.format(currentTrial)]
        elif currentTrial < 0:
            if theirDictionary['trial{0}'.format(previousTrial)] == publicKey['key{0}'.format(previousTrial)]:
                desicion = privateKey['key{0}'.format(currentTrial)]
            else:
                desicion = fail_safe()
                
                
        
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    return desicion

def fail_safe():
    return "b"
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             