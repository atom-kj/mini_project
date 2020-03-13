def days_until_launch(current_day, launch_day):
    """"Returns the days left before launch.
    
    current_day (int) - current day in integer
    launch_day (int) - launch day in integer
    """
    if launch_day < current_day: # for negative answer
        launch_day = current_day
    return launch_day - current_day