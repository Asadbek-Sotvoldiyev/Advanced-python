def get_hashtag(text):
    a = text.split()
    result = "#"+a[0].title()
    for i in a[1:]:
        result+=i.title()
    return result

print(get_hashtag('Hello World thanks for you'))
# result: #HelloWorldThanksForYou