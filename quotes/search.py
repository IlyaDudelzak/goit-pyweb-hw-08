from models import Author, Tag, Quote

def print_quote(quote:Quote):
    print(f"{quote.author.fullname}: {quote.quote}")

if __name__ == '__main__':
    while True:
        try:
            cmd = input("Enter command: ").split(":")
            args = None
            if(len(cmd) > 1):
                args = cmd[1].removeprefix(" ")
                args =  args.split(",")
            cmd = cmd[0]
            match(cmd):
                case "name":
                    for quote in Quote.objects:
                        if(quote.author.fullname == args[0]):
                            print_quote(quote)
                case "tag":
                    for quote in Quote.objects:
                        for tag in args:
                            should_break = False
                            for tagg in quote.tags:
                                if(tagg.name == tag):
                                    print_quote(quote)
                                    should_break = True
                                    break
                            if(should_break):
                                break
                case "exit":
                    exit()
        except KeyboardInterrupt:
            print("exit")
            exit()
        
