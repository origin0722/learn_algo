//输入一串字符（不超过255个字符），利用指针方式，将字符串中的大写字母转换成小写字母，并输出转换后的新串。
#include<stdio.h>
#include<string.h>
void change(char *s)
{
    while(*s!='\0')
    {
        if(*s>='A'&&*s<='Z')
        {
            *s=*s+32;
        }
        s++;
    }
}
int main()
{
    char s[255];
    scanf("%255s",s);
    change(s);
    printf("%s",s);
    return 0;
}