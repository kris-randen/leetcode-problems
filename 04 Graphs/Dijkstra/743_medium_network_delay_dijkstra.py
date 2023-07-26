"""

743. Network Delay Time
Medium
6.7K
336
Companies
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.



Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

"""

from collections import defaultdict
from heapq import *
from typing import List

class HeapDict:
    def __init__(self, order=None):
        self.pq, self.qp, self.dict, self.N = [-1], {}, {}, None
        self.order = order if order else (lambda x, y: x if x < y else y)

    def __getitem__(self, key): return self.dict[key]

    def __len__(self): return len(self.pq) - 1 if not self.N else self.N

    def is_valid(self, i): return 1 <= i <= len(self)

    def valid(self, i): return i if self.is_valid(i) else None

    def is_empty(self): return len(self) == 0

    def key(self, i): return self.pq[i]

    def val(self, i):
        return self.dict[self.key(i)]

    def item(self, i): return self.key(i), self.val(i)

    def ord(self, i, j):
        return i if self.order(self.val(i), self.val(j)) == self.val(i) else j

    def pref(self, i, j):
        if i and j: return self.ord(i, j)
        return i if not j else j

    def up(self, i): return i // 2

    def lt(self, i): return 2 * i

    def rt(self, i): return (2 * i) + 1

    def parent(self, c): return self.valid(self.up(c))

    def left(self, p): return self.valid(self.lt(p))

    def right(self, p): return self.valid(self.rt(p))

    def child(self, p): return self.pref(self.left(p), self.right(p))

    def bal_up(self, c):
        p = self.parent(c)
        if not p: return True
        return self.pref(p, c) == p

    def bal_dn(self, p):
        return self.pref(self.child(p), p) == p

    def unbal_p(self, c):
        return None if self.bal_up(c) else self.parent(c)

    def unbal_c(self, p):
        return None if self.bal_dn(p) else self.child(p)

    def swap(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[self.pq[i]], self.qp[self.pq[j]] = i, j

    def lift(self, c):
        p = self.unbal_p(c)
        if not p: return None
        self.swap(p, c); return p

    def drop(self, p):
        c = self.unbal_c(p)
        if not c: return None
        self.swap(p, c); return c

    def swim(self, c):
        while c: c = self.lift(c)

    def sink(self, p):
        while p: p = self.drop(p)

    def heapify(self):
        for i in range(len(self), 0, -1): self.sink(i)

    def __setitem__(self, key, value):
        if key in self.dict:
            index = self.qp[key]
        else:
            self.pq.append(key)
            index = len(self)
        self.qp[key] = index; self.dict[key] = value
        self.swim(index); self.sink(index)

    def top_key(self): return self.pq[1]

    def top_val(self): return self.dict[self.top_key()]

    def top_item(self): return self.top_key(), self.top_val()

    def pop_item(self):
        self.swap(1, len(self))
        key, val = self.item(len(self))
        self.pq.pop()
        self.sink(1)
        self.qp.pop(key); self.dict.pop(key)
        return key, val

    def pop_key(self): return self.pop_item()[0]

    def pop_val(self): return self.pop_item()[1]

    def sorted_items(self):
        self.N = len(self)
        while self.N > 1:
            self.swap(1, self.N); self.N -= 1; self.sink(1)
        items = [self.item(i) for i in self.pq]
        self.N = None; self.heapify()
        return items

    def sorted_keys(self):
        return [map(lambda x: x[0], self.sorted_items())]

    def sorted_vals(self):
        return [map(lambda x: x[1], self.sorted_items())]

class Wedigraph:
    def __init__(self, V, es):
        self.V = V; self.adj = defaultdict(list)
        self.adds(es)

    def add(self, e):
        self.adj[e[0]].append(e)

    def adds(self, es):
        for e in es: self.add(e)


class DijkstraHeapq:
    def __init__(self, g, s):
        self.g = g; self.V = g.V
        self.dist_to = {v: float('inf') for v in range(1, self.V + 1)}
        self.dist_to[s] = 0; self.pq = []
        heappush(self.pq, (s, self.dist_to[s]))
        while self.pq:
            v, _ = heappop(self.pq)
            for e in self.g.adj[v]:
                self.relax(e)

    def relax(self, e):
        u, v, wt = e; du, dv = self.dist_to[u], self.dist_to[v]
        if dv > du + wt:
            self.dist_to[v] = du + wt
            heappush(self.pq, (v, self.dist_to[v]))

    def max_time(self):
        max_t = 0
        for v in range(1, self.V + 1):
            if self.dist_to[v] == float('inf'): return -1
            max_t = max(max_t, self.dist_to[v])
        return max_t


class DijkstraHeapDict:
    def __init__(self, g, s):
        self.g = g; self.V = g.V; self.adj = self.g.adj
        self.dist_to = {v: (0 if v == s else float('inf')) for v in range(1, self.V + 1)}
        self.pq = HeapDict(); self.pq[s] = self.dist_to[s]; c = 0
        while self.pq and c < self.V + 4:
            v = self.pq.pop_key(); c += 1
            for e in self.adj[v]:
                self.relax(e)

    def relax(self, e):
        u, v, wt = e; du, dv = self.dist_to[u], self.dist_to[v]
        if dv > du + wt:
            self.dist_to[v] = du + wt
            self.pq[v] = self.dist_to[v]

class Edge:
    def __init__(self, u, v):
        self.u, self.v = u, v

    def __str__(self):
        return f'u = {self.u}, v = {self.v}'

    def __repr__(self):
        return self.__str__()

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = Wedigraph(n, times); dijk = DijkstraHeapq(g, k)
        return dijk.max_time()

def ppt():
    print('ha')

def ppf():
    print('ho')


if __name__ == '__main__':
    # es = [(1, 2, 4), (1, 3, -4), (2, 3, 6), (2, 4, -30), (3, 4, -9), (1, 4, 2), (4, 1, 13)]
    # g = Wedigraph(4, es)
    # print(f'g = {g.adj}')
    # dijk = DijkstraHeapDict(g, 1)
    # print(f'distances = {dijk.dist_to}')
    # us = ["amxqm","emltyqm","eopqygzi","fdygnb","fti","hlymcho","hneyh","iww","kkgy","lul","mbpcschk","myicoov","nhlwoz","oqyaez","puksbb","rywllv","tejdk","tvvklwv","txbhgse","xvc","yeqrcma","ygpp","ywkiraq","alqjhmp","asfxudbx","bctq","bxj","eanmfjrw","ebl","epnk","evx","fsnpuexc","fthpft","gnlejzsf","gsvmzxw","hnz","htuwbbap","ibewwu","ikz","ioqx","jcrths","jhadg","kbcee","kgyf","klojcbqk","lbbntns","ll","llltqxrg","lxczym","lzkmf","mqu","nvj","nzvso","oynhmfdh","qybjp","rmdjyct","rokuo","sbfnhp","sk","slrkq","srkbj","strehbrz","uaohmrcn","utkuwgt","vfaygbac","vixxyh","vjpyizj","wek","wfcvsqrg","wub","xiwproo","xk","yako","zlngfan","amsrmhxq","bauboal","bjyblgk","bngmssvy","ceqwef","ctdsk","cvjbs","cxkciwzq","cynhwl","dehpkon","dwu","dycp","enfd","eytfxgq","fjbujsjb","fuym","gdywwog","gsvhepd","hec","hmrs","hneqsoc","huztrh","hybhd","ibv","icwq","iifjvcyt","inxzrsrc","jbpcfx","jcrbnwe","jkp","kzfwvgxo","lethjxbn","lh","lpp","lv","mbcrl","md","mv","mvmmo","nzmruv","oclcff","oo","pbvquv","pxbfrmzv","pxvuufmb","qjd","qs","qt","qvptdx","qwzmsh","recp","rmhrats","ryd","siu","sqjak","ssrhdpdo","sxsjojyq","ttyee","ueshrug","umnazia","uxkjiflv","vatzpu","verub","vgmk","vidsjn","wepsuyx","wsuevxuy","wupioza","xj","ybhtjfqt","yfueb","yhkci","yr","zo","zzrosejs","bg","bnxk","bqbcnk","bqt","btcgll","cmstgv","cwqmaez","dgxu","eljltqs","ferdvt","fq","fujb","gmrtxofh","hoyqucx","ht","hvd","ih","isbame","iyychnmp","javino","jlaokmo","jrd","kdudr","klhyi","ldvqoi","lrbdoib","mggtebu","mjftjj","nfg","nkxy","nox","nqcnlrs","ohgszrge","oll","ovfgjrje","pb","plxufnbv","pyubrhq","rhjqjm","rjq","sjnjuqf","slhhd","tno","ukzww","utgbtzbw","vdkn","vf","vhw","vwa","wehtltm","wmkg","wruidqxj","wsp","wuwtqynj","wx","xoejob","xva","xvfztsmg","xxnuelmh","zhod","zikyver","zqs","agstpaj","asdjtqf","axr","bsd","bsrwbgw","bvbnyzx","cja","cwymbawg","djsez","dxvcb","esweflv","eyidrzcv","ezhhks","fhsaragz","fnsihyx","gafn","gaqxfgvu","gbwzts","gdwbpg","htx","htzxhgwe","hyytzn","inxhodc","joobor","jqyie","kbv","kf","klvtoow","krhlbbdf","ktcs","lcqvoq","llagh","lqczjco","mofxfn","mojqlg","mpzrhhn","mwfvbc","niqutzv","nqzumvs","ocbwwoze","oibz","okfvgncm","olvjei","ovqcmbsx","pe","pplndvc","qdysj","qmyl","rflszqlw","rjx","ruj","tjrfua","tqazzy","ufogi","uiybbqb","vbmesxef","vct","vslwc","wvyhb","wzitf","xr","ygmkjptq","ykcn","yobz","zh","zlsywvas","zricy","aahqw","ajbvrdip","amto","atwxg","avytejzi","bdujztlz","beawy","beu","bfgwp","bhdxmvr","bkw","blydkbg","bmul","bppbs","byaqua","caokslln","cdjzzwd","cfkoyrfw","cgywt","cnck","cohfs","cqtdotp","dbc","ddlyllm","dkux","dl","dodkqr","dsyj","dubywary","dujy","dx","dxsjwj","edwpifbd","egbq","ehllf","elh","emfawdxb","ervfzz","fqvgfdxn","frysxj","ft","fxn","gdycfau","gf","ggdawy","ggyhr","ggznq","glsvjl","gltvwcy","gvn","gxoqybe","gzdly","hbtp","hfmwsl","hgigfk","hgyejw","hqec","hyyfwcsh","idg","iowmfew","ir","irhu","iulxagt","jauoana","jhuc","jisuqqws","jo","jvidruif","kifqs","knuafilh","kxx","lcxzhg","lmky","lvlptta","lwvlsyl","lwxkn","lzpetg","mhfnfrr","mjhfphus","mkgz","mnbb","mopmm","mrrswj","mubdtbe","mwsl","mxesle","ncmgx","nil","niyqu","nkpy","nlvhc","nlzwmfj","nnt","nwj","ocfiqazn","ojni","okvjkvyq","onkzyw","ooruhnim","oyx","pbn","pdcjumn","pgugzezg","pimd","pki","pkmz","pna","prztfh","puvseih","pwahre","qafhd","qjys","qmc","qnhgyuca","qscflqzr","quyagc","qwluaepp","qxt","qyu","rfnllaff","rg","rrfwb","rsekk","rtpz","rzeigpx","saq","sf","sm","snpy","sqda","srsgf","svoe","tiqy","tlddi","ttrd","ubdmd","ufksguh","uiwde","umvuasw","uogtaom","uwnxdgv","uyufwg","vhfyv","vlkr","vuey","vxklb","vzkfucma","waakunjp","wdd","wms","xa","xczvb","xdlcoipx","xehrx","xfke","xhxanyck","xliwyjpf","xlnomnc","xqfojwnc","xsggkpoa","xssgzj","xurdrryh","ycg","ynss","yoxapiji","ytcj","zap","zdxjg","zhmowi","zhuikb","zhuiuaqt","zosswje","zph","zpt","zsp","zvi","zwwpuo","ehn","fcrcewan","fqddsdat","gluou","gonkvak","ags","anqccafz","bdos","beuskjaw","bivoa","bldgown","blrjnjn","bmugu","bvykudcz","cbtarzna","ccbrqw","cxflkogc","dbvtbysl","ddxb","du","fcgshqau","fejkqvy","fjx","fsgait","fxdiywn","gcjdk","gcvelf","hfawjrid","hovs","hw","japb","je","jm","jtwrf","kcvwi","kjgbko","kmuymas","ktcydtys","lhfzdc","lsfyzup","lubx","njyknfy","nmy","nruvliv","nxmngtf","phr","pqbrzhho","qal","qaq","qmjfwh","rlvybe","rtzbq","sbc","tt","vgvbsme","wq","wtdeb","xgjxns","yfqe","yhqv","yttpiqj","yyjaazzl","zcnuzqm","zfmnn","acpbq","acqbzcpg","acuasra","adktoowx","aif","appjl","au","avvv","bcvljj","bdrkke","bfcfva","bjrnaje","bkfsgskm","bmnrvk","bpn","ccolykvj","cczhhuz","crirtco","cyo","dafywrlg","db","dne","dunmmsl","dvijf","dxk","dzcdokjm","eai","eam","edr","efffpnxk","ekere","ekvuedo","ekytg","epgu","esfwfxz","esg","etblfs","etsh","etzojkt","eyqinhk","fa","fnwpk","fsckiak","fstaojn","ftatanmk","fxx","fxzz","fzd","gcgtnz","gd","gdcidgxe","gderdvij","gdkfmvh","ggcuovv","ggfx","ghofyfe","gmiqujyh","grdglrp","gstoucsf","gt","gxyvkix","gzms","hank","hapk","hdaodkt","hexwxks","hiunkv","hlzvai","hmwa","hrmwljch","hwcqirs","hxwymy","ibigtq","ichmdqj","ie","ildwllf","imk","irymgnl","iw","iwfjpb","iyf","jadesjd","jbbirm","jbmytwjf","jcpbpxdk","jdrbkmv","jgcjpqo","jipyhkgv","jjmlwvaj","jkkq","jt","jucq","jwbvntg","karc","kccprfov","kjt","kkix","kn","kno","kxkfxhpa","lf","lg","lhg","lkpzrll","ln","lvkoyxui","lxypjmjd","ma","mctgtx","msxeuk","mtljx","nbb","ngknu","nkbwua","nnhal","nomtjwe","ntdqrupy","nvju","nzzzxf","oaf","odvgaoym","oevqtgx","ofqdzo","ofr","ojv","old","or","otzer","ovamenq","pbggxbli","pff","phbzohr","pnoh","ptwegwd","pvaq","qhkkpb","qmvuhh","qrq","qsr","qumwb","qwe","qxfuymsv","raceaxrv","reqmnno","rlzzbg","rmljjop","rnltyefb","ruxvu","satqr","scg","senm","sgxjgzlj","snkmqge","snlgqblp","snynmfx","sw","sxsg","terkfmsg","tgdqayyr","thtnshvc","tmro","tsjaxaac","tvvio","twdh","txbi","tye","uc","ud","udby","ufrlx","uhhq","uma","upnyck","utvccvep","vd","ve","vhpvtjml","vhqs","vhr","vjinqohl","vjtn","vqlkipgq","vyuth","wbcb","wevio","whw","wneshaj","wslwmm","wvjexyvs","wwwr","xadiij","xf","xjn","xmlnagfa","xmzmz","xnzh","xpdjlhdp","xpmqgi","xwo","xxp","ydfejw","yhqdm","ykm","ym","ynwsjqv","yoypt","yyodbar","zfk","zkvxjq","zla","zneg","zpxtsud","zryyz","zs","zygl","zzy","bmgxrjb","cia","dfj","dgjdu","dixl","dlu","ejkcva","epfnljam","ez","fpudcpdq","hgcanzea","hvmxam","hvuhtl","icg","iluyh","ipfx","jlcagk","jpt","jxrn","kchar","kkcjvefa","kvy","meggayf","mered","njogumsi","ntrvofp","ofzozxr","oivu","qggrh","qkobff","qruved","qxqb","qysmgz","spa","suzqlp","tg","tocr","udjebe","vmmyrghn","vnnklb","vzzfl","wlpsyfk","wwfhcgi","yalncg","ygog","yjrhzqya","yseycc","zeliuld","zlyuczou","zpdik","zuuuyrwb","ti","xm","aexrptb","ajkxem","apseumj","asia","bb","bdgphzu","bh","bmune","brzaqop","cctjw","citos","clg","cn","cwlulwe","cyxb","dcctlxps","ddcuaaq","dhi","dlzhrdb","dpdyzvc","dwhidp","dzdnmmc","ehlgojs","enralnde","eqfcwxo","eujwuofn","fdwogyuu","fdxewafw","ffw","fssm","gahaxoog","geyr","gfr","gu","guf","hcfomp","hcqgrg","hmxahz","hqydm","hsz","hualrle","hvl","incqx","ipysnwgh","iq","irygzi","iubd","izmrwhj","jb","jhhwp","jjzhd","jrdnvoa","jtax","juf","kknoabwx","leexudh","lefr","merx","mie","mkvqncs","motuandq","mslhf","mtlrlso","mzv","nfpywff","nhqls","nkduorni","nl","nnjn","nticyujp","nvwc","oexo","ofvttmg","ojje","ojwuhrt","olerpji","otqifg","owd","pcrpkry","pmmf","pqwkd","pxgmspla","qeff","qeizry","qlwcw","ronlfg","rpwckq","rrk","rttq","si","slsdvi","tix","tojeb","tru","trx","tzjix","tzronke","tzurlmu","uaxy","ubai","ucknzl","uebnj","uoqmly","usw","vfexk","vhd","vqs","vux","vxecuy","vyxqptfc","wdunp","whfbif","wvwig","wxtek","xaiej","xiv","xnbtud","xtzlh","xvep","yfl","yk","yqstvsuo","ytiwed","ywceyvkc","yxxxeylq","zaqtjd","zcl","zmrjw","zwteabmc","zxnllz","aeszt","aficur","amyiyj","ankkyoj","bijrog","bkeqdhq","bofr","borwtfh","bpczp","brw","bvtwlt","bxrjkgxq","cfj","cyuefc","dfkw","dontitz","ebcxoegr","eiarkc","ekrl","emuxwp","fafn","fiqypqx","fpsij","fptnyg","gql","gykimk","hd","hfvkiuyk","hhj","hiz","hogixlxh","hul","hwv","ihoxlbum","jcmuyyf","jqmsk","jqqsceky","jrpaxvb","jtqjv","kbn","kfxdymxb","kjbdl","lpxv","lqwi","mdglfb","mur","mzekh","nevfwp","ontktd","ool","oqeprxfa","pc","pez","pvc","qgoo","qsfjqu","qsyesc","qtsvjaez","rk","rxfcd","sa","sclx","sdhbxp","soxsbpj","sqmg","tbprv","tbtpjkeu","tmdv","ub","ufimddbs","ujvyus","uvzjqfep","uwfcy","wb","wfnfgjgu","whfv","wmyuqmr","woyocl","wpqfle","wxxoo","xruh","xwret","yh","ykeah","yqwecuie","yslzlqd","yt","yyzvayrh","zbkyoh","zzd","aeevzaz","biqdge","bjrumdn","cbgvjf","cgqxwko","chzxo","csnywr","ezqkfz","fcomyr","gipvcefr","gkoksp","hdzhes","hocy","hsucajbz","ikuog","iyemic","jbwjpnk","jswjwi","jtejvw","kaxkvkjv","kricqh","kuie","lcoftm","lhca","lxkl","moz","mtmn","oeyuz","oxacbtqv","qivk","qnlna","qpprdphu","qsogiqiy","rtbdtvm","rvaiy","smqxudzq","sqtiqcvl","sx","tfol","tja","trh","ugqg","uqskjr","vntfr","wmdn","xbrkgdyw","xs","xtzzh","xzumcs","yniipis","zis","eaxf","frivanp","gobzzi","ikiv","iyaxd","izwh","jiw","mgdekuy","mmqoeyr","qubqspx","rwnigrkf","sgu","sjfwungg","udrj","wxoybsq","xpl","ykp","ypvggn","adz","ahws","aic","anjyuizb","apfgvv","avceu","aw","awmr","ckkulcb","crmiu","dawevmzx","dfs","eav","eldzbubv","erpii","erw","gajcgr","goohv","gsnghu","hfxsu","hlec","hog","hou","ibt","if","ihvolkn","iqfc","itakvz","ivjg","ivtbd","jawy","ji","jtx","kbh","kjkli","klcszliq","lcd","lct","ldpjxk","lfwwac","liozmhk","lpihzqy","luqdkws","mdlgn","mqjwt","mwgzulw","neo","nfotqiw","nkvbdaa","oe","pp","prmvw","qawyay","qdap","qdh","qvaif","qxa","qz","rtdyv","rttt","sdwxylte","sly","svxy","tkdcsud","tztewgwv","upxtmmxf","utlh","vmsd","wd","wktrw","wnqegc","wstyrch","wtjwxas","wyqe","xo","xps","xwzn","yaqat","ycqaqgdb","yfkul","ylk","ysftfpvd","yutstb","zomkt","zpivtptj","zsemv","ng","aaytlfld","aequgwp","afgsbd","agw","aqx","ar","arr","arrr","auehjyea","axcgtlwg","ay","aza","azholcbl","bcehopq","bdaw","bdpfmi","bew","bezo","bfj","bfuelxd","blfh","bnkqx","boyk","br","buq","bzapde","bzvgb","cdmka","cfvhgiao","cgbenf","cuygabd","cz","dbv","dhf","dhz","do","dsnqkcgr","dspiefab","dxbw","dxuvzo","dy","ecb","eercvp","elqllg","eoowlp","eovrucew","ermus","euct","euvbqc","evuahj","exgai","eyed","fcixmwo","felq","fgar","fjhqofm","fp","frteyp","gagsl","gfply","ggalak","gjy","gs","guajus","gviun","gzmivzc","hev","hkc","hkxmtotp","hngaewzg","hryjx","hsb","hwgpqj","hyawq","ial","ibvsy","id","ierx","iow","ippgkem","iwoi","iyuyifpj","izc","izv","jbnliai","jdmnhyhh","jfbkgyh","jhahxwo","jimkbb","jjulepyk","jpi","jpoelgz","kb","kbdyzm","kbs","kekuqlo","kjusffp","klpm","knigx","knm","ko","kpm","kq","kxusgwwf","kzh","lbubvak","lhr","ljhtgdfw","lk","lkce","lny","lsagloa","manppy","mdkatgdj","mdybxh","mhncgq","ml","mohr","mu","mx","mxenruky","navbix","nbp","ncirsk","nco","ndugwcid","ne","ni","njskzfm","nkwip","nlomewm","nlq","nnxrlg","nqwfcg","nrmha","nxagmcr","nyhhk","obxj","oc","odskaqu","oeptbllx","ohwvbxme","osjw","otdofhyr","oyqq","pahoflb","pbbevadv","pngpkf","pnhhm","ppy","pqhl","pxpc","pylub","pzowugg","qao","qloi","qmh","qqku","qszbjq","qutrwott","qvfspy","qxvew","qydo","rcng","rdgmydc","rdn","rmk","roeiav","sactnm","sdrg","sfda","sjpjog","sutbq","swhps","tbv","tdlske","thqffwk","thqwr","tibvxib","tli","tmhac","tnpgyr","tntquag","trvyqg","ucfmyuyr","uck","uf","ug","ulz","umtmbwic","upswld","usfrbuqs","uwvz","uy","vby","vdwfpxa","vei","vgao","vhmvnpd","viwtvpqz","vj","vl","vms","vsvhq","vt","vtifmka","vxjnrpt","vxx","vyb","vzokgasl","wi","wiagfoln","wmmudlm","wnr","wtjhkfmj","wzgjs","xdziogtc","xedbgr","xgma","xh","xjrczjbh","xjtkur","xlac","xrk","xwwzis","xzfyi","ycer","ydrhmj","yit","ylayfbqv","yqynxfld","ytrt","yvhyzajk","zat","zbozkt","zci","zfi","zfkpa","zflpon","zfndbys","zg","zkwmuahz","zpd","zpvo","zsu","zzfrlfb","oq","bjzpdtcu","byv","fpnynxcn","ftxfhpx","ggnroqk","gnd","gw","gyz","houzewi","jlnnj","kgjk","lbxy","lqzwkp","lwqcqxb","mbjejj","mbtrofo","mk","ncrb","nwrbseln","pfhpsns","pyxkbe","rbjzorvg","uerx","upe","vv","wcolhnk","wvzzh","wyppwei","xpd","yxrija","zcrsiqf","bbhidxx","boincann","cqwvu","cupaornn","djldvmql","dndgwklv","dnyf","dwp","eoa","ep","etsnqhce","ewrkaoe","flf","fqrwxqoh","fwl","fxtda","gfiurvro","gjfxqtcm","hfucle","hgncss","hxcqo","imqajzmd","jbs","jd","jdxe","jfksxit","jopuyl","jvjcp","jvoetnv","kgsbid","kqecblp","ktnfvuxs","lkyt","lwz","mkpejmc","mnta","mtq","mwxt","mygkan","nxpjnpxx","opnzbamc","orl","oz","pefigm","pfmk","pisogyw","pldbnjmg","qdv","qgamdor","qzy","rqfqitq","rqoiq","rww","swxta","teikq","tkihurez","tnznoze","tqlkth","tuh","ucspb","uptrf","vswzpfsq","vvojqoj","wwkehwr","xbbehmg","ybyg","yfot","yrjjx","ysrfvgm","zlbeyfm","znsm","zrfs","auepbxw","az","blmfcue","bnbzews","bpmmu","btwod","bwwagl","cafsch","cfgraxi","dckagg","eaq","ebuh","elc","eye","ezoo","fveo","fyfqq","gdkl","gjnnnu","gnmidgfy","gvocnmn","gxca","hlgdmmtd","iyafjqy","jcrlkex","jhw","jlhbt","jxcxle","kedjjih","kmlmtqi","kpjoqlfk","lxqz","mjbraj","mlzsi","nd","ndoulo","ngxfbcx","nn","nwrhi","nwwconn","oefph","ori","orrnrucr","otm","pby","pdt","pinbobm","poums","ppargdq","pucj","pzlvd","qamjip","qgy","qhnvm","qjgmbkns","qmwwgspe","quducpw","rqiltgfz","sc","se","sifc","swfap","tgrt","tnscl","towposl","troorwso","ttdty","ttn","tvuiceq","unwcvu","uwrpln","vama","vhva","vrq","vzxd","wbt","wj","wpar","wste","xg","xtxyavgn","xxzx","yedee","ywk","zorzy","zro","zu","akiidjku","ax","dnzyp","ehorh","eln","fansrxhk","gmigzal","gunwv","kegqhue","kiqtgn","mjcoq","mnrnn","nccyp","njklfyjs","npqsr","nszmxqz","oqdqo","pfasuoip","qbxfug","qyleqwm","rdnxar","shldua","wznldtn","xcgzqfsx","yroum","yx","ab","aguj","ahcqy","ausucpe","bndes","bs","caelq","cirgqpz","daxa","ddyjrtih","dnqpg","dtkkt","edjbvrm","epl","epww","exk","eyxx","fluav","fmlnwqqj","fmwigv","fymxxvam","gawwbh","geu","gionyw","gk","hhrrrwg","hprav","hq","iadbcxt","ic","idvecxv","ifgugc","iki","iolks","itdibyfn","iuusxswh","iyv","izn","izumin","jjkjhrpu","jybykgsw","jzpf","kctit","kfuxfj","kpb","kyw","lcmx","lgerc","loklbdum","lrffbwt","lxgm","mmztt","mnj","mqriwta","mrd","nanpcpy","nhwg","nmztql","nntwxa","nzxubcff","oagi","ofuvpvc","pqxdbhbf","prcfwr","pvwgd","qh","qk","qlgdfb","qsiblhpc","quik","rdgrdybj","rtgz","rvfget","rvin","sih","sq","synprmt","szckg","szmltbbt","tgqjtn","tlj","tninf","tqttke","tsccadjt","uer","uidn","uqg","usmkvic","veak","vga","wc","wdomfuhs","wghu","wt","wuv","xhfzfcew","xl","xqx","yjcqkjzd","ykmcm","yucyjgl","yxp","zffdcd","zhu","zwy","dh","hi","hx","bbsk","bkjkcmn","bocnes","boqi","cbke","dfebt","dxrquzro","dylm","ekyrht","fiivivd","fncgyy","gbtde","hg","hgyzfxzz","hmqg","hyxbzoaq","is","itv","ivfndo","jccbede","jfnw","jjpm","jpggmj","jsxzdgd","lktx","loqmgb","luxuvqjj","lxgsrvu","mlbsq","odknxgdz","qeni","qiqfxgo","qivhuoas","qoxeqmk","qvgi","sjfpmyk","tcjweip","uhljndcc","ujujjiqi","ukdxpj","upeaxrwv","vajsdzax","vnyujcfp","wmkakss","xkuakbf","acxti","amdi","aoqitkd","ap","aypgnzt","bbuwooj","blt","bvqrl","bzxvy","ccpwsil","ccxvrcb","cjvqp","cngc","cpymbdg","crg","cspukhav","cwycrwl","dau","dbs","df","dnurtzs","dowioug","ds","dzdg","eggph","ehix","elf","eyqmaue","ezzmwu","fjsnn","fldsibh","fm","gaoelk","gr","guydmcik","gx","hbkrv","hmkujslv","hnigso","hrwfjmgp","hxyj","ib","ibojwdlc","iwrfl","ja","jctwn","jfmxy","jfur","jhfoihfr","jiogsz","jwyuycnq","jz","kzjmdnr","lacb","lejp","lgibxre","lidxfhi","ltijio","lu","mcghu","morqlzr","mottt","mzffx","nfidyyad","nlhuk","npraml","nqhjun","nxtrruao","oacqhj","ohwt","okqkgoxz","omml","onnm","otig","owsunwds","pa","pdfco","pdwg","pgc","phjgws","pizce","pjzvi","ppwpwbt","pqsis","psvsy","pua","punaah","pwxtip","qfz","qhekm","qnhuq","qw","rdpqf","rjf","rr","rye","sczwwvq","sd","slfljhih","svn","tdj","tioty","tkx","tkyibn","to","tvqqd","txtcupu","uauuipd","uclh","udua","uglbaymo","unmkvluu","uogcx","uywv","vigxzuc","wnocztq","wpnup","wpyc","wvhik","wwt","xcsv","xhw","xlmqrr","xwgfzq","yi","ymrde","yrantf","zcqcq","zgd","zmdc","zmoplb","zpv","zq","abcsi","ag","ail","akhuwa","atopup","axcu","banoxg","bcb","bcix","bcju","bekvmrz","bhhren","bhk","bhrvre","bjehuqnc","bjer","bmgr","bogyvd","bomvtw","bpsh","brvr","bv","byzjgm","casllmd","cbz","cfpeljf","cgfk","ckbpeoeq","cslwub","cuschcn","cvmadnl","cvp","dbje","dfsa","dmbl","dnpeub","dpnwcb","dqqr","dwdopd","eekmoito","eekv","emmgkkhp","eng","eqxexb","erdgir","eypmgxgt","faa","fhev","fly","fma","fpjrc","ftm","fu","fvvgky","gdezmdmy","gfgz","gho","gkvh","gmfnh","gmucgwzn","gohq","gonrzz","gqqp","gugqrygj","gxkfyn","gxvmefzf","gywv","hgra","hhuihm","hicn","hjyr","hle","hnhuelbq","hocgbo","htvl","hwgpdql","hxgqfr","hzxwn","iflujdaz","ilmw","ilohs","imkcjei","impjck","itmi","iv","ixziptn","jajdgpd","jkgnpcmy","jrnn","jufdmqq","jwgnbby","jxsbwep","klvmybv","kzuxxuv","lcqqavi","lgi","lhadgwy","lhsfo","lpzx","lwbwvf","lx","lxkih","lygatsp","maad","mdt","mdzafgt","mongbj","mrnxt","msbfure","msv","mtazym","mtqr","mxaoluup","mxkbsygz","mywdwp","mzbemiqk","nbzlxa","ndhnb","ngrt","nnjkw","npjatiru","nqmtodz","nqxq","nvgz","nvsg","nwcfu","oamuqnn","obc","obgnikyk","obn","of","ofb","ofe","ogv","oip","onigk","oucyynen","ov","owutwnmo","oypr","pajyswp","paytzh","pcbiean","pejxja","pew","phvrj","pixf","pkn","poo","psmg","ptxme","pwvjbqoh","qdknzvz","qejef","qep","qevdsqe","qf","qhzzv","qiocb","qrtlv","qruojqfq","qtnhx","qvldbq","qxqnbega","qzlkf","razibg","rc","rjqybepp","rllvrsn","rmdfim","rmtssud","ruhh","rx","rydcayh","sda","sek","siufqxgi","slwgr","smbfsau","smswqjg","ssma","swvkl","taai","tc","tdli","thitffou","tlfsyvf","tolmunph","tozixprd","tphnp","tsonv","tssqjhrz","tvhzeg","ty","tyf","ua","ugzz","uhvtft","unh","uo","uodhgmoh","uym","vbe","vfm","vfph","vlo","vqjjtpc","vzpjq","vzrhgch","wadkxzaq","wbgt","wep","wgv","whlzp","wjl","wmyvts","wurqumc","xcrvuf","xebuy","xfamcep","xfi","xhpuibm","xjaxedrn","yludmuvy","ymiankek","yp","ypmdjqmp","yykbwp","yytgk","yzxk","zauvu","zb","zgnrs","zgoqvqz","zhzuc","zotgq","zotpousi","zrs","zwdh","zzanmic","aidj","anb","atgtnuog","btviega","caraehar","cax","dbccjtn","dydrhp","eamu","evyxyc","exhawx","frzuov","fwjc","fxsjz","fxvghc","gbrawxjn","gryfg","guwf","hoijsvis","hzgfj","jr","kbqjve","lgob","lhefs","lkscwer","lrgx","nclq","ngszdlwk","nv","nvigfg","obequ","obt","pkbf","pl","pqkqu","qnhrzixn","qxr","skfvk","swd","tdiqnbz","tllkekk","tmhvbnfb","twnw","ubkoyy","ubzouynt","ujfbdx","vkjrtxh","wdrbqfw","wg","woengf","xco","xfxcwi","xzqcpksd","ybfy","yby","yqffhoe","ywlidkmd","abyzjgj","advz","bfcpzg","bn","boxqint","bp","bskohgcm","bstbl","bvyuzl","bwqquuuy","bzbmvbu","calqw","cirgnf","cqpehh","cqseggpo","cx","cyeovix","dgsgi","djhwimr","dwkxte","eolyi","eshmakm","fxhsuu","glmd","haqyfufo","heiqx","hezii","hgslg","hjuz","hmcnloo","hov","htfz","idojlqgn","ikis","ireqzx","jffujhf","kbb","kesw","kjp","kok","kypa","laaupkd","lqccyebo","lrwrhwbf","lvaskmbl","lw","lwvhry","mh","mndejm","motu","mpufpz","nkbstopi","nunuv","oh","okgd","ooto","orycagl","pcyf","psydra","qedtvx","qgdd","qweg","rxngis","sala","shd","svhrqh","svwis","swbynzol","tdzwoaw","tjvglo","tksicthj","tpmuhnpl","tzy","uem","uigd","va","vg","vxes","vxpwzfs","wfgtp","whrwcd","wn","xfb","xlht","xrpnfdu","xy","yhyxn","zhxbx","zirggxfr","zn","aduvdf","amsp","bewnpr","bimnk","bjvvcma","bjxjnzo","bnztdp","bzm","bzscd","cakmupph","cc","cowyr","cu","da","dgsotgp","dhpixrez","dih","dlloq","dzogfrbd","ecwxx","ei","ejqzp","eujx","exdcbc","ezoep","facmg","fkfkvumj","flplskcf","gcc","gcz","gozmrtf","gtwlojc","gypnt","hnrqe","hqyhjwcs","ixo","iymucwgc","izhgd","jdhuyw","jfdiy","jrttwgmf","klev","ks","ksvn","ksyk","ktco","kuggace","kuq","kut","kzlli","lj","lkgxgyf","loktiwm","lqkgv","lt","lvfjcpv","mba","mgvo","mmgrcw","mo","mrbp","mtgczd","mtig","myagutw","nfdk","nfpzchsl","nhk","nip","njx","nnaq","nsy","nui","ohoc","om","oqgjtkpb","oscyv","otmzrkn","ox","oywzb","patv","phxi","pnandszg","prbgczgh","ptdlwxk","pvcnha","pzkohqdn","qcyfr","qfbruv","qxctbz","qzmubsv","rbo","ronsbg","rugqp","ruxftedt","rzaz","sgmlp","sklinw","tbuexx","tinqtyl","trgrmy","ubfas","uihlvhq","urggrtl","utiepy","vemqwifa","vfce","vlvqrwpx","vpfksv","vrccpnr","vsmbrjv","vuvc","wdpwfut","whhr","wklrx","wnc","wpeadaiz","wqldor","wxnmbk","xiyd","xmhfsbm","xntljtp","xoawcqub","xsu","xtkc","yaikkatu","ycp","ypfb","yumjw","yvyhc","zhnuj","zmzal","zp","zrl","zt","zzbuml","am","apszy","aq","bi","blcg","bqv","chb","cqruaif","cwgjknk","dhacxffh","dinpw","dmxrxgnk","edro","emoqk","fcaac","fcjnds","ffmo","fjadaqt","fkg","fnik","foi","gflws","gmfeno","gmvy","hiyu","hl","hmrxruun","hpz","hqsq","hyoffeeb","ikav","il","iprjcg","ivzx","jenhpmem","kxyswlaq","kyujid","lch","ldeepq","lsklp","mctn","mhltzglr","mjdjckq","mkvflt","msymhf","mvf","nliiw","oacines","okji","owefypt","px","pzacgh","qel","qgchrhoo","qgp","rf","rvtwlv","sakluw","slg","sn","suoyxbym","sur","svalyg","svjbchp","swjyxt","thccemp","tpulhcb","trbc","tsxgheia","tu","ubucsa","ufyjwcji","uzd","vadgz","vqrrj","wa","wagtzlvz","wdfuie","wiq","wkwke","wxe","wysy","xbz","xows","xsbl","ymoxhzh","zlt","zm","zmvjyrp","agpr","dalc","dvmbaeh","dzqyhn","eiuni","eoxc","eqosy","fanf","fjci","fw","goeygcn","gskeuik","haxjp","hazrtf","hqyud","hrjyuj","idxxxc","igua","iz","jitq","kscgflwx","kzdue","lgo","mddvlopv","me","molnvq","muz","okb","oltschh","pmrabpky","qfbkfb","qkdv","qlcds","rey","shx","tbvm","te","tejmekki","tjhajpeg","tqlwjser","uiy","umkejtes","wlfhbjuo","wmit","wpd","xi","xyfom","zlpunqan","akpb","an","aynrb","azgqkiu","azuo","bdfnevzp","bl","bmqmmbub","bqyvh","bslqa","bxmvg","byiio","cfvfgg","cyowdrfi","dbtga","dgr","dkcgbd","dvwlnq","eb","elproupv","evzs","faqi","feset","ffjsdh","fhz","fkbgzy","fkvq","fotdqiw","fv","giyrrvu","gjmb","gl","gund","guvps","gvbx","hblf","htr","hzccgtxe","isi","iuwbvbth","jshd","jtwz","jxqxmuv","kano","keiito","kpn","lhxgo","lm","lotlbz","ltmdzt","luwe","lyyuz","mdow","miticfmd","mrmmc","mxcbrrlu","njxzj","nrh","nxzhw","ogm","oiyzmj","ophdfqt","pbyrgdkw","phprvuc","prrgyyo","qe","qqasqg","rfxen","rgdkvp","rjtayu","rq","rudz","sswifa","tmje","tmrqzd","tobdcmmy","tsmybrt","twiac","tzeomj","uqur","vdaasfo","vq","whsm","wnfwsr","xougy","yhvcxb","ypre","yyuf","zflvedue","zfqo","zhwr","znwkkr","agkgdkob","aqo","bepioryw","bqosxv","cqi","crojpx","culbbu","dpvnidbl","dtfga","eremwj","esxxk","fuy","fy","gfxw","gkmylf","gpi","imjp","ipcaze","iqqmh","ivr","ju","kcrqgh","ke","kgenhjk","kjis","ksrleqo","lhih","lirxehxf","lkr","lrtignxm","mcx","nsh","ooqnxztg","os","owne","pxvwjr","pytoyia","rltqagxd","rqb","rtt","rvsfrt","sbaiyxi","sggr","sktvon","smihtt","so","syu","szb","udcqlh","ukgr","ul","unffvs","up","uqjrmmvy","vwadeg","wodgas","xbuwoc","xfbas","xlop","yeekpod","zc","zyy","od","jf","um","xe","hb","wr","bd","ri","et","bt","fl","ph","mr","yf","kg","ut","xfc","zk","ek","kk","lp","kl","sr","jq","qy","hs","jx","xz","lb","qp","ob","ru","vr","zl","xp","kz","bc","hc","aa","vu","hm","ly","ta","wf","vz","bf","gm","op","ze","j","d","c","x","l","r","t","f","w","i","z","a","v","g","m","p","s","b","n","k","e","h","y","o","u","q"]
    # vs = ["abcsi","abyzjgj","advz","ag","agkgdkob","agpr","ail","akhuwa","akpb","am","an","anb","apszy","aq","aqo","atopup","axcu","aynrb","azgqkiu","azuo","banoxg","bc","bcb","bcix","bcju","bdfnevzp","bekvmrz","bepioryw","bfcpzg","bhhren","bhk","bhrvre","bi","bjehuqnc","bjer","bl","blcg","bmgr","bmqmmbub","bn","bogyvd","bomvtw","boxqint","bp","bpsh","bqosxv","bqv","bqyvh","brvr","bskohgcm","bslqa","bstbl","bt","btviega","bv","bvyuzl","bwqquuuy","bxmvg","byiio","byzjgm","bzbmvbu","calqw","caraehar","casllmd","cax","cbz","cc","cfpeljf","cfvfgg","cgfk","chb","cirgnf","ckbpeoeq","cqi","cqpehh","cqruaif","cqseggpo","crojpx","cslwub","cu","culbbu","cuschcn","cvp","cwgjknk","cx","cyeovix","cyowdrfi","dalc","dbccjtn","dbje","dbtga","dfsa","dgr","dgsgi","dhacxffh","dinpw","djhwimr","dkcgbd","dmbl","dmxrxgnk","dnpeub","dpnwcb","dpvnidbl","dqqr","dtfga","dvmbaeh","dvwlnq","dwdopd","dwkxte","dydrhp","dzqyhn","eamu","eb","edro","eekmoito","eekv","eiuni","ek","elproupv","emmgkkhp","emoqk","eng","eolyi","eoxc","eqosy","eqxexb","erdgir","eremwj","eshmakm","esxxk","evyxyc","evzs","eypmgxgt","ezoep","faa","fanf","faqi","fcaac","fcjnds","feset","ffjsdh","ffmo","fhev","fhz","fjadaqt","fjci","fkbgzy","fkg","fkvq","fly","fma","fnik","foi","fotdqiw","fpjrc","frzuov","ftm","fuy","fvvgky","fw","fwjc","fxhsuu","fxsjz","fxvghc","fy","gbrawxjn","gdezmdmy","gfgz","gflws","gfxw","gho","giyrrvu","gjmb","gkmylf","gkvh","gl","glmd","gmfeno","gmfnh","gmucgwzn","gmvy","goeygcn","gohq","gonrzz","gqqp","gryfg","gskeuik","gugqrygj","gund","guvps","guwf","gvbx","gxkfyn","gxvmefzf","gywv","haqyfufo","haxjp","hazrtf","hb","hblf","heiqx","hezii","hgra","hgslg","hhuihm","hicn","hiyu","hjuz","hjyr","hl","hle","hm","hmcnloo","hmrxruun","hnhuelbq","hocgbo","hov","hpz","hqsq","hqyud","hrjyuj","htfz","htvl","hwgpdql","hxgqfr","hyoffeeb","hzccgtxe","hzgfj","hzxwn","idojlqgn","idxxxc","iflujdaz","igua","ikav","ikis","il","ilmw","ilohs","imjp","imkcjei","impjck","ipcaze","iprjcg","iqqmh","ireqzx","isi","itmi","iuwbvbth","iv","ivr","ivzx","ixziptn","j","jajdgpd","jenhpmem","jffujhf","jitq","jkgnpcmy","jrnn","jshd","jtwz","ju","jufdmqq","jwgnbby","jx","jxqxmuv","jxsbwep","kano","kbb","kbqjve","kcrqgh","ke","keiito","kesw","kg","kgenhjk","kjis","kjp","kk","kl","klvmybv","kok","kpn","kscgflwx","ksrleqo","kut","kxyswlaq","kypa","kyujid","kz","kzdue","kzuxxuv","laaupkd","lb","lch","lcqqavi","ldeepq","lgi","lgo","lgob","lhadgwy","lhefs","lhih","lhsfo","lhxgo","lirxehxf","lkr","lkscwer","lm","lotlbz","lp","lpzx","lqccyebo","lrgx","lrtignxm","lrwrhwbf","lsklp","ltmdzt","luwe","lvaskmbl","lw","lwbwvf","lwvhry","lx","lxkih","lygatsp","lyyuz","maad","mctn","mcx","mddvlopv","mdow","mdt","mdzafgt","me","mh","mhltzglr","miticfmd","mjdjckq","mkvflt","mndejm","mo","molnvq","mongbj","motu","mpufpz","mrmmc","mrnxt","msbfure","msv","msymhf","mtazym","mtqr","muz","mvf","mxaoluup","mxcbrrlu","mxkbsygz","mywdwp","mzbemiqk","nbzlxa","nclq","ndhnb","ngrt","ngszdlwk","njxzj","nkbstopi","nliiw","nnjkw","npjatiru","nqmtodz","nqxq","nrh","nsh","nunuv","nvgz","nvigfg","nvsg","nwcfu","nxzhw","oacines","oamuqnn","ob","obc","obequ","obgnikyk","obn","obt","od","of","ofb","ofe","ogm","ogv","oh","oip","oiyzmj","okb","okgd","okji","oltschh","onigk","ooqnxztg","ooto","ophdfqt","oqgjtkpb","orycagl","os","oscyv","otmzrkn","oucyynen","ov","owefypt","owne","owutwnmo","oypr","pajyswp","paytzh","pbyrgdkw","pcbiean","pcyf","pejxja","pew","ph","phprvuc","phvrj","pixf","pkbf","pkn","pl","pmrabpky","poo","pqkqu","prrgyyo","psmg","psydra","ptxme","pwvjbqoh","px","pxvwjr","pytoyia","pzacgh","qdknzvz","qe","qedtvx","qejef","qel","qep","qevdsqe","qf","qfbkfb","qgchrhoo","qgdd","qgp","qhzzv","qiocb","qkdv","qlcds","qnhrzixn","qp","qqasqg","qrtlv","qruojqfq","qtnhx","qvldbq","qweg","qxctbz","qxqnbega","qxr","qy","qzlkf","razibg","rbo","rc","rey","rf","rfxen","rgdkvp","ri","rjqybepp","rjtayu","rllvrsn","rltqagxd","rmdfim","rmtssud","ronsbg","rq","rqb","rtt","ru","rudz","ruhh","rvsfrt","rvtwlv","rx","rxngis","rydcayh","sakluw","sala","sbaiyxi","sda","sek","sggr","shd","shx","siufqxgi","skfvk","sktvon","slg","slwgr","smbfsau","smihtt","smswqjg","sn","so","ssma","sswifa","suoyxbym","sur","svalyg","svhrqh","svjbchp","svwis","swbynzol","swd","swjyxt","swvkl","syu","szb","ta","taai","tbvm","tc","tdiqnbz","tdli","tdzwoaw","te","tejmekki","thccemp","thitffou","tjhajpeg","tjvglo","tksicthj","tlfsyvf","tllkekk","tmhvbnfb","tmje","tmrqzd","tobdcmmy","tolmunph","tozixprd","tphnp","tpmuhnpl","tpulhcb","tqlwjser","trbc","tsmybrt","tsonv","tsxgheia","tu","tvhzeg","twiac","twnw","ty","tyf","tzeomj","tzy","ubkoyy","ubucsa","ubzouynt","udcqlh","uem","ufyjwcji","ugzz","uhvtft","uigd","uiy","ujfbdx","ukgr","ul","um","umkejtes","unffvs","uodhgmoh","up","uqjrmmvy","uqur","ut","uym","uzd","vadgz","vbe","vdaasfo","vfm","vfph","vg","vkjrtxh","vqjjtpc","vqrrj","vr","vwadeg","vxes","vxpwzfs","vz","vzpjq","vzrhgch","wa","wadkxzaq","wagtzlvz","wbgt","wdfuie","wdrbqfw","wep","wfgtp","wg","wgv","whlzp","whrwcd","whsm","wiq","wjl","wklrx","wkwke","wlfhbjuo","wmit","wmyvts","wn","wnfwsr","wodgas","woengf","wpd","wpeadaiz","wurqumc","wxe","wysy","xbuwoc","xbz","xco","xcrvuf","xe","xebuy","xfamcep","xfb","xfbas","xfi","xfxcwi","xhpuibm","xjaxedrn","xlht","xlop","xougy","xows","xp","xrpnfdu","xsbl","xy","xyfom","xz","xzqcpksd","ybfy","yby","yeekpod","yhvcxb","yhyxn","yludmuvy","ymiankek","ymoxhzh","ypmdjqmp","ypre","yqffhoe","ywlidkmd","yykbwp","yytgk","yyuf","yzxk","zauvu","zb","zc","ze","zflvedue","zfqo","zgnrs","zgoqvqz","zhwr","zhxbx","zhzuc","zirggxfr","zk","zl","zlpunqan","zlt","zm","zmvjyrp","zn","znwkkr","zotgq","zotpousi","zrs","zt","zwdh","zyy","aa","bf","d","g","gm","hc","l","r","t","v","vu","a","b","i","m","n","op","x","k","o","p","q","s","w","z","u","e","h","y"]
    # us.sort(); vs.sort()
    # print(f'us: {us}')
    # print(f'vs: {vs}')
    # print(f'len us: {len(us)}')
    # print(f'len vs: {len(vs)}')
    e = Edge(0, 1); f = Edge(1, 2)
    de = {e: 1, f: 2}
    print(f'de = {de}')
    print(f'e = {e}')
    print(f'kwargs = {0}')
    ppt() if False else ppf()

