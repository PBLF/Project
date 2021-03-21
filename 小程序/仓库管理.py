"""
1.商品清单保存在.txt文件中
2.基本实现增删改查功能
3.任意位置输入b返回上级菜单，输入q退出
"""

import os
from subprocess import run


def cecho(num, content):
    print('\033[%sm%s\033[0m' % (num, content))


def choice_action(action):
    while action != "b":
        if action == "q":
            exit(0)
        else:
            break
    return action


def view_shop(file_name):
    commodity = []
    if not os.path.isfile(file_name):
        os.mknod(file_name)
    else:
        with open(file_name, 'r') as file:
            for each in file:
                commodity.append(each.splitlines())
        if len(commodity) == 0:
            cecho(35, "请添加商品")
        else:
            print('%-10s%-8s%-12s' % ('序号', '名字', '价格'))
            for index, value in enumerate(commodity):
                alist = value[0].split(":")
                print('%-12s%-10s%-8s' % (index + 1, alist[0], alist[1]))
        return commodity


def add_shop(file_name):
    while True:
        add_dict = {}
        shop_name = input(">>>输入商品名：").strip()
        if choice_action(shop_name) == "b":
            break
        shop_price = input(">>>输入商品价格：").strip()
        if choice_action(shop_price) == "b":
            break
        elif shop_price.isdigit():
            add_dict[shop_name] = shop_price
            for i in add_dict:
                with open(file_name, 'a+')as file:
                    file.write('%s:%s\n' % (i, add_dict[i]))
                    print("\033[92m%s存入成功\033[0m" % shop_name)
                view_shop(file_name)
        else:
            cecho(31, "Invalid Option")


def del_shop(file_name):
    menu_info = "商品清单"
    print(menu_info.center(26, '-'))
    commodity = view_shop(file_name)
    while True:
        del_num = input(">>>商品序号:").strip()
        if choice_action(del_num) == "b":
            break
        elif del_num.isdigit():
            del_num = int(del_num)
            rc = run("sed -i '/%s/d' %s" % (commodity[del_num - 1][0], file_name), shell=True)
            if not rc.returncode:
                cecho(92, "删除成功")
            else:
                cecho(31, "删除失败")
            view_shop(file_name)
        else:
            cecho(31, "Invalid Option")


def update_price(file_name):
    menu_info = "商品清单"
    print(menu_info.center(26, '-'))
    commodity = view_shop(file_name)
    while True:
        update_num = input(">>>商品序号：").strip()
        if choice_action(update_num) == "b":
            break
        elif update_num.isdigit():
            update_num = int(update_num)
        else:
            cecho(31, "Invalid Option")

        new_price = input(">>>新的价格：").strip()
        if choice_action(new_price) == "b":
            break
        elif new_price.isdigit():
            new_price = int(new_price)
            alist = commodity[update_num - 1][0].split(":")
            alist[1] = new_price
            rc = run("sed -i '/%s/c %s:%s' %s" % (alist[0], alist[0], alist[1], file_name), shell=True)
            if not rc.returncode:
                cecho(92, "修改成功")
            else:
                cecho(31, "修改失败")
            view_shop(file_name)
        else:
            cecho(31, "Invalid Option")


def show_menu():
    cmds = {'0': view_shop, '1': add_shop, '2': del_shop, '3': update_price}
    prompt = '''
    (0)查看商品信息
    (1)增加商品
    (2)删除商品
    (3)修改商品价格
    (b)返回上级菜单
    (q)退出
    输入选项
    '''
    fname = '？？？.txt'
    while True:
        choice = input(prompt).strip()
        if choice not in '0123bq':
            cecho(31, "Invalid Option")
        elif choice_action(choice) == 'b':
            cecho(31, "已经是第一级菜单")
        else:
            cmds[choice](fname)


if __name__ == "__main__":
    try:
        show_menu()
    except KeyboardInterrupt as e:
        print()
        cecho(31, "非正常退出，请输入字母q")
