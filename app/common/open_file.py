import subprocess

def open_word(url):
    subprocess.Popen('start {} '.format(url), shell=True)

def open_dir(url):
    subprocess.Popen('start {} '.format(url), shell=True)


#open_word('\"C:\\Users\\77902\\Desktop\\1124.docx\"')