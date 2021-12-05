class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [0] * len(rooms)
        keys = [0] * len(rooms)
        self.mergeKeys(keys, rooms[0])
        while

    def hasRoomToGo(self, visit_array, key_array):


    def mergeKeys(self, cur_keys, new_keys):
        for key in new_keys:
            if cur_keys[key] == 0:
                cur_keys[key] = 1


