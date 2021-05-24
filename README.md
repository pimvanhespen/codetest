# codetest

## Client
When running the client on a Linux machine use: 
```sh
    sudo apt-get install zeroc-ice-all-runtime
```   
or for development:
```sh
    sudo apt-get install zeroc-ice-all-dev
```    
more info: https://doc.zeroc.com/ice/3.7/release-notes/using-the-linux-binary-distributions .    
    
### Get and run
```sh
    git clone https://github.com/pimvanhespen/codetest.git
    cd codetest/Client
    python3 client.py --Ice.Config=/path/to/config
```

example local config:   
```
    Memory.Proxy=FreeMemory:tcp -p 10000:udp -p 10000:ssl -p 10001
    Wallclock.Proxy=Wallclock:tcp -p 10000:udp -p 10000:ssl -p 10001
    Response.Proxy=Response:tcp -p 10000:udp -p 10000:ssl -p 10001
```   
  
example external config
```
    Memory.Proxy=FreeMemory:tcp -h codetest.iperitydev.com -p 10000:udp -h codetest.iperitydev.com -p 10000:ssl -h codetest.iperitydev.com -p 10001
    Wallclock.Proxy=Wallclock:tcp -h codetest.iperitydev.com -p 10000:udp -h codetest.iperitydev.com -p 10000:ssl -h codetest.iperitydev.com -p 10001
    Response.Proxy=Response:tcp -h codetest.iperitydev.com -p 10000:udp -h codetest.iperitydev.com -p 10000:ssl -h codetest.iperitydev.com -p 10001
```

## Server
```sh
    git clone https://github.com/pimvanhespen/codetest.git
    cd codetest/Server/App
    dotnet publish
    /bin/Debug/net5.0/App --Ice.Config=/path/to/config
```  

example config:   
```
    Health.Endpoints=tcp -p 10000:udp -p 10000:ssl -p 10001
```