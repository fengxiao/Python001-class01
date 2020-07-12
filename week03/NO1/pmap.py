import ipaddress
import json
import argparse
import subprocess
import sys
import telnetlib
from concurrent.futures import ThreadPoolExecutor


def pingcheck(ip):
    p = subprocess.Popen(["ping.exe", ip],
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=True)

    out = p.stdout.read()
    # print(str(out, "GBK"))
    if "无法访问目标主机" in str(out, "GBK"):
        pass
        # print(f"{ip}访问异常")
    else:
        print(f"{ip}——访问正常")

def portcheck(ipandport):
    [ip, port] = ipandport.split(":")
    try:
        tn = telnetlib.Telnet(ip, port)
        print(f"{ip}:{port}——端口访问正常")
    except Exception as e:
        print(f"{ip}:{port}——端口访问异常")

def getiplist(ip):
    [start, end] = ip.split("-")
    parts = start.split(".")[:-1]
    parts.append("0")
    network = ipaddress.ip_network(".".join(parts) + "/24")
    iplist = [
        str(i)
        for i in network.hosts()
        if i >= ipaddress.ip_address(start) and i <= ipaddress.ip_address(end)
    ]
    return iplist

def getipandportlist(ip):
    list = []
    for i in range(75,85):
        list.append(f"{ip}:{i}")
    return  list


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
    if scantype =="ping":
        iplist = getiplist(ip)
        with ThreadPoolExecutor(workers) as executor:
            executor.map(pingcheck, iplist)
    if scantype == "tcp":
        portlist = getipandportlist(ip)
        with ThreadPoolExecutor(workers) as tcpexecutor:
            tcpexecutor.map(portcheck, portlist)