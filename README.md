Autorippr
=========

Autorippr is currently unmaintained. I am lacking in free time to work on this myself but am happy to accept pull requests or make someone a maintainer of the project. 

That said it should still work for most cases.


## Copyright & License

Copyright (c) 2012 Jason Millward - Released under the [MIT license](LICENSE).


## Updates and modifications by BoxOfSnoo

I have compiled useful portions from a few forks of the original

https://github.com/MartinHell/Autorippr/network

- Brought up to Ubuntu 18.04
- Lots of updates and commits

https://github.com/tmcdonagh/Autorippr/network

- Cool script to automatically find the latest version without hardcoding

## Running

As described in the `build-docker.sh` script,

```
$ build-docker.sh
$ docker run -ti -v /tmp:/tmp  --device=/dev/sr1 autorippr --all --debug
```
