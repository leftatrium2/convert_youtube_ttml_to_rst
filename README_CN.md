# convert_youtube_ttml_to_srt

众所周知，youtube网站的默认字幕格式是VTT格式。

跟普通视频网站常用的SRT格式不同，尤其是使用机器翻译转换的字幕，直接用ffmpeg转换为SRT格式后
会出现：
1、字幕重复
2、时间轴不对应
等问题

这个项目，就是将youtube网站的字幕，转换为正常的SRT格式

```python
【requirements.txt】
yt_dlp==2024.3.10
```