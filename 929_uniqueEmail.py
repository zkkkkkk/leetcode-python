#-*-coding:utf-8 -*-
class Solution:
    def numUniqueEmails(self, emails):
        """
        :param emails:alice@leetcode.com,本地名称中的.会被忽略，+后面的部分会被忽略.判断字符串数组中会发给多少个邮件
        :return:地址数量
        """
        uniqueSet = set()
        for email in emails:
            localaddress = email.split("@")
            pre = localaddress[0].split('+')
            actualEmail = pre[0].replace('.', '')
            uniqueSet.add(actualEmail + localaddress[1])
        return len(uniqueSet)
test = Solution()
print(test.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
