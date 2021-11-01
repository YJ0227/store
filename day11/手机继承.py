class OlderPhone():
    __brand = ""   # 品牌

    def setBrand(self, brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand

    def call(self, number):
        print("正在给%s打电话..." % number)

class NewPhone(OlderPhone):
    def call(self, number):
        print("语音拨号中...")
        super().call(number)

    def introduce(self):
        print("品牌为：%s的手机很好用..." % self.getBrand())

phone = NewPhone()
phone.setBrand("华为")
phone.introduce()
phone.call('18211112222')
