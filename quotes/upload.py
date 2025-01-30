from models import Author, Tag, Quote
import json

authors = []
quotes = []
tags = []

if __name__ == '__main__':
    Quote.drop_collection()
    Author.drop_collection()
    with open("authors.json", "r", encoding="utf-8") as f:
        authors_temp = json.load(f)
        for author in authors_temp:
            autor = Author(\
                        fullname=author["fullname"]\
                        ,born_date=author["born_date"]\
                        ,born_location=author["born_location"]\
                        ,description=author["description"]\
                        )
            autor.save()
            authors.append(autor)

    with open("quotes.json", "r", encoding="utf-8") as f:
        quootes = json.load(f)

        for quote in quootes:
            author = None
            for autor in authors:
                if(autor.fullname == quote["author"]):
                    author = autor
            if(author == None):
                raise Exception(f"No author with the name {quote.author}")
            
            taggs = []
            for tag in quote["tags"]:
                if(tag not in tags):
                    tagg = Tag(name=tag)
                    taggs.append(tagg)
                    tags.append(tagg)
                else:
                    for tagg in tags:
                        if(tagg.name == tag):
                            taggs.append(tagg)
            quote = quote["quote"]
            quoote = Quote(
                            tags=taggs,\
                            author=author,\
                            quote=quote,\
                          )
            quoote.save()
            quotes.append(quoote)
    
    for author in authors:
        author.save()
    for quote in quotes:
        quote.save()