def piramide(n):
    ul = n-1
    ast = 1
    for i in range(n):
        while ul >= 0:
            print('%s%s%s' % (('_'*ul), ('*'*ast), ('_'*ul)))
            ul -= 1
            ast += 2
