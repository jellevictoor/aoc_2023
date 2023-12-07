import re
from dataclasses import dataclass

from functions import clean_lines


@dataclass
class Seed:
    seed_id: int


@dataclass
class SeedMap:
    name: str
    destination: [int]
    source: [int]

    def get_destination(self, id: int):
        found = False
        index = 0
        map_index = 0
        for source_range in self.source:
            if source_range[0] <= id < (source_range[0] + source_range[1]):
                found = True
                index = (id - source_range[0])
                break
            else:
                map_index += 1

        if found:
            return self.destination[map_index][0] + index
        else:
            return id


def solve(lines):
    seeds = [rnge.split(' ') for rnge in re.findall(r'(\d+ \d+)', lines[0])]
    name = ""
    seed_maps = []
    destination = list()
    source = list()
    for line in lines[1:]:
        split = line.split(' ')
        if re.match(r'.*\smap:', line):
            if name:
                seed_maps.append(SeedMap(name, destination, source))
                source = []
                destination = []
            name = split[0]
        if re.match(r'\d* \d* \d*', line):
            dest_start = int(split[0])
            source_start = int(split[1])
            length = int(split[2])
            destination.append([dest_start, length])
            source.append([source_start, length])
    seed_maps.append(SeedMap(name, destination, source))
    print(f"done parsing")
    result = []
    for seed_range in seeds:
        for seed in range(int(seed_range[0]), int(seed_range[0])+int(seed_range[1])):
            next = seed
            for seed_map in seed_maps:
                next = seed_map.get_destination(next)
            result.append(next)
    return min(result)


def main():
    with open('input/day5.txt', 'r') as f:
        return solve(clean_lines(f.read()))


def test_day5_star1():
    input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
    expected = 46
    actual = solve(clean_lines(input))
    assert actual == expected
