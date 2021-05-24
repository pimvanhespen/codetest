module Codetest
{
	interface Health
	{
		double GetWallclockTime();
		long GetFreeMemory();
		void GetResponse();
	}
}