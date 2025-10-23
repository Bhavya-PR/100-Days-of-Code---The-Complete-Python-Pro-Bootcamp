def add(*args):
    value = 0
    for num in args:
        value += num
    print(value)
def check(**kwargs):
    color = kwargs["color"]
    model = kwargs.get("model")
    print(color,model)

check(color="red")
# print(check.model)

add(1,2,3)

add(30,50,20,500)
