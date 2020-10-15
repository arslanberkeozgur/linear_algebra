# berke ozgur arslan


sin = __import__('math').sin
cos = __import__('math').cos
asin = __import__('math').asin
acos = __import__('math').acos
sqrt = __import__('math').sqrt
PI = __import__('math').pi


# ----------------------------------------------------------------------------------------------------------------------


class matrix():

    def __init__(self, *args):
        for i in range(len(args)-1):
            if len(args[i]) == len(args[i+1]):
                continue
            else:
                raise Exception(f'Inconsistent number of columns in row {args.index(args[i])+1 }')
        self.itself = [[element for element in row] for row in args]
        self._rowcount = 0
        self._colcount = 0
        self._rows = object
        self._columns = list

    def show(self):
        print(*self.itself, sep="\n")

    def scalar_multiple(self, scalar):
        scalar_multiple = matrix(*[[element * scalar for element in row] for row in self.itself])
        return scalar_multiple

    @property
    def rowcount(self):
        self._rowcount = len(self.itself)
        return self._rowcount

    @property
    def colcount(self):
        self._colcount = len(self.itself[0])
        return self._colcount

    @property
    def rows(self):
        self._rows = self.itself
        return self._rows

    @property
    def columns(self):
        self._columns = [[row[i] for row in self.itself] for i in range(self.colcount)]
        return self._columns

class vector():

    def __init__(self, *args):
        self.itself = [[element] for element in args[0]]
        self._rowcount = 0
        self.colcount = 1
        self._norm = 0

    def show(self):
        print(*self.itself, sep="\n")

    def scalar_multiple(self, scalar):
        scalar_multiple = vector([element[0] * scalar for element in self.itself])
        return scalar_multiple

    @property
    def rowcount(self):
        self._rowcount = len(self.itself)
        return self._rowcount

    @property
    def norm(self):
        self._norm = __import__('math').sqrt(dot_product(self, self))
        return self._norm

    def isparallel(self, vect):
        if self.rowcount == vect.rowcount:
            for i in range(self.rowcount - 1):
                if self.itself[i][0] / vect.itself[i][0] == self.itself[i+1][0] / vect.itself[i+1][0]:
                    continue
                else:
                    return False
            return True
        else:
            raise Exception('Cannot operate on vectors of different dimensions')

    def isorthogonal(self, vect):
        if self.rowcount == vect.rowcount:
            if dot_product(self, vect) == 0:
                return True
            else:
                return False
        else:
            raise Exception('Cannot operate on vectors of different dimensions')

    def projection(self, v1, rnd=16):
        c = round(dot_product(self, v1) / (v1.norm**2), rnd)
        projection = v1.scalar_multiple(c)
        return projection

    def anglebetween(self, v1, rnd=16):
        cosine = dot_product(self, v1) / (self.norm * v1.norm)
        angle = round(acos(cosine), rnd)
        return angle


# ----------------------------------------------------------------------------------------------------------------------


x_hat2 = vector((1, 0))
y_hat2 = vector((0, 1))
x_hat = vector((1, 0, 0))
y_hat = vector((0, 1, 0))
z_hat = vector((0, 0, 1))


# ----------------------------------------------------------------------------------------------------------------------


def addition(*args):
    try:
        zero = [[0 for i in range(len(row))] for row in args[0].itself]
        for i in args:
            zero = [[zero[r][c] + i.itself[r][c] for c in range(len(i.itself[r]))] for r in range(len(i.itself)) ]
        if isinstance(args[0],matrix):
            zero = matrix(*zero)
        elif isinstance(args[0],vector):
            for i in range(len(zero)):
                zero[i] = zero[i][0]
            zero = vector(*zero)
        return zero
    except IndexError:
        print("\nAdditionError: Inconsistent number of columns or rows")


def multiplication(*args):
    for i in range(len(args) - 1):
        if args[i].colcount == args[i + 1].rowcount:
            continue
        else:
            raise Exception(f'Impossible to multiply arguments {args.index(i) + 1} and {args.index(i + 1) + 1}')

    product = [[0 for col in range(args[1].colcount)] for row in range(args[0].rowcount)]

    if len(args) == 2:
        for j in range(args[0].rowcount):
            for k in range(args[1].colcount):
                product[j][k] = sum([args[0].itself[j][m] * args[i + 1].itself[m][k] for m in range(args[0].colcount)])
        product = matrix(*product)
        return product

    p = args[0].itself

    for i in range(len(args) - 1):
        product = [[0 for col in range(args[i + 1].colcount)] for row in range(args[i].rowcount)]
        for j in range(args[i].rowcount):
            for k in range(args[i + 1].colcount):
                product[j][k] = sum([p[j][m] * args[i + 1].itself[m][k] for m in range(args[i].colcount)])

        p = product.copy()

    product = matrix(*p)
    return product


def power(m,p):

    if p > 1:
        power_list = [m for i in range(p)]
        return multiplication(*power_list)
    elif p == 1:
        return m
    else:
        raise Exception('Invalid entry')


def dot_product(v1, v2):
    if isinstance(v1, vector) and isinstance(v2, vector):
        if v1.rowcount == v2.rowcount:
            dot_p = 0
            for i in range(v1.rowcount):
                dot_p += v1.itself[i][0] * v2.itself[i][0]
            return dot_p
        else:
            raise Exception('Cannot take dot product of vectors of different dimensions')
    else:
        raise Exception('Dot product is only applicable to vectors')


# ----------------------------------------------------------------------------------------------------------------------


def complex_length(cmplx):
    r = sqrt(cmplx.real ** 2 + cmplx.imag ** 2)
    return r


def polar_form(cmplx,rnd=16):
    r = complex_length(cmplx)
    theta = round(acos(cmplx.real/r), rnd)
    return r, theta







