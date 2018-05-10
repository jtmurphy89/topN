import argparse
import heapq


def topN(itr, n):
    """
        Takes a file or list of integers and return the largest n among them,
        in decreasing order.

    :param itr: Iterable of ints
    :param n: Positive integer
    :return: list of largest n ints in itr, in decreasing order.
    """
    top_n_ints = []
    if n < 0:
        raise TypeError("Input {} must be a non-negative integer".format(n))
    if n == 0:
        return top_n_ints
    for item in itr:
        # I'm assuming that I'm always going to be given
        # something that can be converted to an int here...
        # Or, at least, that's the way i'm interpreting the
        # statement that the input file "[contains] individual
        # numbers on each line." If I happen to not be given
        # an int here, I would rather the conversion fail and
        # a ValueError be raised (mostly because I just want
        # the comparisons to always be between objects of the
        # same type. Obviously, I could modify this
        # behavior as needed (e.g. try/except block).
        num = int(item)
        if len(top_n_ints) < n:
            heapq.heappush(top_n_ints, num)
        elif len(top_n_ints) == n and num > top_n_ints[0]:
                heapq.heapreplace(top_n_ints, num)
    return sorted(top_n_ints, reverse=True)


def check_n(n):
    if n.isdigit() and int(n) >= 0:
        return int(n)
    else:
        raise argparse.ArgumentTypeError("Input {} must be a valid, nonnegative integer".format(n))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Given an input file and a number N, outputs the largest N numbers, in decreasing order."
    )
    parser.add_argument('input_file', help="Location of input file. Must have only 1 int on each line.")
    parser.add_argument('N', help='Number of the largest elements to output.', type=check_n)
    parser.add_argument('output_file', help='Location to write the top N numbers of input_file.')
    args = parser.parse_args()

    with open(args.input_file, 'r') as in_file:
        with open(args.output_file, 'w') as out_file:
            top_n = topN(in_file, args.N)
            out_file.write('\n'.join([str(i) for i in top_n]))

