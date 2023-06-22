"""
1353. Maximum Number of Events That Can Be Attended
Medium
2.5K
330
JPMorgan
company
Amazon
company
Google
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.



Example 1:


Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4

"""
import time
from collections import defaultdict
from typing import Optional


class Event:
    def __init__(self, event, idt):
        self.idt, self.start, self.end, self.attended = idt, event[0], event[1], False

    def contains(self, d):
        return self.start <= d <= self.end

    def __str__(self):
        return f'id {self.idt}, start {self.start}, end {self.end}, attended {self.attended}'

class MinPQ:
    def __init__(self, keys, order=None):
        self.keys = [None] + [_ for _ in keys]
        self.order = order if order else (lambda x, y: x if x[1] <= y[1] else y)
        self.N = None
        self.heapify()

    @property
    def n(self):
        return len(self.keys) - 1 if self.N is None else self.N

    def empty(self):
        return self.n == 0

    def key(self, i):
        return self.keys[i] if self.is_legit(i) else None

    def ordered(self, i, j):
        return i if self.order(self.key(i), self.key(j)) == self.key(i) else j

    def preferred(self, i, j):
        if not i and not j: return None
        if not i: return j
        if not j: return i
        return self.ordered(i, j)

    def is_legit(self, i):
        return 1 <= i <= self.n

    def legit(self, i):
        return i if self.is_legit(i) else None

    def up(self, i):
        return i // 2

    def lt(self, i):
        return 2 * i

    def rt(self, i):
        return 2 * i + 1

    def parent(self, c):
        return self.legit(self.up(c))

    def left(self, p):
        return self.legit(self.lt(p))

    def right(self, p):
        return self.legit(self.rt(p))

    def child(self, p):
        return self.preferred(self.left(p), self.right(p))

    def swap(self, i, j):
        self.keys[i], self.keys[j] = self.keys[j], self.keys[i]

    def bal_down(self, p):
        if not p: return True
        return self.preferred(p, self.child(p)) == p

    def bal_up(self, c):
        if not c: return True
        p = self.parent(c)
        if not p: return True
        return self.preferred(p, c) == p

    def unbal_parent(self, c):
        if self.bal_up(c): return None
        return self.parent(c)

    def unbal_child(self, p):
        if self.bal_down(p): return None
        return self.child(p)

    def lift(self, c):
        p = self.unbal_parent(c)
        if not p: return None
        self.swap(p, c); return p

    def drop(self, p):
        c = self.unbal_child(p)
        if not c: return None
        self.swap(p, c); return c

    def swim(self, c):
        while not self.bal_up(c):
            c = self.lift(c)

    def sink(self, p):
        while not self.bal_down(p):
            p = self.drop(p)

    def heapify(self):
        for i in range(self.n, 0, -1): self.sink(i)

    def push(self, key):
        self.keys.append(key)
        self.swim(self.n)

    def pop(self) -> Optional[Event]:
        if self.empty(): return None
        self.swap(1, self.n)
        top = self.keys.pop()
        self.sink(1)
        return top

    def sort(self):
        self.N = self.n
        while self.N >= 1:
            self.swap(1, self.N)
            self.N -= 1
            self.sink(1)
        self.N = None

    def __str__(self):
        s = ''
        for i in range(1, self.n + 1):
            s += f', {self.keys[i]}'
        return s

    def print(self):
        print(self.keys)

def min_max(es):
    if not es: return 0, 0
    min_d, max_d = float('inf'), float('-inf')
    events, day_event = [], defaultdict(set)
    for (i, e) in enumerate(es):
        min_d = min(min_d, e[0])
        max_d = max(max_d, e[1])
        ev = Event(e, i); events.append(ev)
        for d in range(e[0], e[1] + 1):
            if ev not in day_event[d]:
                day_event[d].add(ev)
    return min_d, max_d, events, day_event

def max_events(es):
    if not es: return 0
    min_d, max_d, events, day_event = min_max(es)
    order = lambda e, f: e if e.end <= f.end else f
    max_es = 0
    for day in range(min_d, max_d + 1):
        es = day_event[day]
        pqd = MinPQ(keys=es, order=order)
        if not pqd.empty():
            e = pqd.pop()
            if e.attended:
                while not pqd.empty() and e.attended:
                    e = pqd.pop()
            if not e.attended:
                max_es += 1
            e.attended = True
    return max_es

