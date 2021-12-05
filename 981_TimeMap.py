class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 初始化key 和value list的字典
        self.key_vlist_map = {}
        # 初始化key + ts，保存value对应的index,这样存value的时候就不用排序
        self.key_ts_index_map = {}



    def set(self, key: str, value: str, timestamp: int) -> None:
        value_list = []
        this_key = key + "_" + str(timestamp)
        if self.key_vlist_map.__contains__(this_key):
            value_list = self.key_vlist_map.get(this_key)
        value_list.append(value)
        self.key_ts_index_map[this_key]

    def get(self, key: str, timestamp: int) -> str:
        for to_get_ts in range(timestamp, 0, -1):
            try:
                if self.key_vlist_map.get(self.key_ts_index_map)

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
test_dict = {}
print(test_dict.get(5))