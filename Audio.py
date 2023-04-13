__init__ = ('Audio')

import pyaudio
import wave
class Audio:
    def __init__(self, time, savePath: str):
        self.p = pyaudio.PyAudio()
        self.recordTime = time
        # CHANNELS=1#现在配置的是麦克风阵列
        # CHUNK=1024
        # RESPEAKER_RATE+=16000
        # RESPEAKER_WIDTH=2
        # WAVEOUTPUT="output.wav"
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            frames_per_buffer=self.CHUNK,
            input=True
        )
        self.wf = wave.open(savePath, 'wb')
        self.wf.setnchannels(self.CHANNELS)
        self.wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        self.wf.setframerate(self.RATE)

    def startRecord(self) -> str:
        try:
            import time
            delay=self.recordTime
            closetime=time.time()+delay
            # for i in tqdm.tqdm(range(0, int(self.RATE / self.CHUNK * int(self.recordTime)))):
            while time.time()<=closetime:
                data = self.stream.read(self.CHUNK)
                self.wf.writeframes(data)
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()
            self.wf.close()
            return "结束录音"
        except:
            import tqdm
            for i in tqdm.tqdm(range(0, int(self.RATE / self.CHUNK * self.recordTime))):
                data = self.stream.read(self.CHUNK)
                self.wf.writeframes(data)
            self.stream.stop_stream()
            self.stream.close()
            self.p.terminate()
            self.wf.close()
            return "结束录音"
