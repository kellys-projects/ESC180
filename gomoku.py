
###############################################################
def is_empty(board):
    # empty board [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],****, [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    for i in range(len(board)):
        for j in range(len(board[i])): 
            if len(board[i][j].strip()) > 0:
                return False
    return True

###############################################################

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    
    if d_y == 1 and d_x == 0:
       return is_bounded_1_0(board, y_end, x_end, length, d_y, d_x)
    elif d_y == 0 and d_x == 1:
       return is_bounded_0_1(board, y_end, x_end, length, d_y, d_x)
    elif d_y == 1 and d_x == 1:
       return is_bounded_1_1(board, y_end, x_end, length, d_y, d_x)
    elif d_y == 1 and d_x == -1:
       return is_bounded_1m1(board, y_end, x_end, length, d_y, d_x)
    
################################################################

def is_win(board):
    # This function determines the current status of the game, and returns one of
    # ["White won", "Black won", "Draw", "Continue playing"] 
    COLOUR_B = "b"
    COLOUR_W = "w"
    LENGTH_5 = 5
    be_seq_exist = True
    result = ["White won", "Black won", "Draw", "Continue playing"]

    for i in range (len(board) -1):
        for j in range(1, len(board[0])-1):
           # one_open_seq_count, one_semi_open_seq_count = 0, 0 # the one open or semi-open seq count in the board
            if board[i][j] == COLOUR_B: 
               if check_win(board, i, j, COLOUR_B):
                  return result[1]
            elif board[i][j] == COLOUR_W:
               if check_win(board, i, j, COLOUR_W):
                  return result[0]
    if isFull(board):
       return result[2]
    else:
       return result[3]   

 
################################################################
def search_max(board):
    MAX_SCORE = 100000
    COLOUR_B = "b"
    EMPTY_COLOUR = " "
    moveTuple_1_0 = ()
    moveTuple_0_1 = ()
    moveTuple_1_1 = ()
    moveTuple_1m1 = ()
    moveTuple_non = ()
        
    board_score = score(board)
    # if black or white already has a sequence with length = 5
    if (board_score == MAX_SCORE) or (board_score == -MAX_SCORE):
       return moveTuple_non   
    
    for i in range (len(board) -1):
        for j in range(1, len(board[0])-1):
           # one_open_seq_count, one_semi_open_seq_count = 0, 0 # the one open or semi-open seq count in the board
            if board[i][j] == COLOUR_B:  
          
               ############### search length = 4 #####################
               # param (board, col, y_start, x_start, length, d_y, d_x) 
               moveTuple_1_0 = search_max_1_0(board, "b", i, j, 4, 1, 0)
               if moveTuple_1_0 != moveTuple_non :
                  return moveTuple_1_0
               moveTuple_0_1 = search_max_0_1(board, "b", i, j, 4, 0, 1)
               if moveTuple_0_1 != moveTuple_non :
                  return moveTuple_0_1
               moveTuple_1_1 = search_max_1_1(board, "b", i, j, 4, 1, 1)
               if moveTuple_1_1 != moveTuple_non :
                  return moveTuple_1_1
               moveTuple_1m1 = search_max_1m1(board, "b", i, j, 4, 1, -1)
               if moveTuple_1m1 != moveTuple_non :
                  return moveTuple_1m1
               
               ############### search length = 3 #####################
               # param (board, col, y_start, x_start, length, d_y, d_x) 
               moveTuple_1_0 = search_max_1_0(board, "b", i, j, 3, 1, 0)
               if moveTuple_1_0 != moveTuple_non :
                  return moveTuple_1_0
               moveTuple_0_1 = search_max_0_1(board, "b", i, j, 3, 0, 1)
               if moveTuple_0_1 != moveTuple_non :
                  return moveTuple_0_1
               moveTuple_1_1 = search_max_1_1(board, "b", i, j, 3, 1, 1)
               if moveTuple_1_1 != moveTuple_non :
                  return moveTuple_1_1
               moveTuple_1m1 = search_max_1m1(board, "b", i, j, 3, 1, -1)
               if moveTuple_1m1 != moveTuple_non :
                  return moveTuple_1m1
               
               ############### search length = 2 #####################
               # param (board, col, y_start, x_start, length, d_y, d_x) 
               moveTuple_1_0 = search_max_1_0(board, "b", i, j, 2, 1, 0)
               if moveTuple_1_0 != moveTuple_non :
                  return moveTuple_1_0
               moveTuple_0_1 = search_max_0_1(board, "b", i, j, 2, 0, 1)
               if moveTuple_0_1 != moveTuple_non :
                  return moveTuple_0_1
               moveTuple_1_1 = search_max_1_1(board, "b", i, j, 2, 1, 1)
               if moveTuple_1_1 != moveTuple_non :
                  return moveTuple_1_1
               moveTuple_1m1 = search_max_1m1(board, "b", i, j, 2, 1, -1)
               if moveTuple_1m1 != moveTuple_non :
                  return moveTuple_1m1
               
               ############### search length = 1 #####################
               # param (board, col, y_start, x_start, length, d_y, d_x) 
               moveTuple_1_0 = search_max_1_0(board, "b", i, j, 1, 1, 0)
               if moveTuple_1_0 != moveTuple_non :
                  return moveTuple_1_0
               moveTuple_0_1 = search_max_0_1(board, "b", i, j, 1, 0, 1)
               if moveTuple_0_1 != moveTuple_non :
                  return moveTuple_0_1
               moveTuple_1_1 = search_max_1_1(board, "b", i, j, 1, 1, 1)
               if moveTuple_1_1 != moveTuple_non :
                  return moveTuple_1_1
               moveTuple_1m1 = search_max_1m1(board, "b", i, j, 1, 1, -1)
               if moveTuple_1m1 != moveTuple_non :
                  return moveTuple_1m1

################################################################

