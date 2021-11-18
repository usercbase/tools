## 说明

用来快速获取disable_functions有没有遗漏的
示例：

```
python disable_functions_leak.py pcntl_wifexited,pcntl_wifstopped    //后面跟phpinfo()得到的disable_functions
```

