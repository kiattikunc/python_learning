"3 large variable"
import sys
import math
from decimal import Decimal

print(0xff)

print(math.log(sys.maxsize,2))
print(math.factorial(52))

print(id(1))
print(id(2))
print(id(1+1))
a=1+1
print(id(a))
print(2**2048)
print(len(str(2**2048)))

"4 Decimal"

tax_rate=Decimal('7.25')/Decimal('100')

purchase_amount=Decimal('2.95')
print(tax_rate*purchase_amount)
penny=Decimal('0.01')
total_amount=purchase_amount+tax_rate*purchase_amount
print(total_amount.quantize(penny))
answer=(19/155)*(155/19)
print(round(answer))

print(math.frexp(8.066E+67))