import requests

def main():
	try:
		ip=""   # 修改此处即可
		url=ip+":888/pma"
		r=requests.get(url)
		if r.status_code is 200:
			print("可能存在漏洞")
		else:
			print("不存在漏洞")
		
	except:
		pass

if __name__=="__main__":
	main()