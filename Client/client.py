import sys
import timeit
import Ice
import Codetest


def get_memory(communicator):
	base = communicator.propertyToProxy("Memory.Proxy")
	prx = Codetest.MemoryPrx.checkedCast(base)
	if not prx:
		raise RuntimeError("Invalid proxy")

	free = prx.GetFreeMemory()
	return free


def get_wallclock(communicator):
	base = communicator.propertyToProxy("Wallclock.Proxy")
	prx = Codetest.WallclockPrx.checkedCast(base)
	if not prx:
		raise RuntimeError("Invalid proxy")

	time = prx.GetWallclockTime()
	return time


def get_responsetime(communicator):
	base = communicator.propertyToProxy("Response.Proxy")
	prx = Codetest.ResponsePrx.checkedCast(base)
	if not prx:
		raise RuntimeError("Invalid proxy")

	elapsed = timeit.timeit(lambda: prx.GetResponse(), number=10)
	return elapsed


with Ice.initialize(sys.argv, "client.config") as communicator:
	print("Free memory: ", get_memory(communicator))
	print("Time: ", get_wallclock(communicator))
	print("Response time: ", get_responsetime(communicator))

