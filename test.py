import argparse
import pprint
from test import run_tests

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", type=str, default=None,
                    help="Name of a test to run")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()

if args.verbose:
    pp = pprint.PrettyPrinter(indent=4)

results = run_tests(args.verbose, args.test)

if not args.verbose:
    del results["results"]

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(results)
