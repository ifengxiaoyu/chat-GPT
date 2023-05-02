import time
import subprocess

def focus_timer(minutes):
    print("开始专注！")
    for i in range(minutes*60,0,-1):
        if i % 300 == 0:
            print(f"还有{i//60}分钟...")
        elif i % 60 == 0:
            print("还有1分钟...")
        time.sleep(1)
    print("时间到！")
    subprocess.call(['say', '时间到！'])

if __name__ == '__main__':
    focus_timer(25)  # 设定25分钟专注时间，可根据需要进行更改
