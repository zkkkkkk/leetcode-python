def goodsInputer():
    newGoods = []
    infoGoods = []
    newGoods = input("输⼊商品信息(商品名称、单价,销售数量),直接输入，用逗号隔开(回车退出):").split(',')
    name = newGoods[0]
    num = 0
    while newGoods != [""]:
        # 查库存里有没有这个商品的信息
        foundFlag = 0
        for singleGood in infoGoods:  # 遍历每一个商品
            if singleGood[0] == newGoods[0]:  # 找到名字相同的时候，改单价和销售数量
                singleGood[1] = (int(singleGood[1]) + int(newGoods[1])) / 2
                singleGood[2] = int(singleGood[2]) + int(newGoods[2])
                foundFlag = 1
        # 判断一下有没有找到过，找到过那信息已经修改过了；没找到商品的时候加入商品
        if foundFlag == 0:
            infoGoods.append(newGoods)
        newGoods = input("输⼊商品信息(商品名称、单价,销售数量),直接输入，用逗号隔开(回车退出):").split(',')
        # 判断一下单价和销售数量，是不是数字，有输入错的检查要求；因为计算过程中转成数字计算了，所以这里得先转回字符串再判断
        if newGoods != [""] and not (str(newGoods[1]).isdigit and str(newGoods[2]).isdigit):
            newGoods = input("输⼊商品信息(商品名称、单价,销售数量),直接输入，用逗号隔开(回车退出):").split(',')
    # list转成元组，元组不可变
    tupleGoods = tuple(infoGoods)
    return tupleGoods


def goodSaleQtyRanker (x, u):
    #把tuple转成list才能排序
    listGoods = list(u)
    '''排序函数
        key这个参数要是一个函数，用来排序；
        这里的意思是 listGoods这个待排序的列表，里每一个元素是[商品名字,商品价格，商品销量]。
        排序我们实际是需要根据每一行进行排序，一行里数据比较复杂， 但是排序我们只需要一个值，那么key这个函数的作用，就是从一行里把用来排序的字段提取出来。
        所以
        方法一：
            lambda x(等价于函数的参数):x[2](等价于函数的返回值)
        方法二：
            def getSortKey(x)
                return x[2]
        '''
    listGoods.sort(key = lambda sortKey:sortKey[2], reverse=True) ## 默认是从小到大，我们取销售量大的 需要反转
    #
    rank = 1 # 第一行排第一
    for good in listGoods: #从销售量大的开始，一个个查找；没找到的话排名就+1
        if good[0] == x[0]:
            return rank # 找到了直接返回，
            # break 其实这样写更优雅，跳出for循环；统一在最后返回，一个函数只有一个return是最合理的
        rank += 1
    return rank




def goodsFinder(x, y):
    for singleGoods in y:
        if x == singleGoods[0]:
            tupleGoods = tuple(singleGoods[0:])
            return tupleGoods
    else:
        print('没有找到该商品')


goodsInfoTuple = goodsInputer()
findResult = goodsFinder("a", goodsInfoTuple)

print("查找的商品 a 销量排名为" + str(goodSaleQtyRanker(findResult, goodsInfoTuple)))