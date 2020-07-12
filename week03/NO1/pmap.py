
import json
import argparse
import subprocess
import sys

def ping(ip):
    p = subprocess.Popen(["ping.exe", ip],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=True)

    out = p.stdout.read()
    # print(str(out, "GBK"))
    if "无法访问目标主机" in str(out, "GBK"):
        print("0")
    else:
        print("1")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-n", type=int, help="指定并发数量", default="4")
    parser.add_argument("-f", help="扫描类型：ping or tcp", default="ping")
    parser.add_argument("-ip", help="指定IP范围")
    parser.add_argument("-w", help="指定文件名称")

    args = parser.parse_args()
    workers = args.n
    scantype = args.f
    ip = args.ip
    filename = args.w
    # print(f"{workers},{scantype},{ip},{filename}")
    ping(ip)