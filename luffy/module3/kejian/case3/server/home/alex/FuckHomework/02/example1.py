
with open("a.txt", "r", encoding="utf-8") as f:
    for line in f:
    #     print(line)
        print(line.strip().split())

    # [{‘name’:'apple','price':10,'count':3}, {...},{...},...]
    # print([{'name':line.strip().split()[0],'price':line.strip().split()[1],'count':line.strip().split()[2]} for line in f])
    # for i in [{'name':line.strip().split()[0],'price':line.strip().split()[1],'count':line.strip().split()[2]} for line in f]:
    #     print(i)
