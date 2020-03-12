import os, sys
import subprocess
from scipy.io import wavfile

def ffmpeg_AudioToAudio(audioPath, WavPath):
    # 提取视频路径下所有文件名
    audios = os.listdir(audioPath)
    count = 0
    for audio in audios:
        if audio.find('.') < 0 :
            targetPath = WavPath+"\\" + audio
            if False == os.path.exists(targetPath):
                os.makedirs(targetPath)
            ffmpeg_AudioToAudio(audioPath +"\\" + audio, targetPath)
        else:
            # 提取视频的全路径名（含路径+文件名）
            audio_path = audioPath + "\\" + audio
            # 合成输出音频的全路径名（不含后缀）
            wav_path = WavPath + "\\" + os.path.splitext(audio)[0]
            # 提取视频中的音频信息
            strcmd = "ffmpeg -i " + audio_path + " -f wav " + wav_path + ".wav"
            subprocess.call(strcmd, shell=True)

audioPath = os.getcwd() + "\\source"
WavPath = os.getcwd() + "\\target"

ffmpeg_AudioToAudio(audioPath,WavPath)

