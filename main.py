import scrython
import imageio
import requests
import proxy
import time
import json
import constants as co

def process_card(cardname, expansion=None):

    if co.DEBUG == 1:
        with open('data.json') as handle:
            card = json.loads(handle.read())
    else:

        try:
            # If the card specifies which set to retrieve the scan from, do that
            if expansion:
                # Set specified from set formatter
                query = "!\"" + cardname + "\" set=" + expansion
                print("Processing: " + cardname + ", set: " + expansion)
            else:
                query = "!\"" + cardname + "\""
                print("Processing: " + cardname)
            card = scrython.cards.Search(q=query).data()[0]
            #with open('data.json', 'w') as f:
                #f.write(json.dumps(card))

        except scrython.foundation.ScryfallError:
            print("Couldn't find card: " + cardname)
            return




    cardname = card["name"].replace("//", "&")  # should work on macOS & windows now
    cardname = cardname.replace(":", "")  # case for Circle of Protection:

    im = imageio.imread(card["image_uris"]['art_crop'])
    imageio.imwrite('./art.png', im)

    proxy.proxy(im, card)

 
def main():
    with open('cards.txt', 'r') as cards:
        for card in cards:
            card = card.rstrip()
            card = card[2:]
            print(card)
            try:
                pipe_idx = card.index("|")
                process_card(card[0:pipe_idx], card[pipe_idx+1:])
            except ValueError:
                process_card(card)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
