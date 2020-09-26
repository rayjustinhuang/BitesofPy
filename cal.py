from collections import defaultdict

def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    
    cal_list = []
       
    for line in calendar_output.splitlines():
        cal_list.append(line)
        
    print(cal_list)
    
    cal_dict = defaultdict(str)
    
    for j in range(2,len(cal_list)):
        for i in range(0,len(cal_list[1]),3):
            if cal_list[j][i:i+2] == "" or cal_list[j][i:i+2] == "  ":
                continue
            else:
                cal_dict[int(cal_list[j][i:i+2])] = cal_list[1][i:i+2]
    
    return cal_dict
    pass