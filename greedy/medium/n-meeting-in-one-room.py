"""
Problem description: 
---------

"""


class Meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos


def n_meeting_in_one_room(starts, ends, n):
    # Time complexity: O(n log n)
    meet = [Meeting(starts[i], ends[i], i + 1) for i in range(n)]
    sorted(meet, key=lambda x: (x.end, x.pos))
    answer = [meet[0].pos]
    limit = meet[0].end
    for i in range(n):
        if meet[i].start > limit:
            limit = meet[i].end
            answer.append(meet[i].pos)

    return answer


if __name__ == '__main__':
    print(n_meeting_in_one_room([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9], 6))
