# 美化的curl-httpstat

## httpstat

![](http://oy3mfxixl.bkt.clouddn.com/201712201601_736.png)

httpstat 用优雅简洁的统计方式展现了curl的结果

It is a **single file🌟** Python script that has **no dependency👏** and is compatible with **Python 3🍻**.

> 它是一个简单的无依赖的Python3脚本

## Installation

- Download the script directly: `wget https://raw.githubusercontent.com/reorx/httpstat/master/httpstat.py`
- Through pip: `pip install httpstat`
- Through homebrew (macOS only): `brew install httpstat`

> For Windows users, @davecheney's [Go version](https://github.com/davecheney/httpstat) is suggested. → [download link](https://github.com/davecheney/httpstat/releases)

## Usage

Simply:

```
python httpstat.py httpbin.org/get
```

If installed through pip or brew, you can use `httpstat` as a command:

```
httpstat httpbin.org/get
```

### cURL Options

Because `httpstat` is a wrapper of cURL, you can pass any cURL supported option after the url (except for `-w`, `-D`, `-o`, `-s`, `-S` which are already used by `httpstat`):

> hrrpstat 等同于包装了的cURL，cURL支持的选项，httpstat都支持

```
httpstat httpbin.org/post -X POST --data-urlencode "a=b" -v
```

### Environment Variables

`httpstat` has a bunch of environment variables to control its behavior. Here are some usage demos, you can also run `httpstat --help` to see full explanation.

> httpstat有一些环境变量来控制其行为。这里有一些使用演示，你也可以运行httpstat --帮助看到完整的解释。

