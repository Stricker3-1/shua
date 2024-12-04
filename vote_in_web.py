import requests
import time

def vote_with_cookies(vote_url, use_id, cookies):
    """
    使用登录后的 Cookies 为指定 useID 投票
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
        'Referer': 'https://00d6d6.lanh.love/107/#/vote?act=8828',
    }
    data = {'useID': use_id}  # 提交投票的目标 ID
    try:
        response = requests.post(vote_url, headers=headers, cookies=cookies, data=data)
        if response.status_code == 200:
            print(f"投票成功！响应内容: {response.text}")
        else:
            print(f"投票失败！状态码: {response.status_code}, 响应内容: {response.text}")
    except Exception as e:
        print(f"投票过程中发生错误: {e}")

def main():
    """
    主函数：循环投票
    """
    # 投票 URL 和目标 useID
    vote_url = 'https://00d6d6.lanh.love/107/#/vote?act=8828'
    use_id = 267877

    # 登录后从浏览器开发者工具中获取的 Cookies
    cookies = {
        'sessionid': 'your_session_id',  # 替换为登录后真实的 session ID
        # 根据实际需要添加其他 Cookies，如 csrftoken、auth_token 等
    }

    # 循环投票
    for i in range(10):  # 这里设置为投票 10 次，可根据需要调整
        print(f"正在进行第 {i+1} 次投票...")
        vote_with_cookies(vote_url, use_id, cookies)
        time.sleep(2)  # 增加间隔时间，模拟真实用户行为

if __name__ == '__main__':
    main()
