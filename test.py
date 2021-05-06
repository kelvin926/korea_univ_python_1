d = {"s1":{"year":4, "g":"F"}, "s2":{"year":3, "g":"M"}}
for k, v in d.items():
    print(k, v["year"]*v["g"])