def detect_rows(board, col, length):
   ####CHANGE ME
    open_seq_count, semi_open_seq_count = 0, 0
    # loop through the board
    for i in range (len(board) -1):
        for j in range(1, len(board[0])-1):
           # one_open_seq_count, one_semi_open_seq_count = 0, 0 # the one open or semi-open seq count in the board
            if board[i][j] == col:
             
               # detect_row(board, col, y_start, x_start, length, d_y, d_x)
               # check case 1: (d_y,d_x) = (1, 0) is : direction top-to-bottom
               open_seq_count_1_0, semi_open_seq_count_1_0 = detect_row( board, col,i, j, length, 1, 0)
               # check case 2: (d_y,d_x) = (0, 1) is : direction left-to-right
               open_seq_count_0_1, semi_open_seq_count_0_1 = detect_row(board, col, i, j, length, 0, 1)
               # check case 3: (d_y,d_x) = (1, 1) is : direction upper-left-to-lower-right
               open_seq_count_1_1, semi_open_seq_count_1_1 = detect_row(board, col, i, j, length, 1, 1)
               # check case 3: (d_y,d_x) = (1,-1) is : direction upper-right-to-lower-left
               open_seq_count_1m1, semi_open_seq_count_1m1 = detect_row(board, col, i, j, length, 1, -1)

               open_seq_count += open_seq_count_1_0 + open_seq_count_0_1 + open_seq_count_1_1 + open_seq_count_1m1             
               semi_open_seq_count += semi_open_seq_count_1_0 + semi_open_seq_count_0_1  + semi_open_seq_count_1_1  + semi_open_seq_count_1m1 
   
    return open_seq_count, semi_open_seq_count

################################################################  
#   
# detect_row(board, col, y_start, x_start, length, d_y, d_x)
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    rowtuple =(0,0)
    # the last stone at location      
    y_end = y_start + d_y * (length -1)
    x_end = x_start + d_x * (length-1)

    isQualifiedToCheck = isQualifiedToDetect(board, col, y_start, x_start, length, d_y, d_x)
    if isQualifiedToCheck:
      ## case 1: (d_y,d_x) = (1, 0) is : direction top-to-bottom
      if d_y == 1 and d_x == 0:
         rowtuple = detect_row_1_0(board, col, y_start, x_start, length, d_y, d_x)

      ## case 2: (d_y,d_x) = (0, 1) is : direction left-to-right 
      elif d_y == 0 and d_x == 1: 
         rowtuple = detect_row_0_1(board, col, y_start, x_start, length, d_y, d_x)
    
      ## case 3: (d_y,d_x) = (1, 1) is : direction upper-left-to-lower-right
      elif d_y == 1 and d_x == 1:
         rowtuple = detect_row_1_1(board, col, y_start, x_start, length, d_y, d_x)
      ## case 4: (d_y,d_x) = (1,-1) is : direction upper-right-to-lower-left  
      elif d_y == 1 and d_x == -1:  
         rowtuple = detect_row_1m1(board, col, y_start, x_start, length, d_y, d_x)
      else:
         rowtuple = (0,0)

    return rowtuple
###############################################################################
def isFull(board):
   for i in range(len(board)):
        for j in range(len(board[i])): 
            if len(board[i][j].strip()) == 0:
                return False
   return True
###############################################################################
# i = start_y, j = start_x
def check_win (board, i, j, col):
   # check (1,0)
   if i + 4 <= len(board )-1 :
      if board[i + 1][j] == col and board[i + 2][j] == col and board[i + 3][j] == col and board[i + 4][j] == col:
         return True
   # check (0,1)
   elif j + 4 <= len(board )-2 :
      if board[i][j + 1] == col and board[i][j + 2] == col and board[i][j + 3] == col and board[i][j + 4] == col:
       return True
   # check (1,1)
   elif i + 4 <= len(board )-1 and j + 4 <= len(board )-2:
      if board[i + 1][j + 1] == col and board[i + 2][j + 2] == col and board[i + 3][j + 3] == col and board[i+4][j + 4] == col:
       return True
   # check (1, -1)
   elif i + 4 <= len(board )-1 and j - 4 >= 1:
      if board[i + 1][j - 1] == col and board[i + 2][j - 2] == col and board[i + 3][j - 3] == col and board[i+4][j - 4] == col:
       return True
   else:
      return False
   
#############################################################################################
def isQualifiedToDetect(board, col, y_start, x_start, length, d_y, d_x):
   RealSeqLen = 0
   isQualified = False

   y_end = y_start + d_y * (length -1)
   x_end = x_start + d_x * (length-1)
   if y_end > len(board) -1 or x_end > len(board) -1:
      return False
   if d_y == 1 and d_x == 0:
      for i in range (1,length + 1):
            if y_start + i > y_end or board[y_start + i][x_start] != col:
               # no sequence
               if i == 1:
                  RealSeqLen = 1
               else:
                  RealSeqLen = i 
               break

   elif d_y == 0 and d_x == 1: 
     for i in range (1,length + 1):
            if board[y_start][x_start + i] != col:
               if i == 1:
                  RealSeqLen = 1
               else:
                  RealSeqLen = i 
               break
   elif d_y == 1 and d_x == 1: 
     for i in range (1,length + 1):
            if board[y_start + i][x_start + i] != col:
               if i == 1:
                  RealSeqLen = 1 
               else:
                  RealSeqLen = i
               break
   elif d_y == 1 and d_x == -1: 
      for i in range (1,length + 1):
          if board[y_start + i][x_start - i] != col:
             if i == 1:
                  RealSeqLen = 1 
             else:
                  RealSeqLen = i 
             break
   #print("RealSeqLen",RealSeqLen)
   #print("checked Length",length)
   if RealSeqLen == length:
      isQualified = True
   #print("isQualified",isQualified)
   return isQualified

########################################################

