def findValley(heights):
    """
    Assumption: 'heights' is a nonempty list of integers with the guarantee
    that there is some index 0 <= i < len(l) such that the sublist
    heights[0:i+1] is strictly decreasing and the sublist heights[i:len(l)] is
    strictly increasing. So heights[i] is the 'valley'.

    Return the index i of the valley. Your algorithm must run in O(log n) time.

    You can assume that we will only test your implementation with
    lists that satisfy the above property.

    Examples:
    findValley([10, 7, 4, 1, 3, 6])
    3

    findValley([4])
    0

    findValley([3, 2, 1])
    2

    findValley([9, 14])
    0

    findValley([11, 2, 11, 12])
    1
    """

    pass



def climbing(heights, rest, limit):
    """
    Assumption: 'heights' is a nonempty list of positive integers that are
    strictly increasing and both 'rest' and 'limit' are positive integers.

    The list 'heights' is the various heights (in feet) of ledges on a cliff.
    The value 'rest' represents how many seconds you have to rest between
      climbing "bursts" (see the description below).
    The value 'limit' is how many seconds you have to climb the cliff, and is
      guaranteed to be at least the last height in the list.

    Suppose you are able to climb 1 foot per second consecutively for a certain
    amount of time, let's call this time 'burst'. However, after at most 'burst'
    seconds you have to rest for 'rest' seconds on one of the ledges of the
    cliff to regain your stamina. You cannot rest while hanging on to the cliff,
    you have to be on a ledge when you rest. You rest the same amount of time
    even if your latest climb was not for 'burst' seconds.

    What is the minimum value of 'burst' such that you are able to reach the
    highest ledge in at most 'limit' seconds?

    Example 1:
    climbing([30, 70, 95, 120, 145, 190], 10, 210)
    70

    That is, if you can climb for 70 seconds consecutively between rests, then:
     In your first burst, you can reach ledge 70.
     In your second burst, you can reach ledge 120.
     In your final burst, you reach the top.
    In total, you spend 190 seconds climbing and 20 seconds resting, which is
     exactly the value of 'limit'

    However, if you can only climb for 69 seconds then the fastest you can
    climb the cliff is:
     In your first burst, you can only reach ledge 30.
     In your second burst, you reach ledge 95.
     In your third burst, you reach ledge 120.
     In your fourth burst, you reach ledge 145.
     Finally, you reach ledge 190.
    In total, you spent 190 seconds climbing and 40 seconds resting, too long!

    Example 2:
    climbing([50, 100], 1, 100)
    100

    That is, you can reach the top in a single burst if you can climb for 100
    seconds consecutively.

    However, if you can only climb for 99 seconds consecutively then the best
    you can do is reach ledge 50, rest for 1 second, then reach the top for a
    total of 101 seconds.

    Example 3:
    climbing([50, 99], 1, 100)
    50

    That is, if you can climb for 50 seconds consecutively then you can reach
    the ledge at height 50 in your first burst, rest for 1 second, then reach
    the top after 49 more seconds for a total of 100 seconds.

    But if you can only climb for 49 seconds consecutively then you can't even
    reach the first ledge!
    """

    pass
