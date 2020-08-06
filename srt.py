from datetime import timedelta, datetime
from typing import List


def get_srt_section_ids(text: str) -> List[int]:
    """Parse a caption (srt) text passed in and return a
       list of section numbers ordered descending by
       highest speech speed
       (= ratio of "time past:characters spoken")

       e.g. this section:

       1
       00:00:00,000 --> 00:00:01,000
       let's code

       (10 chars in 1 second)

       has a higher ratio then:

       2
       00:00:00,000 --> 00:00:03,000
       code

       (4 chars in 3 seconds)

       You can ignore milliseconds for this exercise.
    """
    chunked_text = [line for line in text.splitlines() if line != ""]
    chunked_text = [chunked_text[i:i+3] for i in range(0, len(chunked_text), 3)]
    
    time_dict = {}
    
    for chunk in chunked_text:
        start, end = chunk[1].split(" --> ")
        start, end = datetime.strptime(start, "%X,%f").replace(microsecond=0), datetime.strptime(end, "%X,%f").replace(microsecond=0)
        length = len(chunk[2])
        
        time_dict[chunk[0]] = length/(end - start).seconds
        
    ordered = sorted(time_dict.items(), key = lambda x: x[1], reverse = True)
    
    return [int(item[0]) for item in ordered]
    pass