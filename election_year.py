

class ElectionYear(object):
    def __init__(self, year, ec_total=None, pop_total=None, pop_margin=None):
        self.year = year
        self.ec_total = ec_total
        self.pop_total = pop_total
        self.pop_margin = pop_margin

    def pop_per_ec(self):
        if not self.pop_total and self.ec_total:
            return -1
        return self.pop_total / self.ec_total

    def swing_weight(self):
        if not self.pop_total and self.pop_margin:
            return -1
        return self.pop_total / self.pop_margin


year_data = {
    1824: ElectionYear(1824, ec_total=261, pop_total=365928),
    1828: ElectionYear(1828, ec_total=261, pop_total=1148018, pop_margin=141656),
    1832: ElectionYear(1832, ec_total=288, pop_total=1276659, pop_margin=228628),
    1836: ElectionYear(1836, ec_total=294, pop_total=1502811, pop_margin=213384),
    1840: ElectionYear(1840, ec_total=294, pop_total=2412694, pop_margin=145938),
    1844: ElectionYear(1844, ec_total=275, pop_total=2703864, pop_margin=39413),
    1848: ElectionYear(1848, ec_total=290, pop_total=2876818, pop_margin=125763),
    1852: ElectionYear(1852, ec_total=296, pop_total=3159640, pop_margin=218520),
    1856: ElectionYear(1856, ec_total=296, pop_total=4051605, pop_margin=494472),
    1860: ElectionYear(1860, ec_total=303, pop_total=4681335, pop_margin=333966),
    1864: ElectionYear(1864, ec_total=233, pop_total=4031887, pop_margin=405581),
    1868: ElectionYear(1868, ec_total=294, pop_total=5722440, pop_margin=304810),
    1872: ElectionYear(1872, ec_total=366, pop_total=6471983, pop_margin=763729),
    1876: ElectionYear(1876, ec_total=369, pop_total=8418659, pop_margin=-252666),
    1880: ElectionYear(1880, ec_total=369, pop_total=9219477, pop_margin=9457),
    1884: ElectionYear(1884, ec_total=401, pop_total=10060145, pop_margin=57579),
    1888: ElectionYear(1888, ec_total=401, pop_total=11388846, pop_margin=-94530),
    1892: ElectionYear(1892, ec_total=444, pop_total=12068027, pop_margin=363099),
    1896: ElectionYear(1896, ec_total=447, pop_total=13938674, pop_margin=601331),
    1900: ElectionYear(1900, ec_total=447, pop_total=13997429, pop_margin=857932),
    1904: ElectionYear(1904, ec_total=476, pop_total=13525095, pop_margin=2546677),
    1908: ElectionYear(1908, ec_total=483, pop_total=14889239, pop_margin=1269356),
    1912: ElectionYear(1912, ec_total=531, pop_total=15044278, pop_margin=2173563),
    1916: ElectionYear(1916, ec_total=531, pop_total=18536585, pop_margin=578140),
    1920: ElectionYear(1920, ec_total=531, pop_total=26765180, pop_margin=7004432),
    1924: ElectionYear(1924, ec_total=531, pop_total=29097107, pop_margin=7337547),
    1928: ElectionYear(1928, ec_total=531, pop_total=36807012, pop_margin=6411659),
    1932: ElectionYear(1932, ec_total=531, pop_total=39751898, pop_margin=7060023),
    1936: ElectionYear(1936, ec_total=531, pop_total=45647699, pop_margin=11070786),
    1940: ElectionYear(1940, ec_total=531, pop_total=49902113, pop_margin=4966201),
    1944: ElectionYear(1944, ec_total=531, pop_total=47977063, pop_margin=3594987),
    1948: ElectionYear(1948, ec_total=531, pop_total=48793535, pop_margin=2188055),
    1952: ElectionYear(1952, ec_total=531, pop_total=61751942, pop_margin=6700439),
    1956: ElectionYear(1956, ec_total=531, pop_total=62021328, pop_margin=9551152),
    1960: ElectionYear(1960, ec_total=537, pop_total=68832482, pop_margin=112827),
    1964: ElectionYear(1964, ec_total=538, pop_total=70639284, pop_margin=15951287),
    1968: ElectionYear(1968, ec_total=538, pop_total=73199998, pop_margin=511944),
    1972: ElectionYear(1972, ec_total=538, pop_total=77744027, pop_margin=17995488),
    1976: ElectionYear(1976, ec_total=538, pop_total=81531584, pop_margin=1683247),
    1980: ElectionYear(1980, ec_total=538, pop_total=86509678, pop_margin=8423115),
    1984: ElectionYear(1984, ec_total=538, pop_total=92653233, pop_margin=16878120),
    1988: ElectionYear(1988, ec_total=538, pop_total=91594686, pop_margin=7077121),
    1992: ElectionYear(1992, ec_total=538, pop_total=104423923, pop_margin=5805256),
    1996: ElectionYear(1996, ec_total=538, pop_total=96275401, pop_margin=8201370),
    2000: ElectionYear(2000, ec_total=538, pop_total=105405100, pop_margin=-543895),
    2004: ElectionYear(2004, ec_total=538, pop_total=122294846, pop_margin=3012166),
    2008: ElectionYear(2008, ec_total=538, pop_total=131313820, pop_margin=9550193),
    2012: ElectionYear(2012, ec_total=538, pop_total=129085410, pop_margin=4982291),
    2016: ElectionYear(2016, ec_total=538, pop_total=136669276, pop_margin=-2868686),
    2020: ElectionYear(2020, ec_total=538, pop_total=00000000, pop_margin=00000000),
}