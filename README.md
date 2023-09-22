# DHU-LessonSelect
东华大学选课脚本

## 简单说明
 - 你需要在学校内网环境下使用本脚本（VPN或校园网）
 - 修改 py 文件中的选课代号
 - 获取你的 cookie（JSESSIONID） 并输入到 `token.txt` 中

## 进阶内容
如果你想一次抢多门课，你可以写一个像这样的批处理文件
```
wt python ./266156.py
wt python ./266150.py
wt python ./266687.py
wt python ./267967.py
......
```
