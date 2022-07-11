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
    print(lists)

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


    # 测试功能   ADOGO商业广告发展群  TD银行投资讲座五群
    w.send_img(self_wx=self_wx, to_wx="228563099@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi1.jpg")
    w.send_text(self_wx=self_wx, to_wx="228563099@chatroom", msg='‍蒙城小米精品分享及售后群品类涵盖生活🥂、运动、美容🥰、创意、家居🛋等多方面小米最黑科技产品。给您一个不一样的选择空间。')
    # time.sleep(1)
    # w.send_img(self_wx=self_wx, to_wx="2505455504@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/repair.jpg")
    # time.sleep(5)
    # w.logout(self_wx=self_wx)

    # #山东人商务及生活交流群
    # w.send_img(self_wx=self_wx, to_wx="104060697@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #文苑清风诵读好声音
    # w.send_img(self_wx=self_wx, to_wx="216177289@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #精彩信息共享交流群
    # w.send_img(self_wx=self_wx, to_wx="2132313807@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    #
    # #ADOGO商业广告发展群
    # w.send_img(self_wx=self_wx, to_wx="228563099@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #北极商盟之广告与生意经
    # w.send_img(self_wx=self_wx, to_wx="2238310305@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #装修咨询，房地产信息
    # w.send_img(self_wx=self_wx, to_wx="2420078280@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #TD银行投资讲座五群
    # w.send_img(self_wx=self_wx, to_wx="2505455504@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    #
    # #欢乐网络教室
    # w.send_img(self_wx=self_wx, to_wx="2494010639@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #便利店主互助群
    # w.send_img(self_wx=self_wx, to_wx="2506294180@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #华总会《蒙华同春》春晚三群
    # w.send_img(self_wx=self_wx, to_wx="26001620259@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #市场广告，资源共享群
    # w.send_img(self_wx=self_wx, to_wx="27595706872@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    #
    # #蒙城物品2⃣️群加你朋友进来
    # w.send_img(self_wx=self_wx, to_wx="2696310183@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #南岸瑞和商业广告群
    # w.send_img(self_wx=self_wx, to_wx="316690492@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #Concordia交流群•蒙城汇
    # w.send_img(self_wx=self_wx, to_wx="3478259743@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #蒙城休闲文化活动召集
    # w.send_img(self_wx=self_wx, to_wx="346486084@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    #
    # #蒙特利尔·房屋租赁
    # w.send_img(self_wx=self_wx, to_wx="336646094@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #中外企业交流群（1）
    # w.send_img(self_wx=self_wx, to_wx="4553368439@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #他乡故里
    # w.send_img(self_wx=self_wx, to_wx="468737081@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    #
    # #北美文化传媒
    # w.send_img(self_wx=self_wx, to_wx="5914992836@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #枫花雪乐
    # w.send_img(self_wx=self_wx, to_wx="6093070779@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #快快乐乐吃吃吃
    # w.send_img(self_wx=self_wx, to_wx="6174030823@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    #
    # #蒙特利尔第八信息交流群
    # w.send_img(self_wx=self_wx, to_wx="6118291578@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #粤菜吃货群欢迎大家围观哦
    # w.send_img(self_wx=self_wx, to_wx="96571598@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #蒙城顺风车，边境，多伦多搬家接送
    # w.send_img(self_wx=self_wx, to_wx="7625950767@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #蒙城租房找房二手交易生活信息群
    # w.send_img(self_wx=self_wx, to_wx="5281311408@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    #
    # #口罩面罩酒精洗手液防护品
    # w.send_img(self_wx=self_wx, to_wx="18502209111@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #从北京到蒙城
    # w.send_img(self_wx=self_wx, to_wx="19035579811@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #蒙城医疗服务信息群
    # w.send_img(self_wx=self_wx, to_wx="198500794@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #春节香港盆菜团购群
    # w.send_img(self_wx=self_wx, to_wx="25757847006@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    #
    # #蒙城汽车房屋家电维修维护
    # w.send_img(self_wx=self_wx, to_wx="26256907158@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #蒙特利尔代理军团
    # w.send_img(self_wx=self_wx, to_wx="26300505418@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #專業汽修
    # w.send_img(self_wx=self_wx, to_wx="26548110241@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #海台网活动抽奖群
    # w.send_img(self_wx=self_wx, to_wx="26713908895@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    #
    # #加拿大徽商总会
    # w.send_img(self_wx=self_wx, to_wx="27167818625@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #北美生活艺术政聊群
    # w.send_img(self_wx=self_wx, to_wx="27352416840@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #资源共享家俱家居装饰
    # w.send_img(self_wx=self_wx, to_wx="324688986@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #蒙城二手交易群
    # w.send_img(self_wx=self_wx, to_wx="6073020567@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    #
    # #蒙城活动分享群
    # w.send_img(self_wx=self_wx, to_wx="6067993520@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #南岸BROSSARD分享群
    # w.send_img(self_wx=self_wx, to_wx="6174161612@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #蒙城人脉圈
    # w.send_img(self_wx=self_wx, to_wx="6223237732@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #蒙市-美金互换人民币
    # w.send_img(self_wx=self_wx, to_wx="6804740109@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    #
    # #蒙特利尔青年爱国群
    # w.send_img(self_wx=self_wx, to_wx="7632165442@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #蒙市-美金互换人民币
    # w.send_img(self_wx=self_wx, to_wx="6804740109@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    #
    # #室内外油漆粉刷
    # w.send_img(self_wx=self_wx, to_wx="18354518555@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #蒙城众筹
    # w.send_img(self_wx=self_wx, to_wx="6169311307@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    #
    # #加拿大，
    # w.send_img(self_wx=self_wx, to_wx="22923400322@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #蒙城买卖书群
    # w.send_img(self_wx=self_wx, to_wx="26854417434@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #温哥华DS 广告信息群二群
    # w.send_img(self_wx=self_wx, to_wx="5903007682@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    #

    # #蒙村生活群
    # w.send_img(self_wx=self_wx, to_wx="25781308120@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #蒙城置业群
    # w.send_img(self_wx=self_wx, to_wx="6181105893@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #NDG parents
    # w.send_img(self_wx=self_wx, to_wx="61906881@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    #
    # #蒙城多城医用外科现货！！随时取
    # w.send_img(self_wx=self_wx, to_wx="26785616535@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #用联科网络，享精彩生活。
    # w.send_img(self_wx=self_wx, to_wx="7339146762@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #(租房，卖车，生意）
    # w.send_img(self_wx=self_wx, to_wx="6218973700@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    #
    # #🇨🇳国际搬运交流群🇨🇦
    # w.send_img(self_wx=self_wx, to_wx="5965277219@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #🇨🇦蒙特利尔🍁战“疫”群
    # w.send_img(self_wx=self_wx, to_wx="26557506474@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #PEQ学习工作交流群
    # w.send_img(self_wx=self_wx, to_wx="6271059852@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    #
    # #酒之坛
    # w.send_img(self_wx=self_wx, to_wx="130647885@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #南岸幸福快乐大家亲
    # w.send_img(self_wx=self_wx, to_wx="6290090934@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #蒙城二手闲置物品群
    # w.send_img(self_wx=self_wx, to_wx="4668973265@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    #
    # #老陈杂练折腾群
    # w.send_img(self_wx=self_wx, to_wx="5924272390@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #2022龙舟节侨学商界支持群
    # w.send_img(self_wx=self_wx, to_wx="2425343376@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #蒙城生活信息港
    # w.send_img(self_wx=self_wx, to_wx="18585070834@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #Montreal装修群
    # w.send_img(self_wx=self_wx, to_wx="5957977463@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")

    # # # 一周发一次
    # # 中加语言文化学院1群
    # w.send_img(self_wx=self_wx, to_wx="302138888@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #魁北克格瑞斯多元文化三群
    # w.send_img(self_wx=self_wx, to_wx="5944110996@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #SD魁北克山东同乡会
    # w.send_img(self_wx=self_wx, to_wx="3680428212@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")
    # #laval中国人
    # w.send_img(self_wx=self_wx, to_wx="45060083@chatroom", path=r"C:/Users/huaow/Desktop/ZHAO YUE/poster/xiaomi2.jpg")

if __name__ == '__main__':
    main()

