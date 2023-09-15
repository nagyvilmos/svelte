import argparse
import pprint
from test import run_tests

parser = argparse.ArgumentParser(description="Run application tests")

parser.add_argument("-t", "--test", type=str, default=None,
                    help="Comma seperate list of tests to run; the function name and not the description")
parser.add_argument("-f", "--file", type=str, default=None,
                    help="Comma seperate list of files to run; does not include the .py extension")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
parser.add_argument("-l", "--loud", action="store_true",
                    help="return full result object rather than summary")
parser.add_argument("-s", "--silent", action="store_true",
                    help="suppress output of function results")
args = parser.parse_args()

pp = pprint.PrettyPrinter(indent=2,compact=False)

if args.verbose:
    pp.pprint(args)
test_list = [x.strip() for x in args.test.split(',')] if args.test is not None else None
test_files = [x.strip() for x in args.file.split(',')] if args.file is not None else None
results = run_tests(args.verbose or not args.silent, args.loud and not args.silent, test_list, test_files, pp)

if not args.verbose:
    del results["results"]

pp.pprint(results)
