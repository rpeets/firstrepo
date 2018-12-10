#
# https://www.codewars.com/kata/camelcase-method/train/python
#

def camel_case(string):
    return ''.join([i for i in string.title() if i.isalpha()])

def main():
    '''
    '''
    pass

print(camel_case("test case"), "TestCase")
print(camel_case("camel case method"), "CamelCaseMethod")
print(camel_case("say hello "), "SayHello")
print(camel_case(" camel case word"), "CamelCaseWord")
print(camel_case(""), "")
