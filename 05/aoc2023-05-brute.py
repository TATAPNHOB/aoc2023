with open('input') as f:
    lines = f.readlines()

seeds_range = []
seeds = []

maps = []
first = True

class Range:
    def __init__(self, source, range, destination = -1):
        self.source = source
        self.range = range
        self.destination = destination
    def getend(self):
        return self.source + self.range
    def setend(self, end):
        self.range = end - self.source
    def delend(self):
        pass

    def offset(self):
        if (self.destination == -1):
            return 0
        else:
            return self.destination - self.source

    end = property(getend, setend, delend)

    def __str__(self):
        if (self.destination == -1):
            return str(self.source) + " (" + str(self.range) + ") " + str(self.end)
        else:
            return str(self.source) + " (" + str(self.range) + ") " + str(self.end) + " [" + str(self.destination - self.source) + "]"

    def __eq__(self, other):
        if (isinstance(other, Range)):
            return self.source == other.source and self.range == other.range
        else:
            return False

import time

start = time.time()

for line in lines:
    line = line.replace('\n','')
    if (line.find("seeds") != -1):
        seeds_range = line.split(": ")[1].split(" ")
        for i in range(0, len(seeds_range), 2):
            seeds.append(Range(source = int(seeds_range[i]), range = int(seeds_range[i + 1])))       
    elif (line.find("map") != -1):
        if first:
            g_map = []
            first = False
        else:
            maps.append(g_map)
            g_map = []
    elif line != "":
        line = line.split(" ")
        g_map.append(Range(source=int(line[1]), destination= int(line[0]), range= int(line[2])))
maps.append(g_map)

locations = []
for seed in seeds:
   t = seed
   for m in maps:
       found = False
       for r in m:
           if t in range(r.source, r.end + 1):
               found = True
               t = t - r.source + r.destination
           if found:
               break
   locations.append(t)
print(min(locations))

# def in_range(n, r):
#     return n >= r.source and n <= r.source + r.range

# def are_overlapping(r1, r2):
#     return in_range(r1.source, r2) or in_range(r1.end, r2) or in_range(r2.source, r1) or in_range(r2.end, r1)

# def find_overlap(r1, r2):
#     source = max(r1.source, r2.source)
#     r = max(r1.end, r2.end)
#     if r <= source:
#         return None
#     return Range(source=source, range= r - source)

# def map_range(r1, r2):
#     #case 1: r2 is less and out of range
#     if r2.end < r1.source:
        
#         # print(r1, 'and', r2, 'do not overlap and r2 is less')
#         return {"mappable": None, "left": [r1]}
#     #case 2: r2 is more and out of range
#     elif r2.source > r1.end:
        
#         # print(r1, 'and', r2, 'do not overlap and r2 is more')
#         return {"mappable": None, "left": [r1]}
#     #case 3: r1 is in r2
#     elif in_range(r1.source, r2) and in_range(r1.end, r2):
        
#         # print(r1, 'and', r2, 'overlap and r1 is in r2')
#         return {"mappable": r1, "left": []}
#     #case 4: r2 is in r1
#     elif in_range(r2.source, r1) and in_range(r2.end, r1):
        
#         # print(r1, 'and', r2, 'overlap and r2 is in r1')
#         m = Range(source= r2.source, range= r2.range)
#         left = [Range(source= r1.source, range= m.source - r1.source - 1)]
#         left.append(Range(source= m.end + 1, range= r1.end - m.end - 1))
#         return {"mappable": m, "left": left}
#     #case 5: overlap to the left
#     elif in_range(r2.end, r1) and r2.source < r1.source:
        
#         # print(r1, 'and', r2, 'overlap in the left')
#         m = Range(source=r1.source, range=r2.end - r1.source)
#         left = [Range(source= m.end + 1, range= r1.end - m.end - 1)]
#         return {"mappable": m, "left": left}
#     #case 6: overlap to the right
#     elif in_range(r2.source, r1) and r2.end > r1.end:
        
#         # print(r1, 'and', r2, 'overlap in the right')
#         m = Range(source=r2.source, range=r1.end - r2.source)
#         left = [Range(source= r1.source, range= r1.range - m.range - 1)]
#         return {"mappable": m, "left": left}

# # for seed in seeds:
# #     ranges = [[seed, 0]]
# #     for i in range(len(maps)):
# #         current_ranges = list(map(lambda r: r[0], filter(lambda range: range[1] == i, ranges)))
# #         for seed_range in current_ranges:
# #             for r in maps[i]:
# #                 #check if ranges overlap
# #                 res = map_range(seed_range, r)
# #                 print(r, res)
# #                 if len(res["left"]) != 0:
# #                     for j in res["left"]:
# #                         if j not in current_ranges:
# #                             current_ranges.append([j, i])
# #                 if res["mappable"] != []:
# #                     ranges.append([res["mappable"], i+1])
# #         current_ranges = list(map(lambda r: r[0], filter(lambda range: range[1] == i, ranges)))
# #         if len(current_ranges) != 0:
# #             for q in current_ranges:
# #                 ranges.append([q, i+1])
# #         current_ranges.clear()

# ranges = []

# for seed in seeds:
#     ranges.append([seed, 0])
#     for layer in range(len(maps)):
#         # print('entered layer', layer)
#         left = []
#         current_ranges = list(map(lambda r: r[0], filter(lambda range: range[1] == layer, ranges)))
#         # print('current ranges:')
#         # for t in current_ranges:
#         #     print(t)
#         while len(current_ranges) != 0:
#             current_range = current_ranges.pop(0)
#             transformed = False
#             for r in maps[layer]:
#                 res = map_range(current_range, r)
#                 # print(res)
#                 # print()
#                 if res["mappable"] != None:
#                     transformed = True
#                     s = Range(res["mappable"].source + r.offset(), res["mappable"].range)
#                     if [s, layer+1] not in ranges:
#                         ranges.append([s, layer+1])
#                     for l in res["left"]:
#                         current_ranges.append(l)
#                     break
#             if (not transformed):
#                 if [current_range, layer+1] not in ranges:
#                     ranges.append([current_range, layer+1])

# lowest_loc = 9999999999999999999999999999999999999

# for i in range(len(ranges)):
#     # print(ranges[i][1], ranges[i][0])
#     if ranges[i][1] == 7:
#         print(ranges[i][0])
#         if ranges[i][0].source < lowest_loc:
#             lowest_loc = ranges[i][0].source

# end = time.time()

# print((end - start) * 1000, "ms")

# print(lowest_loc)