# param (board, col, y_start, x_start, length, d_y, d_x)   
def search_max_1_0(board, col, y_start, x_start, length, d_y, d_x):
    
    moveTuple =()
    open_count =0 
    semi_open_count = 0
   # detect_row_1_0(board, col, y_start, x_start, length, d_y, d_x)
   # end location
    y_end = y_start + d_y * (length -1)
    x_end = x_start + d_x * (length-1)
   # board score for x_move & y_move
    score_start = 0
    score_end = 0
    empty_col = " "
    if length == 1:
      if (board[y_start - 1][x_start] != empty_col and board[y_start - 1][x_start] != col ):
         moveTuple =(y_end, x_end + 1 )
         return moveTuple
      elif (board[y_start + 1][x_start] != empty_col and board[y_start + 1][x_start] != col ):
         moveTuple =(y_end, x_end + 1 )
         return moveTuple
      else:
         moveTuple =(y_start - 1, x_start )
         return moveTuple
    open_count, semi_open_count = detect_row_1_0(board, col, y_start, x_start, length, d_y, d_x)
    # open sequence
    if open_count > 0:
       # since it is an open sequence, it is empty before and after the sequence
       board[y_start - 1][x_start] = col
       score_start = score(board)
       # rollback the board change
       board[y_start - 1][x_start] = empty_col
       #
       board[y_end + 1][x_end] = col
       score_end = score(board)
       # rollback the board change
       board[y_end + 1][x_end] = empty_col
       if score_start >= score_end:
           moveTuple =(y_start - 1, x_start)
           
       else:
           moveTuple =(y_end + 1, x_end)

    # semi_open sequence
    elif semi_open_count > 0:
       # if no space before the start of the sequence
       if y_start == 0 or ( board[y_start - 1][x_start]!= empty_col and board[y_start -1][x_start] != col):
           moveTuple =(y_end + 1, x_end)
       else:
           moveTuple =(y_start - 1, x_start)

    return moveTuple       
######################################################################### 

def search_max_0_1(board, col, y_start, x_start, length, d_y, d_x):
    
    moveTuple =()
    open_count = 0 
    semi_open_count = 0
   # detect_row(board, col, y_start, x_start, length, d_y, d_x)
   # end location
    y_end = y_start + d_y * (length -1)
    x_end = x_start + d_x * (length-1)
   # board score for x_move & y_move
    score_start = 0 
    score_end = 0
    empty_col = " "
    if length == 1:
      if ( board[y_start][x_start - 1] != empty_col and board[y_start][x_start - 1] != col ):
         moveTuple =(y_end , x_end + 1)
         return moveTuple
      else:
         moveTuple = (y_start, x_start - 1)
         return moveTuple
    open_count, semi_open_count = detect_row(board, col, y_start, x_start, length, d_y, d_x)

    # open sequence
    if open_count > 0:
       # since it is an open sequence, it is empty before and after the sequence
       board[y_start][x_start - 1] = col
       score_start = score(board)
       # rollback the board change
       board[y_start][x_start - 1] = empty_col
       #
       print("y_end",y_end)
       print("x_end + 1",x_end + 1)
       board[y_end][x_end + 1] = col
       score_end = score(board)
       # rollback the board change
       board[y_end][x_end + 1] = empty_col
       if score_start >= score_end:
           moveTuple =(y_start, x_start - 1)
           
       else:
           moveTuple =(y_end , x_end + 1)

    # semi_open sequence
    elif semi_open_count > 0:
       # if no space before the start of the sequence
       if x_start == 1 or (board[y_start][x_start -1 ]!= empty_col and board[y_start][x_start -1 ] != col):
           moveTuple =(y_end, x_end + 1)
       else:
           moveTuple =(y_start, x_start -1)

    return moveTuple       
#########################################################################      

def search_max_1_1(board, col, y_start, x_start, length, d_y, d_x):
    
    moveTuple =()
    open_count =0 
    semi_open_count = 0
   # detect_row_1_0(board, col, y_start, x_start, length, d_y, d_x)
   # end location
    y_end = y_start + d_y * (length -1)
    x_end = x_start + d_x * (length-1)
   # board score for x_move & y_move
    score_start = 0 
    score_end = 0
    empty_col = " "
    if length == 1:
      if (board[y_start - 1][x_start - 1] != empty_col and board[y_start - 1][x_start - 1] != col ):
          moveTuple =(y_end + 1 , x_end + 1)
          return moveTuple
      else:
          moveTuple =(y_start -1 , x_start - 1)
          return moveTuple
    open_count, semi_open_count = detect_row(board, col, y_start, x_start, length, d_y, d_x)
    # open sequence
    if open_count > 0:
       # since it is an open sequence, it is empty before and after the sequence
       board[y_start -1][x_start - 1] = col
       score_start = score(board)
       # rollback the board change
       board[y_start -1][x_start - 1] = empty_col
       #
       board[y_end + 1][x_end + 1] = col
       score_end = score(board)
       # rollback the board change
       board[y_end + 1][x_end + 1] = empty_col
       if score_start >= score_end:
           moveTuple =(y_start - 1, x_start - 1)
           
       else:
           moveTuple =(y_end + 1, x_end + 1)

    # semi_open sequence
    elif semi_open_count > 0:
       # if no space before the start of the sequence
       if x_start == 1 or y_start ==0 or (board[y_start - 1][x_start -1 ]!= empty_col and board[y_start - 1][x_start -1 ] != col):
           moveTuple =(y_end + 1, x_end + 1)
       else:
           moveTuple =(y_start - 1, x_start -1)

    return moveTuple       

#########################################################################
def search_max_1m1(board, col, y_start, x_start, length, d_y, d_x):
    
    moveTuple =()
    open_count = 0 
    semi_open_count = 0
   # detect_row_1_0(board, col, y_start, x_start, length, d_y, d_x)
   # end location
    y_end = y_start + d_y * (length -1)
    x_end = x_start + d_x * (length-1)
   # board score for x_move & y_move
    score_start = 0 
    score_end = 0
    empty_col = " "
    if length == 1:
      if(board[y_start - 1][x_start + 1] != empty_col and board[y_start - 1][x_start + 1] != col):
         moveTuple =(y_end + 1, x_end - 1)
         return moveTuple
      else:
         moveTuple =(y_start - 1, x_start + 1)
         return moveTuple
    open_count, semi_open_count = detect_row(board, col, y_start, x_start, length, d_y, d_x)
    # open sequence
    if open_count > 0:
       # since it is an open sequence, it is empty before and after the sequence
       board[y_start -1][x_start + 1] = col
       score_start = score(board)
       # rollback the board change
       board[y_start -1][x_start + 1] = empty_col
       #
       board[y_end + 1][x_end - 1] = col
       score_end = score(board)
       # rollback the board change
       board[y_end + 1][x_end - 1] = empty_col
       if score_start >= score_end:
           moveTuple =(y_start - 1, x_start + 1)
           
       else:
           moveTuple =(y_end + 1, x_end - 1)

    # semi_open sequence
    elif semi_open_count > 0:
       # if no space before the start of the sequence
       if x_start == len(board) -2  or y_start ==0 or (board[y_start - 1][x_start +1 ]!= empty_col and board[y_start - 1][x_start +1 ] != col):
           moveTuple =(y_end + 1, x_end -1)
       else:
           moveTuple =(y_start - 1, x_start +1)

    return moveTuple       

