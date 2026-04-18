# LegacyProject
Home exercise

---
For the first (shared) library libcore the conan had to build it:
```python
======== Computing dependency graph ========
Graph root
    cli
Requirements
    libcore/1.0.0#a485b52086419056cc8f4bc0fa6dca79 - Cache

======== Computing necessary packages ========
libcore/1.0.0: Forced build from source
Requirements
    libcore/1.0.0#a485b52086419056cc8f4bc0fa6dca79:38b8b2863892fd9462affa45e40edf183b436246 - Build
```

For the libmarket that depends on libcore only the libmarked had to be build, the libcore is provided by conan cache:
```python
======== Computing dependency graph ========
Graph root
    cli
Requirements
    libcore/1.0.0#a485b52086419056cc8f4bc0fa6dca79 - Cache
    libmarket/1.0.0#e68fdb83961636fb437ae7588744bd5b - Cache

======== Computing necessary packages ========
libmarket/1.0.0: Forced build from source
Requirements
    libcore/1.0.0#a485b52086419056cc8f4bc0fa6dca79:38b8b2863892fd9462affa45e40edf183b436246#b4bff65c4c0e6ef035e00d1303d28ad9 - Cache
    libmarket/1.0.0#e68fdb83961636fb437ae7588744bd5b:3bba3f553868fea9f13bc993604ca96f3aba84e5 - Build
```

For the static library:
```python
======== Computing dependency graph ========
Graph root
    cli
Requirements
    libutils/1.0.0#b653bb5ecb047eea0482b0022c5abda8 - Cache

======== Computing necessary packages ========
libutils/1.0.0: Forced build from source
Requirements
    libutils/1.0.0#b653bb5ecb047eea0482b0022c5abda8:38b8b2863892fd9462affa45e40edf183b436246 - Build
```

For the engine:
```python
======== Computing dependency graph ========
Graph root
    conanfile.py: /data/LegacyProject/engine/conanfile.py
Requirements
    libcore/1.0.0#a485b52086419056cc8f4bc0fa6dca79 - Cache
    libmarket/1.0.0#e68fdb83961636fb437ae7588744bd5b - Cache
    libutils/1.0.0#b653bb5ecb047eea0482b0022c5abda8 - Cache

======== Computing necessary packages ========
Requirements
    libcore/1.0.0#a485b52086419056cc8f4bc0fa6dca79:38b8b2863892fd9462affa45e40edf183b436246#b4bff65c4c0e6ef035e00d1303d28ad9 - Cache
    libmarket/1.0.0#e68fdb83961636fb437ae7588744bd5b:3bba3f553868fea9f13bc993604ca96f3aba84e5#6df9cc1a53e525b2faee6b9da0bc2a83 - Cache
    libutils/1.0.0#b653bb5ecb047eea0482b0022c5abda8:38b8b2863892fd9462affa45e40edf183b436246#8c6c8f678c43c1247e5db7e8e2e18f23 - Cache

======== Installing packages ========
libcore/1.0.0: Already installed! (1 of 3)
libutils/1.0.0: Already installed! (2 of 3)
libmarket/1.0.0: Already installed! (3 of 3)
```

For the gateway:
```python
======== Computing dependency graph ========
Graph root
    conanfile.py: /data/LegacyProject/gateway/conanfile.py
Requirements
    libcore/1.0.0#a485b52086419056cc8f4bc0fa6dca79 - Cache
    libutils/1.0.0#b653bb5ecb047eea0482b0022c5abda8 - Cache

======== Computing necessary packages ========
Requirements
    libcore/1.0.0#a485b52086419056cc8f4bc0fa6dca79:38b8b2863892fd9462affa45e40edf183b436246#b4bff65c4c0e6ef035e00d1303d28ad9 - Cache
    libutils/1.0.0#b653bb5ecb047eea0482b0022c5abda8:38b8b2863892fd9462affa45e40edf183b436246#8c6c8f678c43c1247e5db7e8e2e18f23 - Cache

======== Installing packages ========
libcore/1.0.0: Already installed! (1 of 2)
libutils/1.0.0: Already installed! (2 of 2)
```
