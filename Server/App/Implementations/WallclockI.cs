using System;
using System.Threading;
using Codetest;
using Ice;

namespace App
{
    public class WallclockI : WallclockDisp_
    {
        public override double GetWallclockTime(Current current = null)
        {
            var start = DateTime.Now;
            Thread.Sleep(1000);
            var elapsed = DateTime.Now - start;
            return elapsed.TotalSeconds;
        }
    }
}