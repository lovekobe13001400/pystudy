
#1.strip
mystr = '* hello world *'
mystr.strip('*')

#2.清理文本字符串

#大小写转换
mystr.upper()
mystr.lower()

#3.

s = 'pýtĥöñ\fis\tawesome\r\n'
remap = {
    ord('\t'):'',
    ord('\f'):'',
    ord('\r'):None
}
a = s.translate(remap)
#接着去除和音符
import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)  if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
b.translate(cmb_chrs)