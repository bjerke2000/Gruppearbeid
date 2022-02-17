from asyncio.windows_events import NULL


class disk():
    def __init__(self,size,pos) -> None:
        self.__size = size
        self.__pole = 0
        self.__pos = pos

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        self.__size == value

    @property
    def pole(self):
        return self.__pole
    
    @pole.setter
    def pole(self, value):
        self.__pole == value

    @property
    def pos(self):
        return self.__pos
    
    @pos.setter
    def pos(self, value):
        self.__pos == value



d1 = disk(0,0)
d2 = disk(1,1)
d3 = disk(2,2)
d4 = disk(3,3)

disk_list = [d1, d2, d3, d4]
poletops=[0,NULL,NULL]

def mover(disk_list):
    disk_move_helper(len(disk_list)-1, 2, 0, 1 )
    print("finished")

def disk_move_helper(disk, destination, start, aux):
    if poletops[start] != disk_list[disk].size:
        disk_move_helper(disk-1, start=start, destination=aux, aux=destination)
    else:
        disk_list[disk].pole = destination
        poletops[destination]=disk_list[disk].size
        print(f"Moving disk{disk_list[disk].size} to pole {destination}")
    if disk_list[disk].size!=0:
        disk_move_helper(disk-1, destination=destination, aux=start, start=aux)

mover(disk_list)



    
    
    
