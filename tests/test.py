import test_ownfunctions
import test_geocache
import test_user_io

verbosity = input("Verbosity (1 oder 2): ")

test_ownfunctions.main(verbosity)
test_geocache.main(verbosity)
test_user_io.main(verbosity)