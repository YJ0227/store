'''
有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
'''

class notebook_pc:
    __screen_size = 0
    __price = 0
    __cpu = ''
    __memory_size = 0
    __standby_time = 0

    def setscreen_size(self, screen_size):
        self.__screen_size = screen_size
    def setprice(self, price):
        self.__price = price
    def setcpu(self,cpu):
        self.__cpu = cpu
    def setmeory(self, meory):
        self.__memory_size = meory
    def setstandby(self,standby):
        self.__standby_time = standby
    def getscreen_size(self):
        return self.__screen_size
    def getprice(self):
        return self.__price
    def getcpu(self):
        return self.__cpu
    def getmemory(self):
        return self.__memory_size
    def getstandby(self):
        return self.__standby_time

    # 行为
    def typing(self):
        print("打字")
    def play_games(self):
        print("打游戏")
    def watch_vidio(self):
        print("看视频")
    def introduce(self):
        print("这款电脑屏幕%s寸，价格：%s￥，CPU型号：%s，内存大小%sG，待机时长%s小时"%(self.__screen_size,self.__price,self.__cpu,self.__memory_size,self.__standby_time))

a=notebook_pc()
a.setscreen_size(15)
a.setcpu('Core-i7')
a.setmeory(8)
a.setprice(5680)
a.setstandby(10)
a.typing()
a.introduce()