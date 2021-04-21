def test(theurl):
    thepage = urlopen(theurl).read()
    soup = BeautifulSoup(thepage)
    images = soup.findAll("img")
    for image in images:
        yield image["src"]

