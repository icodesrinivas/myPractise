"""
Message Spreading
There are N students in a class, each in possession of a different funny story.

They want to share funny stories with each other by sending electronic messages. Assume that a sender includes all the funny stories he or she knows at the time the message is sent and that a message may only have one addressee. What is the minimum number of messages they need to send to guarantee that every one of them gets all the funny stories?
Input:
2
Output:
2
Explanation:
Person 1 sends a message to
Person 2, Person 2 sends
message to Person 1.
A total of 2 messages are sent.
"""

def minimumMessages(N):
    return N + (N - 2)