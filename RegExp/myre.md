re模块函数
1.compile
2.match
3.search
4.findall
5.finditer
6.split
7.sub
8.purge
9.group
10.groups
11.groupdict


re.IGNORECASE 忽略大小写 同re.I
re.MULTILINE：多行模式，改变^和$的行为，同 re.M。
re.DOTALL：点任意匹配模式，让'.'可以匹配包括'\n'在内的任意字符，同 re.S。
re.LOCALE：使预定字符类 \w \W \b \B \s \S 取决于当前区域设定， 同 re.L。
re.ASCII：使 \w \W \b \B \s \S 只匹配 ASCII 字符，而不是 Unicode 字符，同 re.A。
re.VERBOSE：详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。主要是为了让正则表达式更易读，同re.X。
