from datetime import datetime, timedelta, date

TODAY = date(2018, 11, 12)


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""
    dates = []
    
    for line in data.splitlines():
        if line[6:8] == "20":
            dates.append(datetime.strptime(line[6:16], '%Y-%m-%d').date())
            
    return list(set(dates))
    pass


def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    streak_counter = 0
    max_streak = 0
    
    sorted_dates = sorted(dates)
    
    if TODAY not in sorted_dates and TODAY != (sorted_dates[-1] + timedelta(days=1)):
        return max_streak
    
    for i in range(1, len(sorted_dates)):
        if (sorted_dates[i] - sorted_dates[i-1]).days == 1:
            streak_counter += 1
        else:
            max_streak = streak_counter
            streak_counter = 0
    
    max_streak = max(max_streak, streak_counter+1)
    
    return max_streak
    pass