#############################################################


def is_bounded_1_0(board, y_end, x_end, length, d_y, d_x):
    
    y_start = y_end - d_y * (length -1)
    x_start = x_end - d_x * (length-1)
    bound = ["OPEN","SEMIOPEN","CLOSED"]
   ## case 1: (d_y,d_x) = (1, 0) is : direction top-to-bottom
   ## direction top-to-bottom sequence not start /end at edge
    if y_start >= 1 and y_end < len(board) - 1:
         # if there is no stone at start and end of the sequence, it is open sequence
         if (board[y_start-1][x_start] == " ") and (board[y_end+1][x_start] == " "): #  open sequence with length col stones
            return  bound[0]
              # if there is a stone before the first stone of sequence and no stone after the sequence, it is semi-open
         elif (board[y_start-1][x_start] != " ") and (board[y_end+1][x_end] == " "):
            return  bound[1] 
         # if there is a stone after the last stone of the sequence , it is semi-open
         elif (board[y_start-1][x_start] == " ") and (board[y_end+1][x_end] != " "):
            return  bound[1] 
         else:
            return  bound[2]    # closed or no sequence

   ## direction top-to-bottom sequence start at top row
    elif y_start == 0: # start at top row
         # if there is a stone after the last stone of the sequence
         if board[y_end+1][x_end] != " ":
            return  bound[2]    # closed or no sequence
         else:
            return  bound[1]    # semi_open sequence   
   ## direction top-to-bottom sequence end at bottom row
    elif y_end == len(board) -1: # end at bottom row
         # if there is a stone before the first stone of the sequence
         if board[y_start-1][x_start] != " " :
            return  bound[2]   # closed or no sequence
         else:
            return  bound[1]   # semi_open sequence
         
######################################################
def is_bounded_0_1(board, y_end, x_end, length, d_y, d_x): 
    y_start = y_end - d_y * (length -1)
    x_start = x_end - d_x * (length-1)
    bound = ["OPEN","SEMIOPEN","CLOSED"]
    ## case 2: (d_y,d_x) = (0, 1) is : direction left-to-right 
    ## direction left-to-right sequence not start /end at edge
    if x_start > 0 and x_end < len(board) - 1: # left edge is x =1
       # if there is no stone at start and end of the sequence, it is open sequence
       if (board[y_start][x_start -1 ] == " ") and (board[y_end][x_end + 1] == " "): #  open sequence with length col stones
           return  bound[0]
              # if there is a stone before the first stone of the sequence and no stone after the sequence, it is semi-open
       elif (board[y_start][x_start - 1] != " " ) and (board[y_end][x_end + 1] == " "):
           return  bound[1] 
       # if no stone before the first stone of sequence, and there is a stone after the last stone of sequence , it is semi-open
       elif (board[y_start][x_start - 1] == " ") and (board[y_end][x_end + 1] != " "):
           return  bound[1] 
       else:
           return  bound[2]   # closed or no sequence
   ##### direction left-to-right sequence start at left edge of the board####
    elif x_start == 0: # start at edge x = 1, left edge of the board
       # if there is a stone after the last stone of the sequence
       if board[y_end][x_end + 1] != " " :
          return  bound[2]   # closed sequence
       else:
          return  bound[1]   # semi_open sequence  
   ##### direction left-to-right sequence end at right edge of the board####
    elif x_end == len (board) -1: # end at right edge
       # if there is a stone  before to first element of the sequence
       if board[y_start][x_start -1] != " " :
          return  bound[2]   # closed sequence
       else:
          return  bound[1]   # semi_open sequence 

##############################################################
def is_bounded_1_1(board, y_end, x_end, length, d_y, d_x):
    y_start = y_end - d_y * (length -1)
    x_start = x_end - d_x * (length-1)
    bound = ["OPEN","SEMIOPEN","CLOSED"]
    ## case 3: (d_y,d_x) = (1, 1) is : direction upper-left-to-lower-right
    ## direction upper-left-to-lower-right sequence not start /end at edge
    if (x_start > 0 and y_start >= 1) and ( x_end < len(board) - 1 and y_end < len(board) - 1):
      # if there is no stone at start and end of the sequence, it is open sequence
       if (board[y_start-1][x_start -1 ] == " ") and (board[y_end + 1][x_end + 1] == " "): #  open sequence with length col stones
          return  bound[0]
      # if there is a stone before the first stone of sequence and no stone after the sequence, it is semi-open
       elif (board[y_start-1][x_start-1] != " ") and (board[y_end+1][x_end+1] == " "):
          return bound[1] 
      # if no stone before the first stone, and there is a stone after the last stone , it is semi-open
       elif (board[y_start-1][x_start - 1] == " ") and (board[y_end+1][x_end + 1] != " "):
          return bound[1] 
       else:
          return bound[2]   # closed or no sequence
    ## direction  upper-left-to-lower-right sequence start at left or top edge of the board####   
    elif x_start == 0 or y_start == 0: # start at left or top edgeof the board
      # if there is a stone  after the last stone of the sequence
       if ((y_end < len(board) - 1) and x_end < len(board) - 1) and  board[y_end+1][x_end + 1] != " ":
          return bound[2]   # closed sequence
      # if the end of the sequence is at bottom edge
       elif y_end == len(board) - 1 or x_end == len(board) - 1:
          return bound[2]   # closed sequence
       else:
          return bound[1]   # semi_open sequence 
  ## direction  upper-left-to-lower-right sequence stop at right or bottom edge of the board####   
    elif x_end == len(board) - 1 or y_end == len(board) - 1: # stop at left or bottom edgeof the board  
      # if there is a stone before the first stone of sequence 
       if board[y_start-1][x_start - 1] != " " :
          return bound[2]   # closed sequence
       else:
          return bound[1]   # semi_open sequence 

