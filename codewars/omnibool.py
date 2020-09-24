# omnibool.py
# https://www.codewars.com/kata/5a5f9f80f5dc3f942b002309/train/python

class Omnibool():
    def __eq__(self, x):
        return True

if __name__ == "__main__":
    omnibool = Omnibool()
    print(omnibool == True and omnibool == False)
