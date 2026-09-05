---
title: "Hello World - 测试文章"
date: 2024-09-03 22:30:00 +0800
categories: [测试, 示例]
tags: [hello, jekyll, chirpy]
---

# 欢迎来到我的博客

这是一篇测试文章，用于验证 Jekyll + Chirpy 主题是否正常工作。

## 测试内容

### 代码块

```python
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)   # 输出结果：3.0 -4.5

def hello_world():
    print("Hello, World!")
    return "Welcome to my blog!"

hello_world()
```

```c
#include <stdio.h>
struct agent{
int session;
int a;
char type;
}Agent;

void swap(int *a,int *b){
    int tmp;
    tmp=*a;
    *a=*b;
    *b=tmp;
}

int main(){

    return 0;
}
```

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

```csharp
using System;

class HelloWorld {
    static void Main() {
        Console.WriteLine("Hello, World!");
    }
}
```

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

```javascript
function helloWorld() {
    console.log("Hello, World!");
}

helloWorld();
```

```typescript
function helloWorld(): void {
    console.log("Hello, World!");
}

helloWorld();
```

```rust
fn main() {
    println!("Hello, World!");
}
```


### 列表情境

- 项目一：测试列表显示
- 项目二：验证主题样式
- 项目三：确认构建流程

### 引用

> 这是一段引用文本，用于测试引用样式是否正常显示。

### Prompts

> An example showing the `tip` type prompt.
{: .prompt-tip }

> An example showing the `info` type prompt.
{: .prompt-info }

> An example showing the `warning` type prompt.
{: .prompt-warning }

> An example showing the `danger` type prompt.
{: .prompt-danger }

## 总结

如果看到这篇文章，说明：

1. Jekyll 构建成功
2. Chirpy 主题正常工作
3. 文章发布流程正确

感谢阅读！
