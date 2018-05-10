from topN import topN
import unittest
import os


class TopNTestCases(unittest.TestCase):
    # test top_n with nothing
    def test_top_n_w_empty_list(self):
        self.assertEqual([], topN([], 5))

    # test top_n with negative int
    def test_top_n_w_neg_n(self):
        with self.assertRaises(TypeError):
            topN([1, 2, 3, 4, 5], -10)

    # test top_n with a few different lists
    def test_top_n_from_lists(self):
        self.assertEqual([19, 18, 17, 16], topN(range(20), 4))
        self.assertEqual([88, 9, 7], topN([2, 4, 7, 2, 88, 9], 3))
        self.assertEqual([3, 2, 1], topN([1, 2, 3], 5))

    # test top_n from a file
    def test_top_n_from_file(self):
        real_top_n = [99999] * 5
        # create an input file
        with open('test_input.txt', 'w') as in_file:
            # put some junk in
            in_file.writelines('\n'.join([str(i) for i in range(1000)]))
            in_file.write('\n')
            # now write the winners
            in_file.writelines('\n'.join([str(i) for i in real_top_n]))

        # read from input file, call topN and write results to file
        with open('test_input.txt', 'r') as in_file:
            with open('test_output.txt', 'w') as out_file:
                top_n = topN(in_file, 5)
                out_file.write('\n'.join([str(i) for i in top_n]))

        # now make sure we've written the correct output
        with open('test_output.txt', 'r') as out_file:
            test_output = [int(line) for line in out_file]
            self.assertEqual(real_top_n, test_output)

        # now remove the files
        for file in ['test_input.txt', 'test_output.txt']:
            if os.path.exists(file):
                os.remove(file)


if __name__ == '__main__':
    unittest.main()
