def generate_hashtag(s):
    l = len(s)
    if l >= 140 or l == 0:
        return False
    else:
        s = s.split()
        hashtag = '#'
        for i in range(len(s)):
            hashtag = hashtag + s[i].capitalize()
        return hashtag


print(generate_hashtag(" Hello there thanks for trying my Kata"))
