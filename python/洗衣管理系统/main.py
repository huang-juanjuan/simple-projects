import datetime

class Member:
    def __init__(self, member_no, reg_date, name, age, balance, phone, address):
        self.member_no = member_no
        self.reg_date = reg_date
        self.name = name
        self.age = age
        self.balance = balance
        self.phone = phone
        self.address = address

class Clothing:
    def __init__(self, clothing_no, description, receive_date, wash_date, quantity, category, status, member_name, charge):
        self.clothing_no = clothing_no
        self.description = description
        self.receive_date = receive_date
        self.wash_date = wash_date
        self.quantity = quantity
        self.category = category
        self.status = status
        self.member_name = member_name
        self.charge = charge

    def modify_clothing_status(self, status, wash_date):
        self.status = status
        self.wash_date = wash_date

    def modify_clothing_info(self, description, receive_date, quantity, category, charge):
        self.description = description
        self.receive_date = receive_date
        self.quantity = quantity
        self.category = category
        self.charge = charge


class LaundryManagementSystem:
    def __init__(self):
        self.members = []
        self.clothes = []

    # 会员注册
    def register_member(self):
        member_no = input("请输入会员号：")
        reg_date = datetime.date.today()
        name = input("请输入会员姓名：")
        age = input("请输入年龄：")
        balance = float(input("请输入会员卡余额："))
        phone = input("请输入联系电话：")
        address = input("请输入家庭住址：")
        member = Member(member_no, reg_date, name, age, balance, phone, address)
        self.members.append(member)
        print("会员注册成功！")

    # 会员充值
    def recharge_member(self):
        member_no = input("请输入会员号：")
        for member in self.members:
            if member.member_no == member_no:
                amount = float(input("请输入充值金额："))
                member.balance += amount
                print("会员充值成功！")
                return
        print("找不到该会员！")

    # 添加衣物
    def add_clothing(self):
        clothing_no = input("请输入衣服编号：")
        description = input("请输入衣服描述：")
        receive_date = datetime.date.today()
        wash_date = None
        quantity = int(input("请输入衣服数量："))
        category = input("请输入衣服种类：")
        status = "待洗"
        member_name = input("请输入会员姓名：")
        charge = float(input("请输入收费金额："))

        # 检测会员是否存在
        member_exists = False
        for member in self.members:
            if member.name == member_name:
                member_exists = True

                # 检测会员余额是否充足
                if member.balance < charge:
                    print("会员余额不足，无法添加衣物！")
                    return
                else:
                    member.balance -= charge
                break

        if member_exists:
            clothing = Clothing(clothing_no, description, receive_date, wash_date, quantity, category, status, member_name, charge)
            self.clothes.append(clothing)
            print("衣物登记成功！")
        else:
            print("找不到该会员！")

    # 查看所有衣物
    def view_clothing_info(self):
        for clothing in self.clothes:
            print("衣服编号：", clothing.clothing_no)
            print("衣服描述：", clothing.description)
            print("收取日期：", clothing.receive_date)
            print("数量：", clothing.quantity)
            print("衣服种类：", clothing.category)
            print("状态：", clothing.status)
            print("会员姓名：", clothing.member_name)
            print("收费金额：", clothing.charge)
            print()

    # 搜索会员
    def search_member_info(self):
        search_type = input("请选择查询方式（1.按会员号 2.按会员姓名）：")
        if search_type == "1":
            member_no = input("请输入会员号：")
            for member in self.members:
                if member.member_no == member_no:
                    print("会员号：", member.member_no)
                    print("注册日期：", member.reg_date)
                    print("会员姓名：", member.name)
                    print("年龄：", member.age)
                    print("会员卡余额：", member.balance)
                    print("联系电话：", member.phone)
                    print("家庭住址：", member.address)
                    return
            print("找不到该会员！")
        elif search_type == "2":
            member_name = input("请输入会员姓名：")
            for member in self.members:
                if member.name == member_name:
                    print("会员号：", member.member_no)
                    print("注册日期：", member.reg_date)
                    print("会员姓名：", member.name)
                    print("年龄：", member.age)
                    print("会员卡余额：", member.balance)
                    print("联系电话：", member.phone)
                    print("家庭住址：", member.address)
                    return
            print("找不到该会员！")
        else:
            print("无效的查询方式！")

    # 搜索衣物
    def search_clothing_info(self):
        search_type = input("请选择查询方式（1.按待洗衣物 2.按已洗衣物 3.按存放时间）：")
        if search_type == "1":
            for clothing in self.clothes:
                if clothing.status == "待洗":
                    print("衣服编号：", clothing.clothing_no)
                    print("衣服描述：", clothing.description)
                    print("收取日期：", clothing.receive_date)
                    print("数量：", clothing.quantity)
                    print("衣服种类：", clothing.category)
                    print("状态：", clothing.status)
                    print("会员姓名：", clothing.member_name)
                    print("收费金额：", clothing.charge)
                    print()
        elif search_type == "2":
            for clothing in self.clothes:
                if clothing.status == "已洗":
                    print("衣服编号：", clothing.clothing_no)
                    print("衣服描述：", clothing.description)
                    print("收取日期：", clothing.receive_date)
                    print("数量：", clothing.quantity)
                    print("衣服种类：", clothing.category)
                    print("状态：", clothing.status)
                    print("会员姓名：", clothing.member_name)
                    print("收费金额：", clothing.charge)
                    print()
        elif search_type == "3":
            days = int(input("请输入最少存放天数："))
            for clothing in self.clothes:
                if (datetime.date.today() - clothing.wash_date).days >= days:
                    print("衣服编号：", clothing.clothing_no)
                    print("衣服描述：", clothing.description)
                    print("收取日期：", clothing.receive_date)
                    print("数量：", clothing.quantity)
                    print("衣服种类：", clothing.category)
                    print("状态：", clothing.status)
                    print("会员姓名：", clothing.member_name)
                    print("收费金额：", clothing.charge)
                    print()
        else:
            print("无效的查询方式！")

    # 修改会员信息
    def modify_member_info(self):
        member_no = input("请输入要修改的会员号：")
        for member in self.members:
            if member.member_no == member_no:

                # 删除该会员名下所有衣物
                self.clothes = [clothing for clothing in self.clothes if clothing.member_name != member.name]
                member.name = input("请输入新的会员姓名：")
                member.age = input("请输入新的年龄：")
                member.balance = float(input("请输入新的会员卡余额："))
                member.phone = input("请输入新的联系电话：")
                member.address = input("请输入新的家庭住址：")
                print("会员信息修改成功！")
                return
        print("找不到该会员！")

    # 修改衣物信息
    def modify_clothing_info(self):
        clothing_no = input("请输入要修改的衣服编号：")
        for clothing in self.clothes:
            if clothing.clothing_no == clothing_no:
                description = input("请输入新的衣服描述：")
                receive_date = datetime.date.today()
                quantity = int(input("请输入新的衣服数量："))
                category = input("请输入新的衣服种类：")
                charge = float(input("请输入新的收费金额："))
                clothing.modify_clothing_info(description, receive_date, quantity, category, charge)
                print("衣物信息修改成功！")
                return
        print("找不到该衣物！")

    # 清洗衣物
    def wash_clothing(self):
        clothing_no = input("请输入要修改的衣服编号：")
        for clothing in self.clothes:

            # 检测衣物是否存在
            if clothing.clothing_no == clothing_no:
                status = input("衣物是否已洗（y/n）：")
                if status == "y":
                    wash_date = datetime.date.today()
                    status = "已洗"
                else:
                    wash_date = None
                    status = "待洗"
                clothing.modify_clothing_status(status, wash_date)
                print("衣物清洗状态修改成功！")
                return
        print("找不到该衣物！")

    # 删除会员
    def delete_member(self):
        member_no = input("请输入要删除的会员号：")
        for member in self.members:
            if member.member_no == member_no:
                self.members.remove(member)

                # 删除该会员名下所有衣物
                self.clothes = [clothing for clothing in self.clothes if clothing.member_name != member.name]
                print("会员删除成功！")
                return
            print("找不到该会员！")

    # 删除衣物
    def delete_clothing(self):
        clothing_no = input("请输入要删除的衣服编号：")
        for clothing in self.clothes:
            if clothing.clothing_no == clothing_no:
                self.clothes.remove(clothing)
                print("衣物删除成功！")
                return
        print("找不到该衣物！")

    # 提醒取衣
    def remind_clothing_pickup(self):
        for clothing in self.clothes:

            # 存放时间按照清洗时间开始计算
            if clothing.wash_date is not None and (datetime.date.today() - clothing.wash_date).days >= 7:
                print("衣服编号：", clothing.clothing_no)
                print("衣服描述：", clothing.description)
                print("收取日期：", clothing.receive_date)
                print("数量：", clothing.quantity)
                print("衣服种类：", clothing.category)
                print("状态：", clothing.status)
                print("会员姓名：", clothing.member_name)
                print("收费金额：", clothing.charge)
                print("请尽快取走衣物！")
                print()

    def menu(self):
        while True:
            print("欢迎使用干洗店洗衣管理系统！")
            print("1. 会员管理")
            print("2. 衣物管理")
            print("3. 洗衣信息浏览")
            print("4. 会员基本信息查询")
            print("5. 衣物基本信息查询")
            print("6. 修改会员信息")
            print("7. 修改衣物信息")
            print("8. 删除会员")
            print("9. 删除衣物")
            print("10. 清洗衣物")
            print("11. 提醒取衣物")
            print("12. 会员充值")
            print("0. 退出系统")
            choice = input("请输入操作编号：")
            if choice == "1":
                self.register_member()
            elif choice == "2":
                self.add_clothing()
            elif choice == "3":
                self.view_clothing_info()
            elif choice == "4":
                self.search_member_info()
            elif choice == "5":
                self.search_clothing_info()
            elif choice == "6":
                self.modify_member_info()
            elif choice == "7":
                self.modify_clothing_info()
            elif choice == "8":
                self.delete_member()
            elif choice == "9":
                self.delete_clothing()
            elif choice == "10":
                self.wash_clothing()
            elif choice == "11":
                self.remind_clothing_pickup()
            elif choice == "12":
                self.recharge_member()
            elif choice == "0":

                # 保存会员信息和衣物信息到文件
                with open("members.txt", "w") as f:
                    for member in self.members:
                        f.write(
                            f"{member.member_no},{member.reg_date},{member.name},{member.age},{member.balance},{member.phone},{member.address}\n")
                with open("clothes.txt", "w") as f:
                    for clothing in self.clothes:
                        f.write(
                            f"{clothing.clothing_no},{clothing.description},{clothing.receive_date},{clothing.wash_date},{clothing.quantity},{clothing.category},{clothing.status},{clothing.member_name},{clothing.charge}\n")
                        print("感谢使用干洗店洗衣管理系统！")
                break
            else:
                print("无效的操作编号！")

    # 启动时加载数据
    def load_data(self):
        try:
            with open("members.txt", "r") as f:
                for line in f:
                    data = line.strip().split(",")
                    member_no = data[0]
                    reg_date = datetime.datetime.strptime(data[1], "%Y-%m-%d").date()
                    name = data[2]
                    age = data[3]
                    balance = float(data[4])
                    phone = data[5]
                    address = data[6]
                    member = Member(member_no, reg_date, name, age, balance, phone, address)
                    self.members.append(member)
            with open("clothes.txt", "r") as f:
                for line in f:
                    data = line.strip().split(",")
                    clothing_no = data[0]
                    description = data[1]
                    receive_date = datetime.datetime.strptime(data[2], "%Y-%m-%d").date()
                    wash_date = None if data[3] == "" else datetime.datetime.strptime(data[3], "%Y-%m-%d").date()
                    quantity = int(data[4])
                    category = data[5]
                    status = data[6]
                    member_name = data[7]
                    charge = float(data[8])
                    clothing = Clothing(clothing_no, description, receive_date, wash_date, quantity, category, status, member_name,
                                        charge)
                    self.clothes.append(clothing)
                    print("数据加载成功！")
        except FileNotFoundError:
            print("找不到数据文件，将创建新的数据文件。")

# 测试代码
system = LaundryManagementSystem()
system.load_data()
system.menu()
