# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pydub import AudioSegment
import numpy as np
import os
import shutil

def print_audio_volume(audio_path):
    song = AudioSegment.from_file(audio_path, format='mp3')
    wav = np.array(song.get_array_of_samples())
    sr = song.frame_rate
    mean_volume = np.mean(np.abs(wav))  # 计算平均音量
    print(f"平均音量: {mean_volume}")
    return mean_volume

def print_audio_volume2(audio_path):
    # 加载音频文件
    audio = AudioSegment.from_mp3(audio_path)
    # 计算平均音量
    average_volume = audio.dBFS
    print(f"Original volume of {audio_path}: {average_volume} dBFS")

def print_dir(directory_path):
    # 遍历目录
    for filename in os.listdir(directory_path):
        # 构建完整的文件路径
        ext = os.path.splitext(filename)[1].lower()
        if ext == '.mp3':
            print(filename, end=": ")
            print_audio_volume(os.path.join(directory_path, filename))

def rename_file(directory_path):
    # 遍历目录
    for filename in os.listdir(directory_path):
        # 检查文件名中是否包含下划线
        if '_' in filename:
            # 分离文件名和扩展名
            name, extension = os.path.splitext(filename)
            # 根据下划线拆分文件名
            parts = name.split('_', 1)
            old_file_path = os.path.join(directory_path, filename)

            if len(parts) == 2:
                number_part, rest_part = parts
                # 检查数字部分是否全部由数字组成
                if number_part.isdigit():
                    # 补齐数字为3位
                    number_padded = number_part.zfill(3)
                    # 构建新的文件名
                    new_filename = f"{number_padded}_{rest_part}{extension}"
                    # 构建完整的文件路径
                    new_file_path = os.path.join(directory_path+r"\new", new_filename)
                    # 拷贝文件并重命名
                else:
                    print(f"error: {filename}")
            else:
                new_file_path = os.path.join(directory_path+r"\new", filename)
            print(f"Copied and renamed '{old_file_path}' to '{new_file_path}'")
            shutil.copy2(old_file_path, new_file_path)

def mod_audio_volume(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".mp3"):
            # 构建完整的文件路径
            in_file_path = os.path.join(directory_path, filename)
            out_file_path = os.path.join(directory_path + r"\mod", filename)
            # 加载音频文件
            mod_file_audio(in_file_path, out_file_path, -8.9)


def mod_file_audio(in_file_path, our_file_path, target_volume):
    audio = AudioSegment.from_mp3(in_file_path)
    # 计算平均音量
    average_volume = audio.dBFS
    print(f"Original volume of {in_file_path}: {average_volume} dBFS")

    # 计算需要调整的音量差值
    change_in_volume = target_volume - average_volume
    # 调整音量
    audio = audio + change_in_volume

    # 导出调整后的音频文件
    audio.export(our_file_path, format="mp3")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # 指定目录路径
    directory_path = r'D:\temp\05 弘扬世界和平\new'
    #rename_file(directory_path)
    #print_audio_volume(r"D:\temp\05 弘扬世界和平\new\024_《弘扬世界和平》2.8.mp3")
    #print_audio_volume2(r"D:\temp\05 弘扬世界和平\new\015_《弘扬世界和平》1.12.mp3")
    #mod_file_audio(r"D:\temp\05 弘扬世界和平\new\024_《弘扬世界和平》2.8.mp3", r"D:\temp\05 弘扬世界和平\new\mod\024_《弘扬世界和平》2.8.mp3", -8.90898)
    #print_audio_volume(r"D:\temp\05 弘扬世界和平\new\mod\024_《弘扬世界和平》2.8.mp3")

    mod_audio_volume(directory_path)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