#####################################################################
def is_bounded_1m1(board, y_end, x_end, length, d_y, d_x):
    y_start = y_end - d_y * (length -1)
    x_start = x_end - d_x * (length-1)
    bound = ["OPEN","SEMIOPEN","CLOSED"]
   ## case 4: (d_y,d_x) = (1,-1) is : direction upper-right-to-lower-left 
   ## direction upper-right-to-lower-left sequence not start /end at edge
    if (x_start < len(board) -1 and y_start >= 1) and ( x_end >=1 and y_end < len(board) - 1): 
      # if there is no stone at start and end of the sequence, it is open sequence
       if (board[y_start-1][x_start +1 ] == " ") and (board[y_end + 1][x_end - 1] == " "): #  open sequence with length col stones
           return bound[0]
      # if there is a stone before the first stone of sequence and no stone after the sequence, it is semi-open
       elif (board[y_start-1][x_start+1] != " ") and (board[y_end+1][x_end-1] == " "):
           return bound[1] 
      # if no stone before the first stone, and there is a stone after the last checked stone , it is semi-open
       elif (board[y_start-1][x_start + 1] == " ") and (board[y_end+1][x_end - 1] != " "):
           return bound[1] 
       else:
           return bound[2]   # closed or no sequence   
   ## direction  upper-right-to-lower-left sequence start at right or top edge of the board#### 
    elif (x_start == len(board) -1) or (y_start == 0) : # start at righgt or top edge  
      # if there is a stone with different colour after the last stone of the sequence
       if (x_end==0 or y_end==len(board)-1) or (board[y_end+1][x_end - 1] != " "):
          return bound[0]   # closed sequence 
      # if the end of the sequence is at bottom edge
       else:
          return bound[1]   # semi-open sequence 

   ##### direction  upper-right-to-lower-left sequence stop at left or bottom edge of the board####
    elif (x_end == 0) or (y_end == len(board)-1) : # stop at left or bottom edge 
      # if there is a stone before the first stone of sequence with different colour
       if board[y_start-1][x_start + 1] != " ":
          return bound[2]   # closed sequence
       else:
          return bound[1]   # semi_open sequence 

###########################################################




# param ( board, col, y_start, x_start, length, d_y, d_x) 
# (d_y,d_x) = (1, 0) is : direction top-to-bottom
# max length 4, min length 2
def detect_row_1_0(board, col, y_start, x_start, length, d_y, d_x):
    #print("detect_row_1_0(board, col, y_start, x_start, length, d_y, d_x)")
    rowtuple =(1,1)
    realLength = 0
    y_end = y_start + d_y * (length -1)
    x_end = x_start + d_x * (length-1)
    
    ## case 1: (d_y,d_x) = (1, 0) is : direction top-to-bottom
    ## if direction top-to-bottom sequence start at top edge
    if y_start == 0: # start at top row
        for i in range (1,length):
            if board[y_start + i][x_start] != col:
               rowtuple =(0,0)   # no sequence
               break
        if rowtuple != (0,0): # sequence exist
           if board[y_end+1][x_end] == " ":
              rowtuple =(0,1)   # semi-open sequence  
           else:
              rowtuple =(0,0)   # closed sequence    
           
    ## direction top-to-bottom sequence end at bottom row
    elif y_end == len(board) -1: # end at bottom row
        for i in range (1, length):
            if board[y_start + i][x_start] != col:
               rowtuple =(0,0)   # no sequence
               break
        if rowtuple != (0,0): # sequence exist
            if board[y_start-1][x_start] == " ":
              rowtuple =(0,1)   # semi-open sequence 
            else:
              rowtuple =(0,0)   # closed sequence   
    
     ## direction top-to-bottom sequence not start / end at top / bottom edge
    elif y_start >= 1 and y_end < len(board) - 1:
        for i in range (1, length):
            if board[y_start + i][x_start] != col:
               rowtuple =(0,0)   # no sequence
               break  
        if rowtuple != (0,0): # sequence may exist
           # if no stone before and after the first and last stone of the sequence
           if (board[y_start-1][x_start] == " ") and (board[y_end+1][x_start] == " "): #  open sequence with length col stones
              rowtuple =(1,0)
           # if there is a stone before the first stone of sequence with different colour and no stone after the sequence, it is semi-open
           elif (board[y_start-1][x_start] != " " and board[y_start-1][x_start] != col) and (board[y_end+1][x_end] == " "):
              rowtuple =(0,1)
            # if there is a stone after the last stone of the sequence with different colour , it is semi-open
           elif (board[y_start-1][x_start] == " ") and (board[y_end+1][x_end] != " " and board[y_end+1][x_end] != col): 
              rowtuple =(0,1) 
           else: 
              rowtuple =(0,0) 
    #print("rowtuple_1_0",rowtuple)
    return rowtuple

