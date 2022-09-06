def domain_name(url):
    url = url.replace('http://', '')
    url = url.replace('http://www.', '')
    url = url.replace('https://', '')
    url = url.replace('www.', '')
    url = url.replace('https://www.', '')

    for i in range(len(url)):
        if url[i] == '.':
            end = i
            break
    return url[:i]


print(domain_name("https://www.cnet.com"))
