

#!/usr/bin/python3
#  -*- coding: utf-8 -*-
'''图书管理系统
1. 创建一个列表存储书籍信息，包括书名，作者名，价格
2. 创建一个列表存储用户信息，包括用户名，密码
3. 制作一个注册登录系统，登录后可以使用添加书籍，删除书籍，
修改书籍信息，查询单本书籍信息，查询所有书籍信息等功能
4. 制作其它合理功能。
'''

'''图书管理系统操作说明
一、普通用户
    1.先注册
    2.登录到系统
    3.进行功能操作    （增、删、改、查书籍）
    4.退出系统
二、管理者
    1.使用管理者账户登陆（xls：123456）
    2.管理普通用户    （删、改、查用户）
    3.退出系统
'''

books = [{'name': '西游记', 'author': '吴承恩', 'price': '19.9'},
         {'name': '三国演义', 'author': '罗贯中', 'price': '99.9'},
         {'name': '完美世界', 'author': '辰东', 'price': '199.9'},
         {'name': '斗破苍穹', 'author': '土豆', 'price': '99'}
         ]
users = [{'name': 'Tom', 'passwd': '12345'}]


# 主菜单
def menu():
    print('*' * 40)
    print('*' * 10, '欢迎来到图书管理系统')
    print('*' * 40)
    print('请选择：')
    print("1: 注册新用户：")
    print("2. 已有账户，登陆：")
    print("3. 退出本系统")


# 用户小屋（功能页面）
def user_menu(self):
    print('*' * 40)
    print('欢迎%s!   来到图书小屋' % self)
    print('请选择您所需的功能：')
    print('1. 添加书籍')
    print('2. 删除书籍')
    print('3. 修改书籍信息')
    print('4. 查询单本书籍信息')
    print('5. 查询所有书籍信息')
    print('6. 退出您的图书小屋')


# 管理者页面
def manger():
    print('*' * 40)
    print('欢迎本系统管理者！！！')
    print('*' * 40)
    print('请选择您所需的功能：')
    print('1. 删除一个用户')
    print('2. 修改用户密码')
    print('3. 查看一个用户信息')
    print('4. 查看全部用户信息')
    print('5. 退出管理者页面')


# 删除用户
def del_user():
    user_name = input('请输入要删除的用户名：')
    count = 0
    index = 0
    for i in users:
        if user_name == i['name']:
            count = 1
            del users[index]
            print('删除成功！！！')
        index += 1
    if count == 0:
        print('查无此人！！！')


# 修改用户
def edit_user():
    user_name = input('请输入要修改密码的用户名：')
    count = 0
    index = 0
    for i in users:
        if user_name == i['name']:
            count = 1
            del users[index]
            new_user_name = user_name
            new_user_passwd = input('请输入修改后的密码：')
            new_user = {'name': new_user_name, 'passwd': new_user_passwd}
            users.append(new_user)
            print('修改成功！！！')
        index += 1
    if count == 0:
        print('查无此人！！！')


# 查看一个用户
def look_user():
    user_name = input('请输入要查看的用户名：')
    count = 0
    print('用户名\t密码\t')
    for i in users:
        if user_name == i['name']:
            count = 1
            print('%s\t\t%s\t' % (i['name'], i['passwd']))
    if count == 0:
        print('查无此人！！！')


# 查看全部用户
def look_users():
    print('用户名\t密码\t')
    for i in users:
        print('%s\t\t%s\t' % (i['name'], i['passwd']))


# 注册页面
def sign_up():
    user_name = input("请输入您的用户名：")
    user_passwd = input("请输入您的密码：")
    user = {'name': user_name, 'passwd': user_passwd}
    users.append(user)
    print("注册成功！！！")


# 登陆页面
def login():
    user_name = input("请输入您的用户名：")
    user_passwd = input("请输入您的密码：")
    count = 0
    for i in users:
        if user_name == i['name']:
            count = 1
            if user_passwd == i['passwd']:
                print("登陆成功！！！")
                return user_name
            else:
                print("密码错误！！！")
                print("请重试。")
                login()
    if count == 0:
        print("用户名不存在！！！")
        print("请重试。")
        login()


# 添加书籍
def add_book():
    book_name = input('请输入要添加书籍的名字：')
    book_author = input('请输入要添加书籍的作者：')
    book_price = input('请输入要添加书籍的价格：')
    book = {'name': book_name, 'author': book_author, 'price': book_price}
    books.append(book)
    print('添加成功！！！')


# 删除书籍
def del_book():
    book_name = input('请输入要删除书籍的名字：')
    count = 0
    index = 0
    for i in books:
        if book_name == i['name']:
            count = 1
            del books[index]
            print('删除成功！！！')
        index += 1
    if count == 0:
        print('查无此书！！！')


# 修改书籍
def edit_book():
    book_name = input('请输入要修改书籍的名字：')
    count = 0
    index = 0
    for i in books:
        if book_name == i['name']:
            count = 1
            del books[index]
            new_book_name = input('请输入修改后书籍的名字：')
            new_book_author = input('请输入修改后书籍的作者：')
            new_book_price = input('请输入修改后书籍的价格：')
            new_book = {'name': new_book_name, 'author': new_book_author, 'price': new_book_price}
            books.append(new_book)
            print('修改成功！！！')
        index += 1
    if count == 0:
        print('查无此书！！！')


# 查看一本书籍
def look_book():
    book_name = input('请输入要查看书籍的名字：')
    count = 0
    print('书名\t\t作者\t价格\t')
    for i in books:
        if book_name == i['name']:
            count = 1
            print('%s\t%s\t%s\t' % (i['name'], i['author'], i['price']))
    if count == 0:
        print('查无此书！！！')


# 查看全部书籍
def look_books():
    print('书名\t\t作者\t价格\t')
    for i in books:
        print('[%s]\t%s\t%s\t' % (i['name'], i['author'], i['price']))


# 用户与管理者
def while_user(name):
    while name:  # 根据是否登陆成功，进入用户菜单

        if name == 'xls':  # 判断是否为管理者
            manger()  # 管理者页面
            manger_n = input()
            if manger_n == '1':
                del_user()  # 删除一个用户
            elif manger_n == '2':
                edit_user()  # 修改用户密码
            elif manger_n == '3':
                look_user()  # 查看一个用户信息
            elif manger_n == '4':
                look_users()  # 查看全部用户信息
            elif manger_n == '5':
                break  # 退出管理者页面
            else:
                print("非法输入！！！")
                print("请再次选择：")

        else:
            user_menu(name)  # 普通用户页面
            user_n = input()
            if user_n == '1':
                add_book()  # 添加书籍
            elif user_n == '2':
                del_book()  # 删除书籍
            elif user_n == '3':
                edit_book()  # 修改书籍信息
            elif user_n == '4':
                look_book()  # 查询单本书籍信息
            elif user_n == '5':
                look_books()  # 查询所有书籍信息
            elif user_n == '6':
                break  # 退出普通用户页面
            else:
                print("非法输入！！！")
                print("请再次选择：")


# 主函数
def main():
    # 循环菜单主页面
    while True:
        menu()  # 主菜单页面
        menu_n = input()
        if menu_n == '1':
            sign_up()
        elif menu_n == '2':
            # 循环用户菜单页面
            name = login()  # 用户登陆后返回值name

            while_user(name)  # 用户与管理者

        elif menu_n == '3':
            break
        else:
            print("非法输入！！！")
            print("请再次选择：")


# 调用主函数
main()

