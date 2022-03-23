"""
 * Project name(项目名称)：Python字符串拼接和截取字符串
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 19:18
 * Version(版本): 1.0
 * Description(描述)： Python字符串拼接

 str() 用于将数据转换成适合人类阅读的字符串形式。
repr() 用于将数据转换成适合解释器阅读的字符串形式（Python 表达式的形式），适合在开发和调试阶段使用；
        如果没有等价的语法，则会发生 SyntaxError 异常。
 """

if __name__ == '__main__':
    str1 = "123"
    str2 = "456"
    str3 = "123""4567"
    str4 = str1 + str2
    print(str1)
    print(str2)
    print(str3)
    print(str4)
    num = 12
    str5 = "数字" + str(num) + "."
    str6 = "数字" + repr(num) + "."
    print(str5)
    print(str6)

    s = "12345"
    s_str = str(s)
    s_repr = repr(s)
    print(type(s_str))
    print(s_str)
    print(type(s_repr))
    print(s_repr)


    input()
