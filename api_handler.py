import requests
import os
import time


def generate_image(prompt_text):
    try:
        req = requests.post('https://clipdrop-api.co/text-to-image/v1',
                            files={
                                'prompt': (None, prompt_text, 'text/plain')
                            },
                            headers={
                                'x-api-key': '071860c79d25f0ad2a8112caeecf607cd313526cf0901b7ed44d535c2610c989f556244fc378c7c48722ae439b9b9b38'}
                            )
        req.raise_for_status()
        image_data = req.content
        return image_data
    except Exception as err:
        raise RuntimeError(f"发生错误: {err}")


def save_image(image_data, save_path):
    try:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        timestamp = int(time.time())  # 使用当前时间戳作为唯一标识符
        with open(os.path.join(save_path, f'generated_image_{timestamp}.png'), 'wb') as generate:
            generate.write(image_data)
    except Exception as err:
        raise RuntimeError(f"存储图片时发生错误: {err}")


# 模拟调用API
def generate_image_mock(prompt_text):
    try:
        # 读取本地图片
        with open('D:/学习/敏捷开发/生成的图片/generated_image_1712133767.png', 'rb') as generate:
            image_data = generate.read()
        return image_data
    except Exception as err:
        raise RuntimeError(f"读取本地照片时发生错误: {err}")
