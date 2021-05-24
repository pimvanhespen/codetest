using Codetest;

namespace App
{
    public class MemoryI : MemoryDisp_
    {
        public override long GetFreeMemory(Ice.Current current = null)
        {
            var metrics = MemoryMetricsClient.GetMetrics();
            return (long)metrics.Free;
        }
    }
}