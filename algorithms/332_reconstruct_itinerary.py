# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
#
# Note:
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
import copy


class Solution(object):

    def findItinerary(self, tickets):
        direction_dict = {}
        itinerary = []
        for from_, to_ in tickets:
            direction_dict.setdefault(from_.upper(), []).append(to_.upper())
        curr = "JFK"
        found, path = self.travel(direction_dict, curr)
        path.sort()
        itinerary.append(curr)
        itinerary.extend(path[0])
        return itinerary

    def travel(self, direction_dict, departure):
        if not direction_dict:
            return True, None
        elif departure not in direction_dict:
            return False, None
        else:
            return_list = None
            has_finished = False
            for index, destination in enumerate(direction_dict[departure]):
                new_direction_dict = copy.deepcopy(direction_dict)
                new_direction_dict[departure].pop(index)
                if not new_direction_dict[departure]:
                    del new_direction_dict[departure]
                finished, path = self.travel(new_direction_dict, destination)
                if finished:
                    has_finished = True
                    return_list = [] if return_list is None else return_list
                    if path is not None:
                        for p in path:
                            this_path = list()
                            this_path.append(destination)
                            this_path.extend(p)
                            return_list.append(this_path)
                    else:
                        this_path = list()
                        this_path.append(destination)
                        return_list.append(this_path)
            if has_finished:
                return True, return_list
            else:
                return False, None


a = Solution()
assert(a.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) == ["JFK", "MUC", "LHR", "SFO", "SJC"])
assert(a.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]) == ["JFK","ATL","JFK","SFO","ATL","SFO"])
assert(a.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]) == ["JFK","NRT","JFK","KUL"])
assert(a.findItinerary([["JFK","TPE"],["TPE","NRT"],["NRT","PVG"], ["PVG", "TPE"], ["TPE", "HKG"], ["HKG", "CDG"]])
                       == ["JFK","TPE","NRT","PVG","TPE","HKG","CDG"])