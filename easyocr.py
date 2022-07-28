from cnocr import CnOcr

ocr = CnOcr()
res = ocr.ocr('ocr.png')
a = res[0][0]
print(''.join(a))
res = ''.join(a)
