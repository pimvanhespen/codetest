using System;

namespace App
{
    public class Program
    {
        static int Main(string[] args)
        {
            try
            {
                using var communicator = Ice.Util.initialize(ref args, "config.server");

                // todo: replace to config
                var adapter =
                    communicator.createObjectAdapterWithEndpoints("Health",
                        "default -h localhost -p 10000");
                adapter.add(new MemoryI(), Ice.Util.stringToIdentity("FreeMemory"));
                adapter.add(new WallclockI(), Ice.Util.stringToIdentity("Wallclock"));
                adapter.add(new ResponseI(), Ice.Util.stringToIdentity("Response"));
                
                adapter.activate();

                communicator.waitForShutdown();
            }
            catch (System.Exception e)
            {
                Console.Error.WriteLine(e);
                return 1;
            }

            return 0;
        }
    }
}