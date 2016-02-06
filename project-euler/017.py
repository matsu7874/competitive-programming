"""
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""


def spell_number(n):
    if n <= 0:
        return ''
    if 0 <= n < 10:
        return ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'][n]
    if n < 20:
        return ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'][n-10]
    if n >= 1000:
        return  spell_number(n//1000) + 'thousand' + spell_number(n%1000)
    if n >= 100:
        if n % 100 == 0:
            return spell_number(n//100) + 'hundred'
        else:
            return spell_number(n//100) + 'hundred' + 'and' + spell_number(n%100)
    else:
        if n % 10 == 0:
            return ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'][n//10]
        else:
            return ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'][n//10] + spell_number(n%10)

t = 0
for i in range(1,1000+1):
    # print(spell_number(i))
    t += len(spell_number(i))
print(t)