##################################
# param ( board, col, y_start, x_start, length, d_y, d_x) ##(d_y,d_x) = (0, 1) is : direction left-to-right
def detect_row_0_1(board, col, y_start, x_start, length, d_y, d_x):
    #print("detect_row_0_1(board, col, y_start, x_start, length, d_y, d_x)")
    rowtuple =(1,1)
    y_end = y_start + d_y * (length -1)
    x_end = x_start + d_x * (length-1)
    reallength = 0

    ## if direction left-to-right sequence start at left edge
    # start at edge x = 1, left edge of the board
    if  x_start == 0: #  x = 1, left edge of the board
        for i in range (1,length):
            if board[y_start][x_start + i] != col:
               rowtuple =(0,0)   # no sequence
               break
        if rowtuple != (0,0): # sequence may exist
           if board[y_end][x_end + 1] == " ":
              rowtuple =(0,1)   # semi-open sequence  
           else:
              rowtuple =(0,0)   # closed or no sequence    
           
    ## direction left-to-right sequence end at right edge
    elif x_end == len (board) -1: # end at right edge
        for i in range (1, length):
            if board[y_start][x_start + 1] != col:
               rowtuple =(0,0)   # no sequence
               break
        if rowtuple != (0,0): # sequence may exist
            if board[y_start][x_start-1] == " ":
              rowtuple =(0,1)   # semi-open sequence 
            else:
              rowtuple =(0,0)   # closed sequence   

    # direction left-to-right sequence not start / end at left / right edge
    elif x_start > 0 and x_end < len(board) - 1: # left edge is x =1
        for i in range (1, length):
            if board[y_start][x_start + 1] != col:
               rowtuple =(0,0)   # no sequence
               break
        if rowtuple != (0,0): # sequence may exist
           # if there is no stone at start and end of the sequence, it is open sequence
           if (board[y_start][x_start -1 ] == " ") and (board[y_end][x_end + 1] == " "): #  open sequence with length col stones
              rowtuple =(1,0)
               # if there is a stone before the first stone of the sequence with different colour and no stone after the sequence, it is semi-open
           elif (board[y_start][x_start - 1] != " " and board[y_start][x_start-1] != col) and (board[y_end][x_end + 1] == " "):
              rowtuple =(0,1) 
              # if no stone before the first stone of sequence, and there is a stone after the last stone of sequence with different colour , it is semi-open
           elif (board[y_start][x_start - 1] == " ") and (board[y_end][x_end + 1] != " " and board[y_end][x_end + 1] != col):
              rowtuple =(0,1) 
           else:
              rowtuple =(0,0)   # closed or no sequence
    #print("rowtuple_0_1",rowtuple)
    return rowtuple          
##############################################################################          

# param ( board, col, y_start, x_start, length, d_y, d_x) ##(d_y,d_x) = (1, 1) is : direction upper-left-to-lower-right
def detect_row_1_1(board, col, y_start, x_start, length, d_y, d_x):
    #print("detect_row_1_1(board, col, y_start, x_start, length, d_y, d_x)")
    rowtuple =(1,1)
    y_end = y_start + d_y * (length -1)
    x_end = x_start + d_x * (length-1)
    realLength = 0
    ## if direction upper-left-to-lower-right sequence start at left or top edge
    # start at edge x = 1, left edge of the board
    if  x_start == 0 or y_start == 0: 
        for i in range (1,length):
            if board[y_start + i][x_start + i] != col:
               rowtuple =(0,0)   # no sequence
               break
        if rowtuple != (0,0): # sequence may exist
           if board[y_end + 1][x_end + 1] == " ":
              rowtuple =(0,1)   # semi-open sequence  
           else:
              rowtuple =(0,0)   # closed or no sequence   

    # direction  upper-left-to-lower-right sequence end at right or bottom edge of the board
    elif x_end == len(board) - 1 or y_end == len(board) - 1: 
        for i in range (1,length):
           if board[y_start + i][x_start + i] != col:
              rowtuple =(0,0)   # no sequence
              break
        if rowtuple != (0,0): # sequence may exist
           if board[y_start - i][x_start - i] == " ":
              rowtuple =(0,1)   # semi-open sequence
           else:
              rowtuple =(0,0)   # closed or no sequence  

    # direction upper-left-to-lower-right sequence not start /end at edge
    elif (x_start > 0 and y_start >= 1) and ( x_end < len(board) - 1 and y_end < len(board) - 1):  
        for i in range (1,length):
           if board[y_start + i][x_start + i] != col:
              rowtuple =(0,0)   # no sequence
              break
        if rowtuple != (0,0): # sequence may exist
           # if there is no stone at start and end of the sequence, it is open sequence
           if (board[y_start-1][x_start -1 ] == " ") and (board[y_end + 1][x_end + 1] == " "): 
              rowtuple =(1,0)
           # if there is a stone before the first stone of sequence with different colour and no stone after the sequence, it is semi-open
           elif (board[y_start-1][x_start-1] != " " and board[y_start-1][x_start-1] != col) and (board[y_end+1][x_end+1] == " "):
              rowtuple =(0,1) 
           # if no stone before the first stone, and there is a stone after the last checked stone with different colour , it is semi-open
           elif (board[y_start-1][x_start - 1] == " ") and (board[y_end+1][x_end + 1] != " " and board[y_end+1][x_end + 1] != col):
              rowtuple =(0,1) 
           else:
              rowtuple =(0,0)   # closed or no sequence
    #print("rowtuple_1_1",rowtuple)
    return rowtuple          
#############################################################
      
