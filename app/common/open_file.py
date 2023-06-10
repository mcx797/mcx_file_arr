import subprocess

def open_word(url):
    subprocess.Popen('start winword ' + url , shell=True)