# import urllib.request as request
# import json

# main_url = "http://dontpad.com/"
# page = request.urlopen('http://dontpad.com/testandfsdkf')

# def read_raw(page):
# 	with request.urlopen(main_url + page + ".body.json?lastUpdate=0") as response:
# 		resp = response.read()
# 	return resp

# def read(page, full_json=False):
# 	content = json.loads(read_raw(page).decode())
# 	if "body" in content:
# 		return content["body"] if not full_json else content
# 	return ""


# while read("testandfsdkf") == None:
#     continue
# print(read("testandfsdkf"))

code = "G-113214 é seu código de verificação do Google."
print(code[2:8])