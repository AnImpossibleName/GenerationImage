import json
import requests
# 测试完成，可用，image_url中是可直接打开的网址
# 定义请求的URL和文件路径
url = "https://www.imgtp.com/api/upload"
file_path = "C://Users//袁//Desktop//图//004.jpg"  # 替换为你的文件实际路径

# 打开文件并准备请求体
with open(file_path, 'rb') as f:
    files = {
        'image': ('test.png', f, 'image/png')
    }

    # 发送POST请求
    response = requests.post(url, files=files)

# 检查请求是否成功
if response.status_code == 200:
    print("图片上传成功！")

    # 解析返回的JSON数据
    response_data = json.loads(response.text)

    # 提取图片的URL
    image_url = response_data.get("data", {}).get("url")

    # 检查是否成功获取到URL
    if image_url:
        print("图片URL:", image_url)

        # 存储图片URL到变量
        image_variable = image_url
        print("图片URL已存储在变量image_variable中。")

        # 如果需要，可以在这里使用image_variable变量
        # 例如，将其输出到控制台或进行其他操作
    else:
        print("未能从响应中获取图片URL。")
else:
    print(f"图片上传失败，状态码：{response.status_code}")

# 打印返回的内容，方便调试
print(response.text)