# param ( board, col, y_start, x_start, length, d_y, d_x) ##(d_y,d_x) = (1, -1) is : direction upper-right-to-lower-left  
def detect_row_1m1(board, col, y_start, x_start, length, d_y, d_x):
    #print("detect_row_1m1(board, col, y_start, x_start, length, d_y, d_x)")
    rowtuple =(1,1)
    y_end = y_start + d_y * (length -1)
    x_end = x_start + d_x * (length-1)  
    realLength = 0  
    ## if direction upper-right-to-lower-left sequence start at right or top edge
    # start at edge x = 1, left edge of the board
    if (x_start == len(board) -1) or (y_start == 0) : 
        for i in range (1,length):
           if board[y_start + i][x_start - i] != col:
              rowtuple =(0,0)   # no sequence
              break
        if rowtuple != (0,0): # sequence may exist
           if board[y_end + 1][x_end - 1] == " ":
              rowtuple =(0,1)   # semi-open sequence  
           else:
              rowtuple =(0,0)   # closed or no sequence   
   # direction  upper-right-to-lower-left sequence stop at left or bottom edge of the board
    elif (x_end == 0) or (y_end == len(board)-1) :
        for i in range (1,length):
           if board[y_start + i][x_start - i] != col:
              rowtuple =(0,0)   # no sequence
              break
        if rowtuple != (0,0): # sequence may exist
           if board[y_start-1][x_start + 1] == " ":
              rowtuple =(0,1)   # semi-open sequence   
           else:
              rowtuple =(0,0)   # closed or no sequence 
   # direction upper-right-to-lower-left sequence not start /end at edge
    elif (x_start < len(board) -1 and y_start >= 1) and ( x_end >=0 and y_end < len(board) - 1):
        for i in range (1,length):
           if board[y_start + i][x_start - i] != col:
              rowtuple =(0,0)   # no sequence
              break
        if rowtuple != (0,0): # sequence may exist
           # if there is no stone at start and end of the sequence, it is open sequence
           if (board[y_start-1][x_start +1 ] == " ") and (board[y_end + 1][x_end - 1] == " "):
              rowtuple =(1,0)   # open sequence 
           # if there is a stone before the first stone of sequence and no stone after the sequence, it is semi-open
           elif (board[y_start-1][x_start+1] != " ") and (board[y_end+1][x_end-1] == " "):
              rowtuple =(0,1) 
           # if no stone before the first stone, and there is a stone after the sequence , it is semi-open
           elif (board[y_start-1][x_start + 1] == " ") and (board[y_end+1][x_end - 1] != " " ):
              rowtuple =(0,1)  
           else:
               rowtuple =(0,0) # closed or no sequence  
    #print("rowtuple_1m1",rowtuple)
    return rowtuple
###########################################################################################


def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board

def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))

def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x

def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    print("open_b[5]:",open_b[5])
    print("semi_open_b[5]:",semi_open_b[5])
    print("open_w[5]:",semi_open_w[5])
    print("semi_open_w[5]:",semi_open_w[5])
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
   
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        
        else:
            move_y, move_x = search_max(board)
           
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
            
        
        
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



# detect_row(board, col, y_start, x_start, length, d_y, d_x)
def test_detect_rowt_1_0():
   print("====================")
   print("Test detect_row_1_0(board, col, y_start, x_start, length, d_y, d_x) d_y=1,d_x=0")
   board1 = make_empty_board(8)
   print("board length:", len(board1))
   #board, start_y, start_x, d_y, d_x, length, col
   put_seq_on_board(board1, 2, 2, 1, 0, 3, "w")
   print_board(board1)
  
   #board, col, y_start, x_start, length, d_y, d_x
   #open_seq_coungt, semi_open_seq_count = detect_row(board1, "w", 5, 2, 3, 1, 0)
   # board, col, y_start, x_start, length, d_y, d_x
   a = detect_row(board1, "w", 2, 2, 3, 1, 0) 
   print(a)
   if(a==(1,0)):
     print("Test (1, 0) is : direction top-to-bottom , start at (2,2) open sequence success") 
   print("====================")

   # detect_row(board, col, y_start, x_start, length, d_y, d_x)
def test_detect_rowt_0_1():
   print("====================")

   print("Test detect_row(board, col, y_start, x_start, length, d_y, d_x) d_y=0,d_x=1")
   board1 = make_empty_board(8)
   print("board length:", len(board1))
   #board, start_y, start_x, d_y, d_x, length, col
   put_seq_on_board(board1, 2, 2, 0, 1, 1, "w")
   put_seq_on_board(board1, 4, 4, 0, 1, 1, "b")
   print_board(board1)
  
   #board, col, y_start, x_start, length, d_y, d_x
   #open_seq_coungt, semi_open_seq_count = detect_row(board1, "w", 5, 2, 3, 1, 0)
   # board, col, y_start, x_start, length, d_y, d_x
   a = detect_row(board1, "b", 2, 2, 4, 0, 1) 
   print(a)
   if(a==(1,0)):
     print("Test (0, 1) is : direction  left-to-right , start at (2,2) open sequence success")     
   print("====================")

  # detect_row(board, col, y_start, x_start, length, d_y, d_x)
def test_detect_rowt_1_1():
   print("====================")
   print("Test detect_row(board, col, y_start, x_start, length, d_y, d_x) d_y=1,d_x=1")
   board1 = make_empty_board(8)
   print("board length:", len(board1))
   #board, start_y, start_x, d_y, d_x, length, col
   put_seq_on_board(board1, 2, 2, 1, 1, 3, "w")
   print_board(board1)
  
   #board, col, y_start, x_start, length, d_y, d_x
   #open_seq_coungt, semi_open_seq_count = detect_row(board1, "w", 5, 2, 3, 1, 0)
   # board, col, y_start, x_start, length, d_y, d_x
   a = detect_row(board1, "w", 2, 2, 3, 1, 1) 
   print(a)
   if(a==(1,0)):
     print("Test (1, 1) is : direction upper-left-to-lower-right , start at (2,2) open sequence success")         
   print("====================")

   # detect_row(board, col, y_start, x_start, length, d_y, d_x)
def test_detect_rowt_1m1():
   print("====================")
   print("Test detect_row(board, col, y_start, x_start, length, d_y, d_x) d_y=1,d_x=-1")
   board1 = make_empty_board(8)
   print("board length:", len(board1))
   #board, start_y, start_x, d_y, d_x, length, col
   put_seq_on_board(board1, 1, 5, 1, -1, 3, "w")
   print_board(board1)
  
   #board, col, y_start, x_start, length, d_y, d_x
   #open_seq_coungt, semi_open_seq_count = detect_row(board1, "w", 5, 2, 3, 1, 0)
   # board, col, y_start, x_start, length, d_y, d_x
   a = detect_row(board1, "w", 1, 5, 3, 1, -1) 
   print(a)
   if(a==(1,0)):
     print("Test (1, -1) is : direction upper-right-to-lower-left , start at (1,5) open sequence success") 
   print("====================")

