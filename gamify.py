"""
Project#1 - Gamification of Exercise

"""

def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''

    global cur_hedons, cur_health, num_of_star, total_activity_time_span

    global cur_time
    global last_activity, last_activity_duration

    global last_finished
    global bored_with_stars
    global is_tired
    global latest_star_time

    global cur_star, cur_star_activity

    cur_hedons = 0
    cur_health = 0
    num_of_star = 0
    total_activity_time_span = 0
    
    is_tired = False
    latest_star_time = 0

    cur_star = None
    cur_star_activity = None

    bored_with_stars = False

    last_activity = None
    last_activity_duration = 0

    cur_time = 0

    last_finished = -1000




def star_can_be_taken(activity):
    global bored_with_stars,cur_star_activity

    if  bored_with_stars is True :
        return False
    elif cur_star_activity != activity:
        return False
    elif latest_star_time != total_activity_time_span: #user didn't take the star right away
        return False
    else:
        return True


def perform_activity(activity, duration):
    global cur_hedons, cur_health, is_tired
    global last_activity, last_activity_duration, total_activity_time_span
    global latest_star_time, cur_star_activity, cur_star

    is_tired = is_user_tired(activity)
    """below print for debug purpose only
    print("===current activity info===")
    print("activity:", activity, ", duration:", duration,", is user tired:", is_tired,)
    print("latest_star_time:", latest_star_time, ", total_activity_time_span so far:", total_activity_time_span)
    print("===end current activity info===")
    """
    #======calculate health point below======
    if activity == "running" and last_activity != "running":
        if duration <= 180: 
            cur_health = cur_health + duration * 3
        else:cur_health = cur_health + 180 * 3 + (duration - 180) * 1

    elif activity == "running" and last_activity == "running":
        if last_activity_duration + duration > 180 :
            cur_health = cur_health + (180 - last_activity_duration)  * 3 + (duration + last_activity_duration - 180) * 1
        else:
            cur_health = cur_health + duration * 3  
    
    elif activity == "textbooks":
        cur_health = cur_health + duration * 2

    else:
    #resting, no point & hedons change      
      cur_health = cur_health

    # =======calculate hedons below=========
    # if no star taken and is not tired
    # if not tired, running gives 2 hedons per min for the first 10 mins, and
    # -2 hedons per min for every min after the first 10
    if (cur_star_activity is None or star_can_be_taken(activity) is False) and is_tired is False:
         if activity == "running":
            if duration - 10 > 0:
                cur_hedons = cur_hedons + 10 *2 + (duration - 10) * (-2 )
            else:
                cur_hedons = cur_hedons + 10 * 2
         elif activity == "textbooks":
            if duration - 20 > 0:
                cur_hedons = cur_hedons + 20 * 1 + (duration - 20) * (-1 )
            else:
                cur_hedons = cur_hedons + 20 * 1
    # if no star taken and is tired give -2 hedons per min          
    elif (cur_star_activity is None or star_can_be_taken(activity) is False) and is_tired is True:
        if activity == "running" or activity == "textbooks":
            cur_hedons = cur_hedons + duration * (-2)            
    # if star was offered and can be taken and user is not tired
    elif star_can_be_taken(activity) is True and is_tired is False:
        if activity == "running":
                # user take the star, get 3 additional hedons per min for at most 10 mins
                # if not tired, running gives 2 hedons per min for the first 10 mins, and
                # -2 hedons per min for every min after the first 10
            if duration - 10 > 0:                
                cur_hedons = cur_hedons + 10 * (3 +2) + (duration - 10) * (-2 )
            else:
                cur_hedons = cur_hedons + duration * (3 +2)

        elif activity == "textbooks":
                # user take the star, get 3 additional hedons per min for at most 10 mins
                # if not tired, textbooks gives 1 hedons per min for the first 20 mins, and
                # -1 hedons per min for every min after the first 20
            if duration > 10 and duration <= 20:
                cur_hedons = cur_hedons + 10 * 3 + duration * 1
            elif duration - 20 > 0:
                cur_hedons = cur_hedons + 10 * 3 + 20 * 1 + (duration - 20) * (-1)
            else:
                # duration <= 10
                cur_hedons = cur_hedons + duration * (3 +1)

     # if star was offered and can be taken and user is tired
    elif star_can_be_taken(activity) is True and is_tired is True:
        #
        if activity == "running" or activity == "textbooks":
            if(duration <= 10):
                cur_hedons = cur_hedons + duration * (3-2)  
            else:
                cur_hedons = cur_hedons + 10 * (3-2) + (duration-10) * (-2)
        
    total_activity_time_span = total_activity_time_span + duration
    last_activity = activity
    last_activity_duration = duration


def get_cur_hedons():
    return cur_hedons

def get_cur_health():
    return cur_health

def offer_star(activity):
    global bored_with_stars, total_activity_time_span,num_of_star 
    global cur_star, cur_star_activity, latest_star_time
    num_of_star = num_of_star + 1

    if total_activity_time_span < 120 and num_of_star == 3 :
        bored_with_stars = True

    cur_star_activity = activity
    latest_star_time = total_activity_time_span
    

def most_fun_activity_minute():
    #return the activity which would give the most hedons if person perform it for one minute at the current time
    global last_activity, is_tired, latest_star_time
    if latest_star_time == total_activity_time_span:
       return cur_star_activity
       
    elif   last_activity == "running" or last_activity == "textbooks":
        return "resting"
    else : #first activity
        return "running"
   

def is_user_tired(activity):
    global last_activity_duration, last_activity, is_tired
    if last_activity is None:
        is_tired = False
        return False
    elif  activity == "resting":
        is_tired = False
        return False
    elif (activity == "running" or activity == "textbooks") and  (last_activity == "resting" and last_activity_duration >= 120):
        is_tired = False
        return False
    else:
        is_tired = True
        return True

 ################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

def get_effective_minutes_left_hedons(activity):
    #Return the number of minutes during which the user will get the full
    #amount of hedons for activity activity
    
    pass

def get_effective_minutes_left_health(activity):
    pass

def estimate_hedons_delta(activity, duration):
    #Return the amount of hedons the user would get for performing activity
    #activity for duration minutes
    pass


def estimate_health_delta(activity, duration):
    pass

################################################################################

if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)
    print("current hedons:", get_cur_hedons())                     # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print("current health points:", get_cur_health())              # 90 = 30 * 3                          # Test 2
    print("most fun activity minute:", most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)
    offer_star("running")
    print("most fun activity minute:", most_fun_activity_minute())  # running                              # Test 4
    
    perform_activity("textbooks", 30)
    print("current health points:", get_cur_health())              # 150 = 90 + 30*2                      # Test 5
    print("current hedons:", get_cur_hedons())                     # -80 = -20 + 30 * (-2)                # Test 6
    
    offer_star("running")
    perform_activity("running", 20)
    print("current health points:", get_cur_health())              # 210 = 150 + 20 * 3                   # Test 7
    print("current hedons:",get_cur_hedons())                                        # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
   
    perform_activity("running", 170)
    print("current health points:", get_cur_health())              # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print("current hedons:", get_cur_hedons())                     # -430 = -90 + 170 * (-2)              # Test 10
   
