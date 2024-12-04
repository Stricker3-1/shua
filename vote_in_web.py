import re
import requests
import random

def vote(url, use_id, n):
    """为指定的 useID 进行投票"""
    ip = [i for i in range(1, 256)]
    for i in range(n):
        # 随机生成 Fake_IP 地址
        Fake_Ip = '192.168.{}.{}'.format(random.choice(ip), random.choice(ip))
        print(f'Fake_IP: {Fake_Ip}')
        
        # POST 请求数据和请求头
        datas = {'useID': use_id}
        headers = {
            'Accept': 'text/plain, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Content-Length': str(len(str(datas))),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': '00d6d6.lanh.love',
            'Origin': 'https://00d6d6.lanh.love',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'https://00d6d6.lanh.love/107/#/vote?act=8828',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'X-Real-Ip': Fake_Ip,
            'X-Forwarded-For': Fake_Ip
        }
        try:
            # 发起 POST 请求
            response = requests.post(url, headers=headers, data=datas)
            # 提取票数信息
            votes_num = re.search(r'\d+', response.text)
            if votes_num:
                print(f'成功投票给 useID={use_id}，当前票数：{votes_num.group(0)}')
            else:
                print('投票响应解析失败')
        except Exception as e:
            print(f'投票失败，错误信息：{e}')

def main():
    """主函数"""
    try:
        # 设置目标 URL 和投票 useID
        vote_url = 'https://00d6d6.lanh.love/107/#/vote?act=8828'
        target_use_id = 267877
        
        # 开始投票
        print(f'开始为 useID={target_use_id} 投票...')
        for _ in range(300):  # 投票 300 次，每次 1 票
            vote(vote_url, target_use_id, 1)
    except Exception as e:
        print(f'程序运行出错，错误信息：{e}')

if __name__ == '__main__':
    main()
