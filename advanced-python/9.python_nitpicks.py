# 1. For-else . flag 사용해서 반복문 돌면서 특정 값을 찾으려 할때 효율적일듯?1
for server in servers:
    if server.check():
        logger.info("Found server")
        primary_server = server
        break
# break 되지 않았을 경우에
else:
    logger.info("No server found")



# 2. Walrus -> go 언어랑 비슷
if response := pattern.search(line):
    print("yes")
else:
    print("non")


# 3. short circuit evaluation, chain 구조로 앞 부터 none 인 경우 뒤 값을 적용해줌. 
# 단순 값 할당을 위한 if-else 문에서 쓰면 좋을덧 
username, full_name = get_user_info()

display_name = username or full_name or "Anonymous"

# 4. Operator Chaining
if 0 < x < 10:
    print("x is between 0 and 10")