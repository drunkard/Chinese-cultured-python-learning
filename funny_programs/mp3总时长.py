import eyed3
import os
import path

p = path.Path(os.getcwd())
tt = 0  # 总时长
for f in p.files('*.mp3'):
    f = eyed3.load(f)
    tt += f.info.time_secs
print(f'一共 {tt/3600} 小时')
