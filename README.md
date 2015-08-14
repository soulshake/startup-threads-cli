# Startup Threads CLI

Send t-shirts from the command line.

# Setup

You need to export your StartupThreads API key as an environment variable.

Add the following line to your bash profile:

```
export STARTUPTHREADS_API_KEY=''
```

Make sure to `source` your profile afterwards. You can check that it's set up correctly by running:

```
echo $STARTUPTHREADS_API_KEY
```

## Commands

```
$ swag inventory

name                 id        status    description      MS  MM    ML    MXL    M2XL      WS    WM    WL  WXL    W2XL  
-------------------  --------  --------  -------------  ----  ----  ----  -----  ------  ----  ----  ----  -----  ------
Motherboard Glow     3xyhor59  approved                    7  19    31    41     10         9     0     0              
No Bullshit Hashtag  jsi4_xay  approved                    5  13    26    16     9          6     0     2             
Invaders             rn2qjafd  approved                    9                                4     6     8            
Scribble (AA)        86dix_xv  approved                   15  0     6     3                10    10    20           
Scribble (Canvas)    zif5xjib  approved                   16  1     23    15               15    13    17          
Lotus                lzunev7m  approved                    4  7     21    23     6          3     0     2         

```


