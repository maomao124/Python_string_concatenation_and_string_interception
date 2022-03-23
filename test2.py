"""
 * Project name(项目名称)：Python字符串拼接和截取字符串
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 19:24
 * Version(版本): 1.0
 * Description(描述)： 截取字符串

 获取单个字符
知道字符串名字以后，在方括号[ ]中使用索引即可访问对应的字符
str name[index]
str name 表示字符串名字，index 表示索引值。
Python 允许从字符串的两端使用索引：
当以字符串的左端（字符串的开头）为起点时，索引是从 0 开始计数的；字符串的第一个字符的索引为 0，第二个字符的索引为 1，第三个字符串的索引为 2 ……
当以字符串的右端（字符串的末尾）为起点时，索引是从 -1 开始计数的；字符串的倒数第一个字符的索引为 -1，倒数第二个字符的索引为 -2，倒数第三个字符的索引为 -3

使用[ ]除了可以获取单个字符外，还可以指定一个范围来获取多个字符，也就是一个子串或者片段
str name[start : end : step]
对各个部分的说明：
str name：要截取的字符串；
start：表示要截取的第一个字符所在的索引（截取时包含该字符）。如果不指定，默认为 0，也就是从字符串的开头截取；
end：表示要截取的最后一个字符所在的索引（截取时不包含该字符）。如果不指定，默认为字符串的长度；
step：指的是从 start 索引处的字符开始，每 step 个距离获取一个字符，直至 end 索引出的字符。step 默认值为 1，当省略该值时，最后一个冒号也可以省略。
 """

if __name__ == '__main__':
    str1 = "The index of the first character of the string is 0"
    print(str1)
    print(str1[15])
    print(str1[29])
    print(str1[18])
    print(str1[14])
    print(str1[10])
    print(str1[3:15])
    print(str1[:10])
    print(str1[::2])
    print(str1[11:])

    input()
