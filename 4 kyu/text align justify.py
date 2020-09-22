# https://www.codewars.com/kata/537e18b6147aa838f600001b/python

test_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ullamcorper a lacus vestibulum sed. Ut morbi tincidunt augue interdum velit euismod in. Pulvinar sapien et ligula ullamcorper. Scelerisque eleifend donec pretium vulputate sapien. Consectetur adipiscing elit duis tristique sollicitudin nibh. Justo laoreet sit amet cursus sit amet dictum. Aenean et tortor at risus viverra adipiscing. Tellus in hac habitasse platea. In ornare quam viverra orci sagittis eu volutpat odio. Mi tempus imperdiet nulla malesuada pellentesque elit eget gravida cum. Urna et pharetra pharetra massa massa ultricies mi. Nunc consequat interdum varius sit amet mattis. Massa massa ultricies mi quis hendrerit dolor magna eget. Odio euismod lacinia at quis risus sed vulputate."""


def justify(text: str, width: int):
    words = text.strip().split(" ")
    sent = list()
    cur_len = 0
    if len(words) == 0:
        return ""
    word = words.pop(0)
    out = ""

    while True:
        cur_len += len(word)
        sent.append(word)
        if cur_len + len(sent) - 1 <= width:
            if len(words) != 0:
                word = words.pop(0)
            else:
                s = ""
                if len(sent) > 1:
                    for i in sent[:-1]:
                        s += i + " "
                s += sent[-1]
                out += s
                break
        else:
            sent.pop()
            s = ""
            if len(sent) > 1:
                ones = [1] * (len(sent) - 1)
                for i in range(width - (cur_len - len(word) + len(sent) - 1)):
                    ones[i % len(ones)] += 1

                for i in range(len(sent) - 1):
                    s += sent[i] + " " * ones[i]
            s += sent[-1] + "\n"
            cur_len = 0
            sent = list()
            out += s
    return out
print(justify(test_text[:250], 30))


# best solution

def justify(text, width):
    length = text.rfind(' ', 0, width+1)
    if length == -1 or len(text) <= width: return text
    line = text[:length]
    spaces = line.count(' ')
    if spaces != 0:
        expand = (width - length) // spaces + 1
        extra = (width - length) % spaces
        line = line.replace(' ', ' '*expand)
        line = line.replace(' '*expand, ' '*(expand+1), extra)
    return line + '\n' + justify(text[length+1:], width)

print(justify(test_text[:250], 30))


