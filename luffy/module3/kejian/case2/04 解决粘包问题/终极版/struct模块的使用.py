import struct
import json


# res=struct.pack('i',1230)
# print(res,type(res),len(res))
#
#
# #client.recv(4)
# obj=struct.unpack('i',res)
# print(obj[0])



# res=struct.pack('i',12300000000)

# res=struct.pack('l',111232301212312312312312000000)
# print(res,len(res))


header_dic = {
    'filename': 'a.txt',
    'md5': 'xxdxxx',
    'total_size': 33333333333333123123123123123333333333234239487239047902384729038479023874902387409237848902374902837490238749082374908237492837498023749082374902374890237498237492837409237409237402397420398749203742093749230749023874902387492083749023874029837420893479072839048723980472390874
}

header_json = json.dumps(header_dic)
# print(type(header_json))
header_bytes=header_json.encode('utf-8')

# print(type(header_bytes))

# print(len(header_bytes))

struct.pack('i',len(header_bytes))