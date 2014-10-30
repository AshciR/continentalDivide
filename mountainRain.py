# mountainRain.py
# Written by: Richard Walker
# Date: October 30, 2014

# Array that holds the mountain information that Kristina Walker gave me
krisMountArr = [ [3,2,1,4,6],
                 [1,4,3,5,4],
                 [3,2,4,2,1],
                 [4,5,5,1,1],
                 [6,2,3,2,3] ]

# Array that holds mountain information that was made by me
richMountArr = [ [1,2,3,2,1],
                 [2,5,4,5,2],
                 [3,4,5,4,3],
                 [2,5,4,5,2],
                 [1,2,3,2,1] ]

def printMtn(mountArr):
    """ Takes a Mountain array and Prints the Mount information matrix """
    for coord in mountArr:
        print coord

def checkPoint(mountArr, x_pos, y_pos):
    """ Takes a 2D array which represents the mountain's topography.
        and the coordinates you want to check."""

    # You need to check the four flow directions. 

    # Checking the x-axis: ---------------------

    # Checks the forward flow,
    # if it flows, then it reached the Atlantic ocean  
    x_atlantic = checkFlow(mountArr[y_pos], x_pos, True)

    # Checks the backward flow
    # if it flows, then it reached the Pacific ocean  
    x_pacific = checkFlow(mountArr[y_pos], x_pos, False)

    # ------------------------------------------
    
    # You need to transpose the matrix in order to use
    # the check flow in the y-direction
    transMtn = zip(*mountArr)

    # Now you can checking the y-axis: ---------
    
    # Checks the forward flow,
    # if it flows, then it reached the Atlantic ocean  
    y_atlantic = checkFlow(transMtn[x_pos], y_pos, True)

    # Checks the backward flow,
    # if it flows, then it reached the Pacific ocean
    y_pacific = checkFlow(mountArr[x_pos], y_pos, False)

    # ------------------------------------------

    # Check if it flows into either ocean first, if thats true, then
    # check if flows into both oceans. If so, then it's a Continental Divide
    return (x_atlantic or x_pacific) and (y_atlantic or y_pacific)


def checkFlow(arr, strtPos, direction):
    """ Takes an array and the starting position in the array,
    and a boolean which represents the direction.

    Then checks if the subsequent positions in the array have
    a lower value that the previous. 
    
    If direction is true it checks forward, left -> right.
    If direction is false, it checks backward, right -> left """

    # If direction is forward
    if (direction):

        # If your in the last element of the array, there
        # are no more positions to check, so the flow must
        # have been true
        if (strtPos == (len(arr) - 1)):
            flow = True

        else:
            # For loop from the starting index, to the
            # penultimate element in the array
            for pos in range(strtPos, (len(arr) - 1)):

                # Else if the next element in the array is smaller than
                # the current element, then flow is possible
                if arr[pos + 1] < arr[pos]:
                    flow = True

                # else, flow isn't possible
                else:
                    flow = False
                    # Stop the for loop
                    break;

    # The direction is Backwards
    else:

        # If your in the first element of the array, there
        # are no more positions to check, so the flow must
        # have been true
        if (strtPos == 0):
            flow = True

        else:
            # Else check the subsequent positions
            for pos in range(strtPos, 0, -1):

                # if the next element in the array is smaller than
                # the current element, then flow is possible
                if arr[pos - 1] < arr[pos]:
                    flow = True

                # else, flow isn't possible
                else:
                    flow = False
                    # Stop the for loop
                    break;

    return flow            