#def detect_rows(board, col, length):
def test_detect_row1():
   print("Test detect_rows(board, col, length) d_y=1,d_x=0")
   board1 = make_empty_board(8)
   print("board length:", len(board1))
   #board, start_y, start_x, d_y, d_x, length, col
   put_seq_on_board(board1, 2, 2, 1, 0, 3, "w")
   print_board(board1)
  
   #board, col, y_start, x_start, length, d_y, d_x
   #open_seq_coungt, semi_open_seq_count = detect_row(board1, "w", 5, 2, 3, 1, 0)
   # board, col, y_start, x_start, length, d_y, d_x
   a = detect_row(board1, "w", 2, 2, 3, 1, 0) 
   print(a)
   if(a==(1,0)):
     print("Test (1, 0) is : direction  top-to-bottom , start at (2,2) open sequence success") 
   
   print("Test detect_rows(board1, w, 3)") 
   b = detect_rows(board1, "w", 3)
   print(b)
   if b==(1,0):
     print("Test detect_rows(board1, w, 3) success") 
   print("====================")

   #def detect_rows(board, col, length):
def test_detect_row2():
   print("Test detect_rows(board, col, length) d_y=0,d_x=1")
   board1 = make_empty_board(8)
   print("board length:", len(board1))

   #board, start_y, start_x, d_y, d_x, length, col
   put_seq_on_board(board1, 1, 3, 0, 1, 3, "w")
   print_board(board1)
  
   #board, col, y_start, x_start, length, d_y, d_x
   #open_seq_coungt, semi_open_seq_count = detect_row(board1, "w", 5, 2, 3, 1, 0)
   # board, col, y_start, x_start, length, d_y, d_x
   a = detect_row(board1, "w", 1, 3, 3, 0, 1) 
   print(a)
   if(a==(1,0)):
     print("Test (0, 1) is : direction  left-to-right , start at (1,3) open sequence success") 

   print("Test detect_rows(board1, w, 3)") 
   b = detect_rows(board1, "w", 3)
   print(b)
   if b==(1,0):
     print("Test detect_rows(board1, w, 3) success") 
   print("====================")

def test_detect_row3():
   print("Test detect_rows(board, col, length) d_y=1,d_x=1")
   board1 = make_empty_board(8)
   print("board length:", len(board1))

   #board, start_y, start_x, d_y, d_x, length, col
   put_seq_on_board(board1, 2, 2, 1, 1, 3, "w")
   print_board(board1)
  
   #board, col, y_start, x_start, length, d_y, d_x
   #open_seq_coungt, semi_open_seq_count = detect_row(board1, "w", 5, 2, 3, 1, 0)
   # board, col, y_start, x_start, length, d_y, d_x
   a = detect_row(board1, "w", 2, 2, 3, 1, 1) 
   print(a)
   if(a==(1,0)):
     print("Test (1, 1) is : direction upper-left-to-lower-right , start at (2,2) open sequence success") 

   print("Test detect_rows(board1, w, 3)") 
   b = detect_rows(board1, "w", 3)
   print(b)
   if b==(1,0):
     print("Test detect_rows(board1, w, 3) success") 
   print("====================")
def test_detect_row4():
   print("Test detect_rows(board, col, length) d_y=1,d_x=1")
   board1 = make_empty_board(8)
   print("board length:", len(board1))

   #board, start_y, start_x, d_y, d_x, length, col
   put_seq_on_board(board1, 1, 5, 1, -1, 3, "w")
   print_board(board1)
   # board, col, y_start, x_start, length, d_y, d_x
   a = detect_row(board1, "w", 1, 5, 3, 1, -1) 
   print(a)
   if(a==(1,0)):
     print("Test (1, -1) is : direction upper-right-to-lower-left , start at (1,5) open sequence success")

   print("Test detect_rows(board1, w, 3)") 
   b = detect_rows(board1, "w", 3)
   print(b)
   if b==(1,0):
     print("Test detect_rows(board1, w, 3) success") 
   print("====================") 

def test_detect_row5():
   print("Test detect_rows(board, col, length) d_y=1,d_x=1")
   board1 = make_empty_board(8)
   print("board length:", len(board1))

   #board, start_y, start_x, d_y, d_x, length, col
   put_seq_on_board(board1, 1, 5, 1, -1, 3, "w")
   put_seq_on_board(board1, 2, 2, 1, 0, 3, "w")
   put_seq_on_board(board1, 6, 2, 0, 1, 3, "w")
   print_board(board1)
   # board, col, y_start, x_start, length, d_y, d_x
   a = detect_row(board1, "w", 1, 5, 3, 1, -1) 
   print(a)   

   print("Test detect_rows(board1, w, 3)") 
   b = detect_rows(board1, "w", 4)
   c = detect_rows(board1, "w", 3)
   d = detect_rows(board1, "w", 2)
   print(b)
   print(c)
   print(d)
   
   print("====================") 
###
def test_is_empty():
    print("======test_is_empty=======")

    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")
    print("====================")
###
def test_detect_rows():
    print("\n====== test_detect_rows =======\n")
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 5; col = 'w' #  (d_y,d_x) = (1, 0) is : direction top-to-bottom
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_detect_row():
    print("\n====== test_detect_row =======\n")
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3 ## (d_y,d_x) = (1, 0) is : direction top-to-bottom
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", y,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_is_bounded():
    print("\n====== test_is_bounded =======\n")
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")

def test_search_max():
    MAX_SCORE = 100000
    print("\n====== test_search_max =======\n")
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    print ("search_max:", search_max(board))
    if search_max(board)== (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def test_score():
     print("\n====== test_score =======\n")

     board = make_empty_board(8)
     x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
     put_seq_on_board(board, y, x, d_y, d_x, length, col)
     x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
     put_seq_on_board(board, y, x, d_y, d_x, length, col)
     print_board(board)
     b = score(board)
     print("score:", b)

def easy_testset_for_main_functions():
    print("\n=== easy_testset_for_main_functions ====\n")
    test_is_empty()
    test_is_bounded()
    test_detect_rows()
    test_detect_row()
    test_search_max()

def some_tests():
    print("\n========some_tests()=========\n")
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    print("=================================")
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    print("=================================")
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);

    analysis(board);
    print("=================================")
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0



#easy_testset_for_main_functions()
#some_tests()

if __name__ == '__main__':
    play_gomoku(8)