if __name__ == '__main__':
    es = [[722,869],[974,1185],[947,1408],[928,1129],[101,279],[833,1132],[226,327],[733,1280],[587,611],[378,1107],[557,1088],[988,1889],[729,1398],[761,1382],[585,821],[580,987],[400,816],[358,1341],[1000,1090],[459,946],[301,1295],[952,1671],[18,224],[397,499],[232,852],[631,1244],[483,776],[215,434],[212,1096],[430,551],[965,1364],[69,257],[89,299],[673,1217],[206,1110],[170,953],[665,1545],[115,286],[25,100],[851,1200],[764,904],[649,1141],[4,774],[190,684],[170,1030],[230,867],[367,913],[984,1412],[19,476],[349,598],[354,1033],[226,717],[523,740],[9,331],[530,1330],[602,1410],[617,1181],[537,590],[167,983],[776,1773],[76,713],[45,937],[968,1132],[976,1249],[67,428],[241,1227],[108,348],[261,1018],[634,1253],[445,710],[358,393],[77,1064],[797,1403],[554,1255],[481,1382],[339,1294],[683,1316],[997,1438],[593,1244],[75,1042],[790,1133],[913,1683],[661,1123],[739,1058],[392,573],[676,1027],[532,736],[756,1006],[85,167],[179,733],[292,512],[387,1094],[991,1426],[123,932],[716,1154],[434,513],[722,1343],[585,1495],[625,662],[252,300],[460,1078],[666,1082],[260,1008],[373,563],[962,1192],[494,1328],[466,724],[403,1064],[613,1260],[156,553],[265,681],[147,1146],[694,883],[133,189],[525,1186],[91,855],[657,1274],[668,1077],[96,354],[917,1627],[160,445],[494,529],[265,438],[669,758],[67,519],[693,793],[356,688],[660,891],[51,80],[977,1277],[573,1048],[506,1374],[568,624],[64,1056],[974,1737],[811,1438],[395,919],[460,547],[592,835],[480,974],[74,321],[934,1058],[825,833],[187,1098],[22,214],[820,994],[725,1565],[864,1637],[702,742],[797,1487],[922,1875],[583,1172],[975,1088],[584,1351],[352,856],[793,1115],[628,1316],[749,1583],[751,1025],[665,1643],[745,839],[504,1082],[126,1119],[126,454],[23,231],[712,724],[467,994],[680,1101],[770,1368],[770,894],[152,271],[987,1568],[437,646],[315,395],[604,1053],[186,842],[854,1359],[206,600],[651,1608],[217,943],[733,1144],[454,1274],[246,769],[671,1203],[146,824],[804,1617],[913,1522],[526,1306],[193,286],[987,1540],[876,1628],[433,1193],[965,1533],[842,1806],[499,1357],[822,1647],[544,669],[365,1206],[578,622],[117,840],[987,1945],[159,392],[840,1073],[540,619],[650,1526],[801,962],[72,1033],[811,873],[635,737],[602,1057],[51,104],[926,1671],[845,1539],[303,915],[391,816],[303,856],[428,1140],[528,1009],[720,1237],[671,1121],[75,589],[228,413],[155,494],[659,1343],[87,557],[410,1373],[687,871],[488,526],[819,900],[739,850],[996,1928],[910,1905],[272,963],[306,1224],[680,1440],[243,517],[379,765],[787,1559],[675,1650],[269,791],[749,1427],[882,1154],[859,967],[156,481],[143,276],[753,1639],[633,1184],[937,1093],[8,311],[981,1500],[266,934],[553,796],[92,867],[266,1064],[641,905],[557,1287],[703,1463],[608,1370],[233,925],[540,1483],[199,1132],[110,674],[612,975],[377,1350],[565,1344],[895,1299],[936,1624],[257,930],[432,1187],[520,573],[578,1187],[381,525],[509,519],[472,524],[748,1201],[290,765],[890,942],[256,584],[406,1171],[254,1019],[420,822],[667,1519],[889,1043],[957,1817],[741,1005],[436,1220],[716,872],[333,477],[572,1533],[443,541],[399,576],[765,1035],[470,1120],[964,1207],[200,633],[171,270],[137,712],[317,952],[237,284],[736,1351],[700,1521],[336,927],[17,478],[757,793],[423,1197],[188,349],[269,426],[575,1170],[705,780],[453,1264],[232,418],[426,1291],[827,1232],[44,894],[725,1311],[290,746],[178,394],[531,1178],[236,1175],[567,722],[322,959],[482,1157],[335,338],[234,327],[829,1296],[620,902],[454,1249],[47,464],[650,1180],[364,1167],[137,224],[891,1400],[208,624],[629,1197],[2,714],[447,897],[374,619],[878,1873],[120,675],[413,1105],[467,1238],[157,824],[107,783],[756,851],[394,1241],[386,923],[133,842],[191,483],[504,1397],[971,1362],[831,1243],[117,1101],[906,1827],[528,666],[101,277],[341,1304],[390,763],[644,1428],[738,1193],[969,1146],[378,540],[730,1629],[182,390],[630,772],[728,1328],[505,1283],[562,912],[139,428],[259,1100],[401,1071],[707,1135],[18,963],[813,1176],[329,964],[104,1048],[971,1180],[693,1104],[936,1839],[538,1352],[33,186],[766,1226],[212,686],[897,1121],[828,1698],[381,1308],[333,578],[548,794]]
    start = time.time()
    print(max_events(es))
    end = time.time()
    print(f'time = {end - start}')


