tam = float(input("Insira um valor em metros: "))
print('{} metros convertidos sao:\n{:.0f}mm\n{:.0f}cm\n{:.0f}dm\n{:.1f}dam\n{:.2f}hm\n{:.3f}km'.format(tam, tam*1000, tam*100, tam*10, tam/10, tam/100, tam/1000))
