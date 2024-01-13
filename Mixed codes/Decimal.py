from decimal import Decimal, getcontext, Context
import decimal

new_context = Context(prec=9, rounding=decimal.ROUND_UP)
decimal.setcontext(new_context)

getcontext().traps[decimal.DivisionByZero] = False

a = Decimal(0.3)
print(a.quantize(Decimal('0.0000')))