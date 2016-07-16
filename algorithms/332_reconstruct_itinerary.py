# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
#
# Note:
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
import collections


class Solution(object):
    def findItinerary(self, tickets):
        self.direction_dict = {}
        tickets.sort()
        for from_, to_ in tickets:
            dest_dict = self.direction_dict.setdefault(from_.upper(), collections.OrderedDict())
            dest_dict.setdefault(to_, 0)
            dest_dict[to_] += 1
        self.num_stops = len(tickets) + 1
        self.itinerary = ["JFK"]
        self.travel()
        return self.itinerary

    def travel(self):
        if self.num_stops == len(self.itinerary):
            return True
        elif self.itinerary[-1] not in self.direction_dict:
            return False
        else:
            depart = self.itinerary[-1]
            for dest, tickets_left in self.direction_dict[depart].items():
                if tickets_left:
                    self.itinerary.append(dest)
                    self.direction_dict[depart][dest] -= 1
                    if self.travel():
                        return True
                    self.itinerary = self.itinerary[:-1]
                    self.direction_dict[depart][dest] += 1
            return False
        pass


a = Solution()
assert(a.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) == ["JFK", "MUC", "LHR", "SFO", "SJC"])
assert(a.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]) == ["JFK","ATL","JFK","SFO","ATL","SFO"])
assert(a.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]) == ["JFK","NRT","JFK","KUL"])
assert(a.findItinerary([["JFK","TPE"],["TPE","NRT"],["NRT","PVG"], ["PVG", "TPE"], ["TPE", "HKG"], ["HKG", "CDG"]])
                       == ["JFK","TPE","NRT","PVG","TPE","HKG","CDG"])