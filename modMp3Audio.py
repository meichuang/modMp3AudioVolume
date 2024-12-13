# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

from pydub import AudioSegment
import numpy as np
import os
import shutil
def main():
    # 检查命令行参数
    if len(sys.argv) > 1:
        #查询单个文件的音量
        if sys.argv[1] == '-q' and len(sys.argv) == 3:
            # 执行 查询文件音量 操作
            print_audio_volume2(sys.argv[2])

        #修改单个文件的音量
        elif sys.argv[1] == '-c' and len(sys.argv) == 4:
            # 执行 b 操作
            try:
                target_volume = float(sys.argv[3])
            except ValueError:
                print("转换失败，输入的音量不是一个有效的浮点数")
            out_file_path = sys.argv[2].replace(".mp3", "_adjusted.mp3")
            mod_file_audio(sys.argv[2], out_file_path, target_volume)
            print("转换结果:" + out_file_path)
        #查询目录下所有mp3文件的音量
        elif sys.argv[1] == '-qa':
            # 执行 c 操作
            print_dir(sys.argv[2])
        #修改目录下所有mp3文件的音量
        elif sys.argv[1] == '-ca' and len(sys.argv) == 5:
            # 执行 b 操作
            try:
                target_volume = float(sys.argv[4])
            except ValueError:
                print("转换失败，输入的音量不是一个有效的浮点数")

            if not os.path.exists(sys.argv[3]):
                os.makedirs(sys.argv[3])

            mod_audio_volume(sys.argv[2], sys.argv[3], target_volume)
        else:
            printUsage()
    else:
        printUsage()

def printUsage():
    print("错误：参数不正确。")
    print("用法：")
    print("  python modMp3Audio.py -q 文件名  # 执行 查询单个文件的音量 操作")
    print("  python modMp3Audio.py -qa 目录名  # 执行 查询目录下所有文件的音量 操作")
    print("  python modMp3Audio.py -c 文件名 音量  # 执行 修改单个文件的音量 操作")
    print("  python modMp3Audio.py -ca 源目录 目的目录 音量  # 执行 修改目录下所有文件音量 操作")

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
    print(f"Volume of {audio_path}: {average_volume} dBFS")

def print_dir(directory_path):
    # 遍历目录
    for filename in os.listdir(directory_path):
        # 构建完整的文件路径
        ext = os.path.splitext(filename)[1].lower()
        if ext == '.mp3':
            print(filename, end=": ")
            print_audio_volume2(os.path.join(directory_path, filename))

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

def mod_audio_volume(in_path, out_path, target_volume):
    for filename in os.listdir(in_path):
        if filename.endswith(".mp3"):
            # 构建完整的文件路径
            in_file_path = os.path.join(in_path, filename)
            out_file_path = os.path.join(out_path, filename)
            # 加载音频文件
            mod_file_audio(in_file_path, out_file_path, target_volume)


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
    main()
    #mod_audio_volume(directory_path)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
