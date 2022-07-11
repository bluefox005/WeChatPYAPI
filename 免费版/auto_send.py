# 如果你是Python36。请删除37、38、39的pyd文件，其他版本同理
from WeChatPYAPI import WeChatPYApi

import time
import logging
from queue import Queue
import os

# 当前目录路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(level=logging.INFO)  # 日志器
msg_queue = Queue()  # 消息队列


def on_message(msg):
    """消息回调，建议异步处理，防止阻塞"""
    print(msg)
    msg_queue.put(msg)


def on_exit(wx_id):
    """退出事件回调"""
    print("已退出：{}".format(wx_id))

def list_to_file(my_list):
    with open('test.txt', 'w',encoding='utf-8') as f:
        for item in my_list:
            f.write("%s\n" % item)

def main():
    # 初次使用需要pip安装三个库：
    # pip install requests
    # pip install pycryptodomex
    # pip install psutil
    #
    # 查看帮助
    help(WeChatPYApi)

    # 实例化api对象
    w = WeChatPYApi(msg_callback=on_message, exit_callback=on_exit, logger=logging)

    # 启动微信
    # w.start_wx()
    w.start_wx(path=os.path.join(BASE_DIR, "login_qrcode.png"))  # 保存登录二维码

    # 这里需要阻塞，等待获取个人信息
    while not w.get_self_info():
        time.sleep(5)

    my_info = w.get_self_info()
    self_wx = my_info["wx_id"]
    print("登陆成功！")
    print(my_info)

    # 拉取列表（好友/群/公众号等）第一次拉取可能会阻塞，可以自行做异步处理
    # 好友列表：pull_type = 1
    # 群列表：pull_type = 2
    # 公众号列表：pull_type = 3
    # 其他：pull_type = 4
    lists = w.pull_list(self_wx=self_wx, pull_type=2)
    list_to_file(lists)
    # print(lists)

    # 获取群成员列表
    # lists = w.get_chat_room_members(self_wx=self_wx, to_chat_room="123@chatroom")
    # print(lists)

    # # 发送文本消息
    # w.send_text(self_wx=self_wx, to_wx="filehelper", msg='作者QQ:\r437382693')
    # time.sleep(1)
    #
    # # 发送图片消息
    # # w.send_img(self_wx=self_wx, to_wx="filehelper", path=r"C:\1.png")
    # # time.sleep(1)
    #
    # # 发送卡片链接
    # w.send_card_link(
    #     self_wx=self_wx,
    #     to_wx="filehelper",
    #     title="QQ",
    #     desc="437382693",
    #     target_url="http://baidu.com",
    #     img_url="http://img-haodanku-com.cdn.fudaiapp.com/oimg_643855036504_1627291311.jpg_310x310.jpg"
    # )
    # time.sleep(1)
    #
    # # 处理消息回调
    # while True:
    #     msg = msg_queue.get()
    #
    #     # 收款
    #     if msg["msg_type"] == 490:
    #         is_recv = msg["detail"]["is_recv"]
    #         if is_recv:
    #             # 收款
    #             w.collection(self_wx=self_wx, msg_data=msg)
    #
    #             # 退款
    #             # w.refund(self_wx=self_wx, msg_data=msg)

    test = {'26387907882@chatroom': "UBIF团购群"}
    for k, v in test.items():
        # 测试功能   UBIF团购群
        print (k,v)
        # w.send_text(self_wx=self_wx, to_wx=k, msg='蒙城UBIF电讯生活馆保健🌈系列❗\n'
        #                                               '小米智能可视采耳棒👂，无线wifi高清📶，300万高精内窥镜🔍，👨‍👩‍👧‍👦适合全家老少💯\n'
        #                                           '🔥小米精选，肯定有你喜欢的#小程序://微商店Lite/这家店超火你也来看看/SnxdoTH4NcmKfGu\n')
        # time.sleep(10)
        # w.send_img(self_wx=self_wx, to_wx=k, path=r"C:/Users/huaow/Desktop/ZHAO YUE/小米/小米蜂鸟可视挖耳勺/微信图片_20220112212712.jpg")
        # time.sleep(10)
        # w.send_img(self_wx=self_wx, to_wx=k, path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")

        # w.send_text(self_wx=self_wx, to_wx=k, msg='👋告别渣网，一家人👨‍👩‍👧‍👦的通讯方式📶不能都放一个篮子里🈲\n'
        #                                               '🔥推荐一卡双号QC短期优惠促销❗12G/40$，🉑无限电话短信，🈶中加长途双向任打，🈚合约。\n'
        #                                           '📢联系4389379780或加微信ubreakifix_helpdesk了解更多详情。\n')
        # time.sleep(10)
        # w.send_img(self_wx=self_wx, to_wx=k, path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/repair.jpg")

    send_daily = {'104060697@chatroom': "山东人商务及生活交流群", '216177289@chatroom': "文苑清风诵读好声音",
                  '2132313807@chatroom': "精彩信息共享交流群",
                  '228563099@chatroom': "ADOGO商业广告发展群", '2238310305@chatroom': "北极商盟之广告与生意经",
                  '2420078280@chatroom': "装修咨询，房地产信息",'355757487@chatroom': "源垒订餐龙虾🦞团购群",
                  '2505455504@chatroom': "TD银行投资讲座五群", '2494010639@chatroom': "欢乐网络教室",
                  '2506294180@chatroom': "便利店主互助群",
                  '26001620259@chatroom': "华总会《蒙华同春》春晚三群", '27595706872@chatroom': "市场广告，资源共享群",
                  '2696310183@chatroom': "蒙城物品2⃣️群加你朋友进来",
                  '316690492@chatroom': "南岸瑞和商业广告群", '346486084@chatroom': "蒙城休闲文化活动召集",
                  '336646094@chatroom': "蒙特利尔·房屋租赁",
                  '4553368439@chatroom': "中外企业交流群（1）", '5914992836@chatroom': "北美文化传媒",
                  '6093070779@chatroom': "枫花雪乐", '6174030823@chatroom': "快快乐乐吃吃吃", '96571598@chatroom': "粤菜吃货群欢迎大家围观哦",
                  '7625950767@chatroom': "蒙城顺风车，边境，多伦多搬家接送", '5281311408@chatroom': "蒙城租房找房二手交易生活信息群",
                  '198500794@chatroom': "蒙城医疗服务信息群",
                  '25757847006@chatroom': "春节香港盆菜团购群", '26300505418@chatroom': "蒙特利尔代理军团",
                  '27167818625@chatroom': "加拿大徽商总会",
                  '6073020567@chatroom': "蒙城二手交易群",
                  '6067993520@chatroom': "蒙城活动分享群", '6174161612@chatroom': "南岸BROSSARD分享群",
                  '6223237732@chatroom': "蒙城人脉圈",
                  '7632165442@chatroom': "蒙特利尔青年爱国群", '6804740109@chatroom': "蒙市-美金互换人民币",
                  '18354518555@chatroom': "室内外油漆粉刷",
                  '6169311307@chatroom': "蒙城众筹", '22923400322@chatroom': "加拿大，", '26854417434@chatroom': "蒙城买卖书群",
                  '5903007682@chatroom': "温哥华DS 广告信息群二群", '25781308120@chatroom': "蒙村生活群",
                  '26785616535@chatroom': "蒙城多城医用外科现货！！随时取", '7339146762@chatroom': "用联科网络，享精彩生活。",
                  '6218973700@chatroom': "(租房，卖车，生意）", '5965277219@chatroom': "🇨🇳国际搬运交流群🇨🇦",
                  '4668973265@chatroom': "蒙城二手闲置物品群",
                  '5924272390@chatroom': "老陈杂练折腾群",
                  '2425343376@chatroom': "2022龙舟节侨学商界支持群", '18585070834@chatroom': "蒙城生活信息港",
                  '1598465020@chatroom': "中加物流大蒙物流hamilton 1群",
                  '386473487@chatroom': "2016康考迪亚新生2群", '1711085213@chatroom': "加园时政窗口",
                  '6202102304@chatroom': "爱蒙城🎈吃喝玩乐群",
                  '18534883883@chatroom': "蒙城多肉植物交流", '27764908392@chatroom': "创业群-求职招聘-租房买房",
                  '5914094876@chatroom': "加拿大共生国际传媒 蒙1", '7678577066@chatroom': "蒙城中高端装修咨询",
                  '6226010832@chatroom': "博艺装修水电工程5145313527",
                  '2458167059@chatroom': "蒙城用工招聘服务群",
                  '2453501819@chatroom': "南岸BROSSARD分享群1️⃣", '17793082685@chatroom': "蒙城-阿里巴巴速卖通优惠二群",
                  '2427283542@chatroom': "蒙特利尔内部招聘信息分享", '5986184764@chatroom': "蒙村能工巧匠",
                  '4550451594@chatroom': "C🇨🇦雇主工资补贴交流群", '6179335841@chatroom': "癌症不是病",
                  '27362705297@chatroom': "蒙城-互助信息交流群",
                  '5988175393@chatroom': "北极商盟办公(魁北克商业联盟)",
                  '6220125724@chatroom': "蒙城美食频道🍁 饕哥酱卤＆小炒",
                  '3478259743@chatroom': "Concordia交流群•蒙城汇",
                  '7446212365@chatroom': "蒙城留学买房货币兑换互助交流群",
                  }

    for k, v in send_daily.items():
        w.send_text(self_wx=self_wx, to_wx=k, msg='👋告别渣网，一家人👨‍👩‍👧‍👦的通讯方式📶不能都放一个篮子里🈲\n'
                                                      '🔥推荐一卡双号QC短期优惠促销❗12G/40$，🉑无限电话短信，🈶中加长途双向任打，🈚合约。\n'
                                                  '📢联系4389379780或加微信ubreakifix_helpdesk了解更多详情。\n')
        time.sleep(10)
        w.send_img(self_wx=self_wx, to_wx=k, path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/repair.jpg")

    send_weekly = {'3680428212@chatroom': "SD魁北克山东同乡会",'45060083@chatroom': "laval中国人",
            '18502209111@chatroom': "口罩面罩酒精洗手液防护品", '6118291578@chatroom': "蒙特利尔第八信息交流群", '5913268640@chatroom': "蒙特利尔湖南商会交流群",
            '5957977463@chatroom': "Montreal装修群",
            '27853107981@chatroom': "春令营2021-孔子学校", '27350306580@chatroom': "魁省新冠疫情补助申请互助1群",
            '6226230903@chatroom': "亲情中华·为你讲故事总群",'27334308107@chatroom': "★蒙村★房产家具买卖租赁群",
            '27963815958@chatroom': "1930上海-南岸店 周二休息",'6271059852@chatroom': "PEQ学习工作交流群",
            '27083416287@chatroom': "蒙城互帮互助群", '26099904802@chatroom': "MCM留学生家政服务端",
            '17992524835@chatroom': "NDG好食好货拼拼团",
            '26924704048@chatroom': "信息交流你我他", '6290090934@chatroom': "南岸幸福快乐大家亲", '130647885@chatroom': "酒之坛",
            '26256907158@chatroom': "蒙城汽车房屋家电维修维护",'26713908895@chatroom': "海台网活动抽奖群",
            '25808906663@chatroom': "联邦援助8000刀线上申请讨论群", '19729177699@chatroom': "蒙特利尔用车互助群",'26264507410@chatroom': "拒绝魁省8月底开学申请网课群",
            '3097163594@chatroom': "辽宁人朋友圈",'26557506474@chatroom': "🇨🇦蒙特利尔🍁战“疫”群",
            '468737081@chatroom': "他乡故里",'18502348539@chatroom': "魁省生活交流互助群", '25880508382@chatroom': "蒙特利尔楼花转让群",
            '26464203956@chatroom': "快乐交友群",'5966989515@chatroom': "易食堂·第一炉·香",
            '24926157529@chatroom': "租房，房屋买卖，二手转让信息交流",'468605172@chatroom': "Montreal广西交流群",
            '27835306947@chatroom': "3⃣️蒙村涮肉➕蒙古烧烤=线上外卖",
            }

    for k, v in send_weekly.items():
        w.send_text(self_wx=self_wx, to_wx=k, msg='👋告别渣网，一家人👨‍👩‍👧‍👦的通讯方式📶不能都放一个篮子里🈲\n'
                                                      '🔥推荐一卡双号QC短期优惠促销❗12G/40$，🉑无限电话短信，🈶中加长途双向任打，🈚合约。\n'
                                                  '📢联系4389379780或加微信ubreakifix_helpdesk了解更多详情。\n')
        time.sleep(10)
        w.send_img(self_wx=self_wx, to_wx=k, path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/repair.jpg")

    send_monthly = {'19035579811@chatroom': "从北京到蒙城",'17871387366@chatroom': "天宝旅游西岛群",'6116137076@chatroom': "MTL生意自售闲置物品买卖广告群",
                    '17833921211@chatroom': "蒙城一期一会美食南岸群（主群）",'26214307396@chatroom': "露营户外运动分享交流",
                    '27495417306@chatroom': "蒙城嗨团～美食，学习桌，卡拉OK",'26076816574@chatroom': "硬床垫大全 宜居生活坊家具店",
                    '18618814617@chatroom': "你好超市送货群","4654777921@chatroom":"凤凰假期机票群",'26548110241@chatroom': "專業汽修",
                    '6267002248@chatroom': "①DT德邦🎀烁烁🎀GUY地铁站",'22304250728@chatroom': "麻辣香锅订餐群2",'19814421779@chatroom': "家住蒙村 之园艺频道2号群",
                    '61906881@chatroom': "NDG parents",'27941106437@chatroom': "海台南岸团送福利群", '473437886@chatroom': "天宝旅游达人1⃣群-5146641996",
                    '24605375866@chatroom': "蒙城回国交流群（核酸检测事宜等）", '2460470982@chatroom': "蒙城华人租房群",'26346308352@chatroom': "★蒙村★南岸美味超值团购群",
                    '27269616527@chatroom': "华人爱心捐赠加拿大医院群",'2454308637@chatroom': "蒙村闲聊群",'27500418263@chatroom': "🇨🇦专业房贷",
                    '26956416202@chatroom': "义工互助购物-蒙特利尔", '25950817325@chatroom': "唐人街美食群(欢迎私厨和餐馆加入)",
                    '26278218223@chatroom': "★蒙村★换汇群",'24076772811@chatroom': "海台爱拼生鲜配送群",
                    }

    # for k, v in send_monthly.items():
    #     w.send_text(self_wx=self_wx, to_wx=k, msg='👋告别渣网，一家人👨‍👩‍👧‍👦的通讯方式📶不能都放一个篮子里🈲\n'
    #                                                   '🔥推荐一卡双号QC短期优惠促销❗12G/40$，🉑无限电话短信，🈶中加长途双向任打，🈚合约。\n'
    #                                               '📢联系4389379780或加微信ubreakifix_helpdesk了解更多详情。\n')
    #     time.sleep(10)
    #     w.send_img(self_wx=self_wx, to_wx=k, path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/repair.jpg")

    # 红包
    # 资源共享家俱家居装饰
    # w.send_text(self_wx=self_wx, to_wx="324688986@chatroom",
    #             msg='如果您家里有闲置或者有损坏不值得维修的，手机/⌚手表/iPad/电脑的小伙伴🙋🏻‍♂，🉑联系我们评估🧧折价哦')
    # w.send_img(self_wx=self_wx, to_wx="324688986@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/手机换钱.jpg")
    # 大连小李美发交流514-748-7070
    # w.send_text(self_wx=self_wx, to_wx="2430497977@chatroom",
    #             msg='如果您家里有闲置或者有损坏不值得维修的，手机/⌚手表/iPad/电脑的小伙伴🙋🏻‍♂，🉑联系我们评估🧧折价哦')
    # w.send_img(self_wx=self_wx, to_wx="2430497977@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/手机换钱.jpg")
    # 周阿姨餐点英才圣劳伦周末中午配送
    # w.send_text(self_wx=self_wx, to_wx="5917103150@chatroom",
    #             msg='如果您家里有闲置或者有损坏不值得维修的，手机/⌚手表/iPad/电脑的小伙伴🙋🏻‍♂，🉑联系我们评估🧧折价哦')
    # 房源买卖咨询，特价商品
    # w.send_text(self_wx=self_wx, to_wx="2456503621@chatroom",
    #             msg='如果您家里有闲置或者有损坏不值得维修的，手机/⌚手表/iPad/电脑的小伙伴🙋🏻‍♂，🉑联系我们评估🧧折价哦')


    print ('Done')




if __name__ == '__main__':
    main()
