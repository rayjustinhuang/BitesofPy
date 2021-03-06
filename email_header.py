import re

EMAIL_HEADER = """Return-Path: <bounces+5555-7602-redacted-info>
...
Received: by 10.8.49.86 with SMTP id mf9.22328.51C1E5CDF
    Wed, 19 Jun 2013 17:09:33 +0000 (UTC)
Received: from NzI3MDQ (174.37.77.208-static.reverse.softlayer.com [174.37.77.208])
by mi22.sendgrid.net (SG) with HTTP id 13f5d69ac61.41fe.2cc1d0b
for <redacted-info>; Wed, 19 Jun 2013 12:09:33 -0500 (CST)
Content-Type: multipart/alternative;
boundary="===============8730907547464832727=="
MIME-Version: 1.0
From: redacted-address
To: redacted-address
Subject: A Test From SendGrid
Message-ID: <1371661773.974270694268263@mf9.sendgrid.net>
Date: Wed, 19 Jun 2013 17:09:33 +0000 (UTC)
X-SG-EID: P3IPuU2e1Ijn5xEegYUQ...
X-SendGrid-Contentd-ID: {"test_id":"1371661776"}"""  # noqa E501


def get_email_details(header: str) -> dict:
    """User re.search or re.match to capture the from, to, subject
       and date fields. Return the groupdict() of matching object, see:
       https://docs.python.org/3.7/library/re.html#re.Match.groupdict
       If not match, return None
    """
    from_regex = re.compile(r'From:\s([^\n]+)\n*?')
    to_regex = re.compile(r'To:\s([^\n]+)\n')
    subject_regex = re.compile(r'Subject:\s([^\n]+)\n')
    date_regex = re.compile(r'Date:\s([^\n]+)\n')
    
    try:
        from_part = re.search(from_regex, header).groups()[0]
        to_part = re.search(to_regex, header).groups()[0]
        subject_part = re.search(subject_regex, header).groups()[0]
        date_part = re.search(date_regex, header).groups()[0][:-12]
        
        result = {'from': from_part, 'to': to_part, 'subject': subject_part, 'date': date_part}
        
        return result
    
    except:
        return None
    pass