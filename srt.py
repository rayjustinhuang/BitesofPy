from datetime import timedelta
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
    
    
        
    print(chunked_text)
    pass

text1 = """
1
00:00:00,498 --> 00:00:02,827
Beautiful is better than ugly.

2
00:00:02,827 --> 00:00:06,383
Explicit is better than implicit.

3
00:00:06,383 --> 00:00:09,427
Simple is better than complex.
"""

get_srt_section_ids(text1)