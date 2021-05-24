import sys
import timeit
import Ice
import Codetest


def get_memory(communicator):
	base = communicator.stringToProxy("FreeMemory:default -p 10000")
	prx = Codetest.MemoryPrx.checkedCast(base)
	if not prx:
		raise RuntimeError("Invalid proxy")

	free = prx.GetFreeMemory()
	return free


def get_wallclock(communicator):
	base = communicator.stringToProxy("Wallclock:default -p 10000")
	prx = Codetest.WallclockPrx.checkedCast(base)
	if not prx:
		raise RuntimeError("Invalid proxy")

	time = prx.GetWallclockTime()
	return time


def get_responsetime(communicator):
	base = communicator.stringToProxy("Response:default -p 10000")
	prx = Codetest.ResponsePrx.checkedCast(base)
	if not prx:
		raise RuntimeError("Invalid proxy")

	elapsed = timeit.timeit(lambda: prx.GetResponse(), number=10)
	return elapsed


with Ice.initialize(sys.argv) as communicator:
	print("Free memory: ", get_memory(communicator))
	print("Time: ", get_wallclock(communicator))
	print("Response time: ", get_responsetime(communicator))

