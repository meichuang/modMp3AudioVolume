depends:
    numpy
    pydub

用法：
  python modMp3Audio.py -q 文件名  # 执行 查询单个文件的音量 操作
  python modMp3Audio.py -qa 目录名  # 执行 查询目录下所有文件的音量 操作
  python modMp3Audio.py -c 文件名 音量  # 执行 修改单个文件的音量 操作
  python modMp3Audio.py -ca 源目录 目的目录 音量  # 执行 修改目录下所有文件音量 操作

说明：
  音量-8是一个比较大的声音了