import tkinter as tk
from tkinter import messagebox
from PIL import Image
from io import BytesIO
from test import api_handler


def generate_image():
    global generate_button
    prompt_text = "A pet, " + prompt_entry.get()  # 在用户输入的提示词前添加 "A pet, "
    if not prompt_text:
        messagebox.showerror("Error", "请输入英文提示词")
        return

    # 禁用生成图像按钮
    generate_button.config(state="disabled")

    # 创建加载提示窗口
    loading_window = tk.Toplevel(root)
    loading_window.title("Loading...")
    loading_label = tk.Label(loading_window, text="正在生成图像中，生成完毕后将会在新的窗口中打开，请耐心等待")
    loading_label.pack()
    loading_window.update()  # 更新加载窗口

    try:
        # 生成图像（调用模拟方法，显示的是本地的图片）
        image_data = api_handler.generate_image_mock(prompt_text)
        # 生成图像
        # image_data = api_handler.generate_image(prompt_text)
        # # 保存图像
        # api_handler.save_image(image_data, 'D:/学习/敏捷开发/生成的图片')

        # 显示图像
        image = Image.open(BytesIO(image_data))
        image.show()

    except Exception as err:
        messagebox.showerror("Error", f"An error occurred: {err}")
    finally:

        # 关闭加载提示窗口
        loading_window.destroy()
        # 启用生成图像按钮
        generate_button.config(state="normal")


def exit_application():
    root.destroy()


# 创建主窗口
root = tk.Tk()
root.title("智能图像生成器")

# 创建提示信息标签
info_label = tk.Label(root, text="请注意，此图像生成器默认生成宠物类图片，请注意提示词的编写。")
info_label.pack()

# 创建输入框和按钮
prompt_label = tk.Label(root, text="请输入提示词:")
prompt_label.pack()
prompt_entry = tk.Entry(root, width=50)
prompt_entry.pack()

generate_button = tk.Button(root, text="生成图片", command=generate_image)
generate_button.pack()

exit_button = tk.Button(root, text="退出", command=exit_application)
exit_button.pack()

# 运行主循环
root.mainloop()
