#!/user/bin/env python
# -*- coding:utf-8 -*-
# 作者：周桂华
# 开发时间: 2021/4/17 19:56

import os
import glob
import pandas as pd
from datetime import datetime


class FileType(object):
    # 文件类型类 key为文件类型
    def __init__(self):
        self.fileTypeDict = {
            "图片": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", ".heif", ".psd"],
            "视频": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp",
                   ".mkv"],
            "音频": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", ".oga", ".raw",
                   ".vox", ".wav", ".wma"],
            "文档": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx",
                   ".docm", ".dox",
                   ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".pdf", ".md", ".xmind"],
            "压缩文件": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
            "文本": [".txt", ".in", ".out", ".json", "xml", ".log"],
            "程序脚本": [".py", ".html5", ".html", ".htm", ".xhtml", ".c", ".cpp", ".java", ".css", ".sql"],
            "可执行程序": [".exe", ".bat", ".lnk"],
            "字体文件": [".ttf", ".OTF", ".WOFF", ".EOT"]
        }

    # 判断文件类型
    def judge_file(self, pathname):
        """
        :param pathname:
        :return: 返回文件类型
        """
        for form, suffix in self.fileTypeDict.items():
            if pathname in suffix:
                return form
        return "无法判断类型文件"


# 需要整理的目标位置
class TargetLocation(object):
    def __init__(self):
        self.fileType = FileType()
        self.data = dict()

    def run(self):
        file_path = input("请输入需要整理的文件夹路径，回车键确定：")
        # 查找匹配的文件
        paths = glob.glob(file_path + "/*.*")
        print('paths-->', paths)
        # path为文件绝对路径
        for path in paths:
            try:
                if not os.path.isdir(path):
                    file = os.path.splitext(path)
                    filename, type = file
                    print('type-->', type)
                    print("filename-->", filename)
                    print('path-->', path)
                    dir_path = os.path.dirname(path)
                    print('dir_path-->', dir_path)
                    # 文件类型
                    form = self.fileType.judge_file(type)
                    self.data.setdefault(form, []).append(path)

            except FileNotFoundError:
                pass
        df = pd.DataFrame.from_dict(self.data, orient='index')
        # 获取桌面路径
        desktop_path = os.path.join(os.path.expanduser('~'), "Desktop/")
        file_name = datetime.now().strftime('%Y-%m-%d') + file_path.replace('\\', '_')\
            .replace(':', '_').replace('/', '_') + '.xlsx'
        excel_path = os.path.join(desktop_path, file_name)
        df.T.to_excel(excel_path, encoding='utf-8', sheet_name='文件分类')


if __name__ == '__main__':
    try:
        while True:
            desktopOrg = TargetLocation()
            desktopOrg.run()
            print("---->你的文件已经整理完成。")
            a = input('---->请按回车键退出,按其他键回车键确定继续整理：')
            if a == '':
                break
    except:
        print("ERROE:路径错误或有重复的文档")






















