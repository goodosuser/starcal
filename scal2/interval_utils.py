# -*- coding: utf-8 -*-
#
# Copyright (C) 2010-2012 Saeed Rasooli <saeed.gnu@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/gpl.txt>.
# Also avalable in /usr/share/common-licenses/GPL on Debian systems
# or /usr/share/licenses/common/GPL3/license.txt on ArchLinux


overlaps = lambda a0, a1, b0, b1: \
    a0 <= b0 <  a1 or \
    a0 <  b1 <= a1 or \
    b0 <= a0 <  b1 or \
    b0 <  a1 <= b1

def simplifyNumList(nums, minCount=3):## nums must be sorted, minCount >= 2
    ranges = []
    tmp = []
    for n in nums:
        if tmp and n - tmp[-1] != 1:
            if len(tmp)>minCount:
                ranges.append((tmp[0], tmp[-1]))
            else:
                ranges += tmp
            tmp = []
        tmp.append(n)
    if tmp:
        if len(tmp)>minCount:
            ranges.append((tmp[0], tmp[-1]))
        else:
            ranges += tmp
    return ranges

def cleanTimeRangeList(lst):
    num = len(lst)
    i = 0
    while i < num-1:
        if lst[i][1] == lst[i+1][0]:
            lst[i] = (lst[i][0], lst[i+1][1])
            lst.pop(i+1)
            num -= 1
        else:
            i += 1

def intervalListBoundaries(lst):
    boundaries = set()
    for start, end in lst:
        boundaries.add(start)
        boundaries.add(end)
    return sorted(boundaries)


def intersectionOfTwoIntervalList(lst1, lst2):
    boundaries = intervalListBoundaries(lst1 + lst2)
    segmentsNum = len(boundaries) - 1
    segmentsContained = [[False, False] for i in range(segmentsNum)]
    for start, end in lst1:
        startIndex = boundaries.index(start)
        endIndex = boundaries.index(end)
        for i in range(startIndex, endIndex):
            segmentsContained[i][0] = True
    for start, end in lst2:
        startIndex = boundaries.index(start)
        endIndex = boundaries.index(end)
        for i in range(startIndex, endIndex):
            segmentsContained[i][1] = True
    result = []
    for i in range(segmentsNum):
        if segmentsContained[i][0] and segmentsContained[i][1]:
            result.append((boundaries[i], boundaries[i+1]))
    #cleanTimeRangeList(result)## not needed when both timeRangeList are clean!
    return result


########################################################################


def testIntersection():
    pprint.pprint(intersectionOfTwoIntervalList(
        [(0,1.5), (3,5), (7,9)],
        [(1,3.5), (4,7.5), (8,10)]
    ))

def testJdRanges():
    pprint.pprint(JdListOccurrence([1, 3, 4, 5, 7, 9, 10, 11, 12, 13, 14, 18]).calcJdRanges())

def testSimplifyNumList():
    pprint.pprint(simplifyNumList([1, 2, 3, 4, 5, 7, 9, 10, 14, 16, 17, 18, 19, 21, 22, 23, 24]))

if __name__=='__main__':
    import pprint
    #testIntersection()
    #testJdRanges()
    testSimplifyNumList()


