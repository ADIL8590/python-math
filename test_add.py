# sum of numbers
def addition(a,b):
    return a+b
def test_addition_basic(a,b):
    assert addition(2,3)==5
    assert addition(-1,1)==0
    assert addition(0,0)==0
if __name__=="__main__":
    print(addition(2,3))











